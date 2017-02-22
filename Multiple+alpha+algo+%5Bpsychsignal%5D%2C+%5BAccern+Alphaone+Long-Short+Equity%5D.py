
# coding: utf-8

# In[1]:

#Psychsignal

from quantopian.algorithm import attach_pipeline, pipeline_output
from quantopian.pipeline import Pipeline
from quantopian.pipeline.factors import CustomFactor, SimpleMovingAverage, AverageDollarVolume, Latest, RSI
from quantopian.pipeline.data.builtin import USEquityPricing
from quantopian.pipeline.data import morningstar as mstar
from quantopian.pipeline.filters.morningstar import IsPrimaryShare
from quantopian.pipeline.data.psychsignal import stocktwits
from quantopian.pipeline.classifiers.morningstar import Sector
from quantopian.pipeline.data import morningstar

import numpy as np
import pandas as pd

class Value(CustomFactor):
    
    inputs = [morningstar.valuation_ratios.book_value_yield,
              morningstar.valuation_ratios.sales_yield,
              morningstar.valuation_ratios.fcf_yield] 
    
    window_length = 1
    
    def compute(self, today, assets, out, book_value, sales, fcf):
        value_table = pd.DataFrame(index=assets)
        value_table["book_value"] = book_value[-1]
        value_table["sales"] = sales[-1]
        value_table["fcf"] = fcf[-1]
        out[:] = value_table.rank().mean(axis=1)

class Momentum(CustomFactor):
    
    inputs = [USEquityPricing.close]
    window_length = 252
    
    def compute(self, today, assets, out, close):       
        out[:] = close[-20] / close[0]

class MessageVolume(CustomFactor):
    inputs = [stocktwits.total_scanned_messages]
    window_length = 21
    def compute(self, today, assets, out, msgs):
        out[:] = -np.nansum(msgs, axis=0)
        
def make_pipeline():
    """
    Create and return our pipeline.
    
    We break this piece of logic out into its own function to make it easier to
    test and modify in isolation.
    
    In particular, this function can be copy/pasted into research and run by itself.
    """
    pipe = Pipeline()
    
    initial_screen = filter_universe()

    factors = {
        "Message": MessageVolume(mask=initial_screen),
        "Momentum": Momentum(mask=initial_screen),
        "Value": Value(mask=initial_screen),
    }
    
    clean_factors = None
    for name, factor in factors.items():
        if not clean_factors:
            clean_factors = factor.isfinite()
        else:
            clean_factors = clean_factors & factor.isfinite()  
            
    combined_rank = None
    for name, factor in factors.items():
        if not combined_rank:
            combined_rank = factor.rank(mask=clean_factors)
        else:
            combined_rank += factor.rank(mask=clean_factors)
    pipe.add(combined_rank, 'factor')

    # Build Filters representing the top and bottom 200 stocks by our combined ranking system.
    # We'll use these as our tradeable universe each day.
    longs = combined_rank.percentile_between(80, 90)
    shorts = combined_rank.percentile_between(10, 20)
    
    pipe.set_screen(longs | shorts)
    
    pipe.add(longs, 'longs')
    pipe.add(shorts, 'shorts')
    return pipe


def initialize(context):
    context.long_leverage = 1.0
    context.short_leverage = -1.0
    context.spy = sid(8554)
    
    attach_pipeline(make_pipeline(), 'ranking_example')
    
    # Used to avoid purchasing any leveraged ETFs 
    context.dont_buys = security_lists.leveraged_etf_list
     
    # Schedule my rebalance function
    schedule_function(func=rebalance, 
                      date_rule=date_rules.month_start (days_offset=0), 
                      time_rule=time_rules.market_open(hours=0,minutes=30), 
                      half_days=True)
    
    # Schedule a function to plot leverage and position count
    schedule_function(func=record_vars, 
                      date_rule=date_rules.every_day(), 
                      time_rule=time_rules.market_close(), 
                      half_days=True)

def before_trading_start(context, data):
    # Call pipeline_output to get the output
    # Note this is a dataframe where the index is the SIDs for all 
    # securities to pass my screen and the columns are the factors which
    output = pipeline_output('ranking_example')
    ranks = output['factor']
    
    long_ranks = ranks[output['longs']].rank()
    short_ranks = ranks[output['shorts']].rank()

    context.long_weights = (long_ranks / long_ranks.sum())
    log.info("Long Weights:")
    log.info(context.long_weights)
    
    context.short_weights = (short_ranks / short_ranks.sum())
    log.info("Short Weights:")
    log.info(context.short_weights)
    
    context.active_portfolio = context.long_weights.index.union(context.short_weights.index)


def record_vars(context, data):  
    
    # Record and plot the leverage, number of positions, and expsoure of our portfolio over time. 
    record(num_positions=len(context.portfolio.positions),
           exposure=context.account.net_leverage, 
           leverage=context.account.leverage)
    

# This function is scheduled to run at the start of each month.
def rebalance(context, data):
    """
    Allocate our long/short portfolio based on the weights supplied by
    context.long_weights and context.short_weights.
    """
    # Order our longs.
    log.info("ordering longs")
    for long_stock, long_weight in context.long_weights.iterkv():
        if data.can_trade(long_stock):
            if long_stock in context.dont_buys:
                continue
            order_target_percent(long_stock, context.long_leverage * long_weight)
    
    # Order our shorts.
    log.info("ordering shorts")
    for short_stock, short_weight in context.short_weights.iterkv():
        if data.can_trade(short_stock):
            if short_stock in context.dont_buys:
                continue
            order_target_percent(short_stock, context.short_leverage * short_weight)
    
    # Sell any positions in assets that are no longer in our target portfolio.
    for security in context.portfolio.positions:
        if data.can_trade(security):  # Work around inability to sell de-listed stocks.
            if security not in context.active_portfolio:
                order_target_percent(security, 0)
       
def filter_universe():  
    """
    9 filters:
        1. common stock
        2 & 3. not limited partnership - name and database check
        4. database has fundamental data
        5. not over the counter
        6. not when issued
        7. not depository receipts
        8. primary share
        9. high dollar volume
    Check Scott's notebook for more details.
    """
    common_stock = mstar.share_class_reference.security_type.latest.eq('ST00000001')
    not_lp_name = ~mstar.company_reference.standard_name.latest.matches('.* L[\\. ]?P\.?$')
    not_lp_balance_sheet = mstar.balance_sheet.limited_partnership.latest.isnull()
    have_data = mstar.valuation.market_cap.latest.notnull()
    not_otc = ~mstar.share_class_reference.exchange_id.latest.startswith('OTC')
    not_wi = ~mstar.share_class_reference.symbol.latest.endswith('.WI')
    not_depository = ~mstar.share_class_reference.is_depositary_receipt.latest
    primary_share = IsPrimaryShare()
    
    # Combine the above filters.
    tradable_filter = (common_stock & not_lp_name & not_lp_balance_sheet &
                       have_data & not_otc & not_wi & not_depository & primary_share)
    
    high_volume_tradable = AverageDollarVolume(
            window_length=21,
            mask=tradable_filter
        ).rank(ascending=False) < 500

    mask = high_volume_tradable
    
    return mask


# In[ ]:

#Accern Alphaone Long-Short Equity

import pandas as pd
import numpy as np

from quantopian.algorithm import attach_pipeline, pipeline_output
from quantopian.pipeline import Pipeline
from quantopian.pipeline.factors import CustomFactor, AverageDollarVolume
from quantopian.pipeline.classifiers.morningstar import Sector

# Sample Version available from 26 Aug 2012 - 08 Feb 2014
from quantopian.pipeline.data.accern import alphaone_free as alphaone

# Premium Version found at https://www.quantopian.com/data/accern/alphaone
# from quantopian.pipeline.data.accern import alphaone as alphaone

class WeightedSentimentByVolatility(CustomFactor):
    # Economic Hypothesis: Sentiment volatility can be an indicator that
    # public news is changing rapidly about a given security. So securities
    # with a high level of sentiment volatility may indicate a change in
    # momentum for that stock's price.
    inputs = [alphaone.article_sentiment]
    window_length = 30
    
    def compute(self, today, assets, out, sentiment):
        out[:] = np.nanstd(sentiment, axis=0) * np.nanmean(sentiment, axis=0)
    
def make_pipeline():

    
    # Screen out penny stocks and low liquidity securities.
    dollar_volume = AverageDollarVolume(window_length=20)
    is_liquid = dollar_volume.rank(ascending=False) < 1000
    
    # Create the mask that we will use for our percentile methods.
    base_universe = (is_liquid)

    # Filter down to stocks in the top/bottom 10% by sentiment rank
    factor = WeightedSentimentByVolatility()
    longs = factor.percentile_between(90, 100, mask=base_universe)
    shorts = factor.percentile_between(0, 10, mask=base_universe)

    # Add Accern to the Pipeline
    pipe_columns = {
         'longs':longs,
         'shorts':shorts
    }

    # Set our pipeline screens
    pipe_screen = (longs | shorts) & (factor != 0)


    # Create our pipeline
    pipe = Pipeline(columns = pipe_columns, screen = pipe_screen) 
    return pipe

# Put any initialization logic here. The context object will be passed to
# the other methods in your algorithm.
def initialize(context):
    attach_pipeline(make_pipeline(), name='factors')
    
    # Create our scheduled functions
    schedule_function(rebalance, date_rules.month_start())
    schedule_function(record_positions, date_rules.every_day(),
                      time_rules.market_close())

    set_commission(commission.PerShare(cost=0, min_trade_cost=0))
    set_slippage(slippage.FixedSlippage(spread=0))

def before_trading_start(context, data):
    # Assign long and short baskets
    results = pipeline_output('factors')
    assets_in_universe = results.index
    context.longs = assets_in_universe[results.longs]
    context.shorts = assets_in_universe[results.shorts]
    
def record_positions(context, data):
    # Record our leverage, exposure, positions, and number of open
    # orders
    record(lever=context.account.leverage,
           exposure=context.account.net_leverage,
           num_pos=len(context.portfolio.positions),
           oo=len(get_open_orders()))
    
def rebalance(context, data):
    short_weight = -1.0/len(context.shorts)
    long_weight = 1.0/len(context.longs)
    assets_in_universe = (context.longs  | context.shorts)

    # Order our shorts
    for security in context.shorts:
        if data.can_trade(security):
            order_target_percent(security, short_weight)
            
    # Order our longs
    for security in context.longs:
        if data.can_trade(security):
            order_target_percent(security, long_weight)
            
    # Order securities not in the portfolio
    for security in context.portfolio.positions:
        if data.can_trade(security):
            if security not in assets_in_universe:
                order_target_percent(security, 0)


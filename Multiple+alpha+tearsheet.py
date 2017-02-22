
# coding: utf-8

# In[1]:

bt2 = get_backtest('589dd1a1894fc1615b741719') #psychsignal algo  very good sharpe ratio!

Entire data start date: 2012-05-04
Entire data end date: 2013-05-03


Backtest Months: 11
Performance statistics	Backtest
annual_return	0.20
cum_returns_final	0.20
annual_volatility	0.08
sharpe_ratio	2.23
calmar_ratio	6.33
stability_of_timeseries	0.94
max_drawdown	-0.03
omega_ratio	1.46
sortino_ratio	3.70
skew	0.38
kurtosis	1.45
tail_ratio	1.26
common_sense_ratio	1.51
gross_leverage	1.86
information_ratio	0.01
alpha	0.21
beta	-0.12
Worst drawdown periods	net drawdown in %	peak date	valley date	recovery date	duration
0	3.19	2012-08-02	2012-08-09	2012-09-07	27
1	2.80	2012-06-11	2012-07-05	2012-07-16	26
2	2.20	2012-11-09	2012-11-15	2012-12-03	17
3	2.09	2012-12-17	2013-01-14	2013-02-22	50
4	1.82	2012-07-23	2012-07-27	2012-08-02	9


[-0.01 -0.02]

usr(/local/lib/python2.7/dist-packages/numpy/lib/function_base.py:3834:, RuntimeWarning:, Invalid, value, encountered, in, percentile)
  RuntimeWarning)
Stress Events	mean	min	max
EZB IR Event	0.11%	-0.94%	1.00%
Recovery	0.07%	-1.43%	2.43%
New Normal	0.09%	-0.85%	1.62%

Top 10 long positions of all time	max
HRI-32887	4.65%
GPS-3321	4.63%
BSX-1131	4.49%
TEX-7408	4.34%
STT-7139	4.26%
KLAC-4246	4.26%
DISC_A-36930	4.23%
BG-22959	4.18%
MPC-41636	4.18%
WBA-8089	4.17%
Top 10 short positions of all time	max
BBY-754	-5.22%
ANF-15622	-5.17%
DDD-12959	-4.88%
LNG-22096	-4.44%
NVDA-19725	-4.35%
ADSK-67	-4.32%
CLR-33856	-4.28%
NTAP-13905	-4.26%
SWKS-23821	-4.23%
NBR-5214	-4.22%
Top 10 positions of all time	max
BBY-754	5.22%
ANF-15622	5.17%
DDD-12959	4.88%
HRI-32887	4.65%
GPS-3321	4.63%
BSX-1131	4.49%
LNG-22096	4.44%
NVDA-19725	4.35%
TEX-7408	4.34%
ADSK-67	4.32%
All positions ever held	max
BBY-754	5.22%
ANF-15622	5.17%
DDD-12959	4.88%
HRI-32887	4.65%
GPS-3321	4.63%
BSX-1131	4.49%
LNG-22096	4.44%
NVDA-19725	4.35%
TEX-7408	4.34%
ADSK-67	4.32%
CLR-33856	4.28%
STT-7139	4.26%
NTAP-13905	4.26%
KLAC-4246	4.26%
DISC_A-36930	4.23%
SWKS-23821	4.23%
NBR-5214	4.22%
BG-22959	4.18%
MPC-41636	4.18%
CMI-1985	4.18%
WBA-8089	4.17%
PH-5956	4.17%
JPM-25006	4.17%
AAPL-24	4.16%
NAV-5199	4.16%
AET-168	4.15%
MS-17080	4.15%
PG-5938	4.13%
OC-32608	4.13%
APA-448	4.12%
...	...
ILMN-21774	0.78%
SJM-21935	0.77%
FLR-24833	0.69%
CHRW-17632	0.67%
FFIV-20208	0.66%
CE-26960	0.64%
KBH-4199	0.63%
EXC-22114	0.62%
FDO-2760	0.61%
KMI-40852	0.58%
DUK-2351	0.57%
INFA-19990	0.56%
MRX-13692	0.56%
TRW-25948	0.54%
FSLR-32902	0.51%
FIO-41554	0.46%
YNDX-41484	0.45%
RHI-6465	0.44%
GT-3384	0.41%
PII-6992	0.34%
STWD-38668	0.33%
DG-38936	0.31%
SD-35006	0.30%
PLD-24785	0.27%
ARUN-33588	0.26%
ORLY-8857	0.25%
ROST-6546	0.17%
GPRO-24003	0.12%
CCI-19258	0.08%
CHK-8461	0.08%
441 rows × 1 columns



# In[ ]:

bt = get_backtest('589dd0891014f35df98ad8ad') #Accern Alphaone Long-Short Equity backtest

Entire data start date: 2013-01-02
Entire data end date: 2013-12-31


Backtest Months: 12
Performance statistics	Backtest
annual_return	0.06
cum_returns_final	0.06
annual_volatility	0.04
sharpe_ratio	1.25
calmar_ratio	1.62
stability_of_timeseries	0.85
max_drawdown	-0.03
omega_ratio	1.22
sortino_ratio	1.86
skew	-0.16
kurtosis	-0.06
tail_ratio	1.09
common_sense_ratio	1.15
gross_leverage	2.01
information_ratio	-0.12
alpha	0.05
beta	0.03
Worst drawdown periods	net drawdown in %	peak date	valley date	recovery date	duration
0	3.43	2013-10-22	2013-12-24	NaT	NaN
1	1.88	2013-05-20	2013-06-28	2013-07-18	44
2	1.61	2013-07-31	2013-08-19	2013-08-26	19
3	1.38	2013-02-12	2013-03-12	2013-04-01	35
4	0.89	2013-04-02	2013-04-25	2013-05-08	27


[-0.005 -0.01 ]

Stress Events	mean	min	max
New Normal	0.02%	-0.88%	0.68%

Top 10 long positions of all time	max
SCTY-43721	2.07%
CLDX-19187	1.90%
TSL-33067	1.90%
SNE-6984	1.69%
AEGR-40294	1.68%
CSIQ-32856	1.68%
SRPT-16999	1.64%
VLO-7990	1.53%
CIEN-16453	1.52%
JAZZ-33959	1.52%
Top 10 short positions of all time	max
ARIA-11880	-2.60%
QIHU-41149	-1.68%
BIDU-27533	-1.68%
LNKD-41451	-1.63%
YOKU-40562	-1.59%
DRYS-26994	-1.57%
INFI-21744	-1.57%
ATVI-9883	-1.56%
JCP-4118	-1.56%
TPX-25802	-1.55%
Top 10 positions of all time	max
ARIA-11880	2.60%
SCTY-43721	2.07%
CLDX-19187	1.90%
TSL-33067	1.90%
SNE-6984	1.69%
QIHU-41149	1.68%
AEGR-40294	1.68%
CSIQ-32856	1.68%
BIDU-27533	1.68%
SRPT-16999	1.64%
All positions ever held	max
ARIA-11880	2.60%
SCTY-43721	2.07%
CLDX-19187	1.90%
TSL-33067	1.90%
SNE-6984	1.69%
QIHU-41149	1.68%
AEGR-40294	1.68%
CSIQ-32856	1.68%
BIDU-27533	1.68%
SRPT-16999	1.64%
LNKD-41451	1.63%
YOKU-40562	1.59%
DRYS-26994	1.57%
INFI-21744	1.57%
ATVI-9883	1.56%
JCP-4118	1.56%
TPX-25802	1.55%
XIV-40516	1.54%
VLO-7990	1.53%
GT-3384	1.52%
NPSP-11356	1.52%
CIEN-16453	1.52%
JAZZ-33959	1.52%
VMW-34545	1.52%
IOC-26617	1.50%
HCA-41047	1.50%
INFY-19894	1.50%
BBRY-19831	1.50%
AGN-8572	1.49%
MTG-5092	1.49%
...	...
BNS-1010	1.20%
IONS-4031	1.20%
PPL-6119	1.20%
VIPS-42707	1.20%
UN-7784	1.20%
IVR-38531	1.20%
KSU-4315	1.20%
SRE-24778	1.20%
NTI-43228	1.19%
FLO-2876	1.19%
CVS-4799	1.19%
BITA-40419	1.19%
GILD-3212	1.19%
VRSK-38817	1.19%
VAR-7904	1.19%
GSK-3242	1.18%
LNC-4498	1.18%
OUTR-24791	1.18%
TIBX-20438	1.18%
GFI-9936	1.18%
DSW-27409	1.18%
HSY-3695	1.18%
EL-13841	1.18%
ALL-24838	1.18%
ARR-35162	1.18%
SUNE-13306	1.17%
KMI-40852	1.17%
SQQQ-39211	1.16%
HTS-36111	1.16%
SIRI-11901	1.16%
738 rows × 1 columns


In [4]:

bt2 = get_backtest('589dd1a1894fc1615b741719') #psychsignal algo  very good sharpe ratio!
100% Time: 0:00:01|###########################################################|
In [6]:

bt2.create_full_tear_sheet()
Entire data start date: 2012-05-04
Entire data end date: 2013-05-03


Backtest Months: 11
Performance statistics	Backtest
annual_return	0.20
cum_returns_final	0.20
annual_volatility	0.08
sharpe_ratio	2.23
calmar_ratio	6.33
stability_of_timeseries	0.94
max_drawdown	-0.03
omega_ratio	1.46
sortino_ratio	3.70
skew	0.38
kurtosis	1.45
tail_ratio	1.26
common_sense_ratio	1.51
gross_leverage	1.86
information_ratio	0.01
alpha	0.21
beta	-0.12
Worst drawdown periods	net drawdown in %	peak date	valley date	recovery date	duration
0	3.19	2012-08-02	2012-08-09	2012-09-07	27
1	2.80	2012-06-11	2012-07-05	2012-07-16	26
2	2.20	2012-11-09	2012-11-15	2012-12-03	17
3	2.09	2012-12-17	2013-01-14	2013-02-22	50
4	1.82	2012-07-23	2012-07-27	2012-08-02	9


[-0.01 -0.02]

usr(/local/lib/python2.7/dist-packages/numpy/lib/function_base.py:3834:, RuntimeWarning:, Invalid, value, encountered, in, percentile)
  RuntimeWarning)
Stress Events	mean	min	max
EZB IR Event	0.11%	-0.94%	1.00%
Recovery	0.07%	-1.43%	2.43%
New Normal	0.09%	-0.85%	1.62%

Top 10 long positions of all time	max
HRI-32887	4.65%
GPS-3321	4.63%
BSX-1131	4.49%
TEX-7408	4.34%
STT-7139	4.26%
KLAC-4246	4.26%
DISC_A-36930	4.23%
BG-22959	4.18%
MPC-41636	4.18%
WBA-8089	4.17%
Top 10 short positions of all time	max
BBY-754	-5.22%
ANF-15622	-5.17%
DDD-12959	-4.88%
LNG-22096	-4.44%
NVDA-19725	-4.35%
ADSK-67	-4.32%
CLR-33856	-4.28%
NTAP-13905	-4.26%
SWKS-23821	-4.23%
NBR-5214	-4.22%
Top 10 positions of all time	max
BBY-754	5.22%
ANF-15622	5.17%
DDD-12959	4.88%
HRI-32887	4.65%
GPS-3321	4.63%
BSX-1131	4.49%
LNG-22096	4.44%
NVDA-19725	4.35%
TEX-7408	4.34%
ADSK-67	4.32%
All positions ever held	max
BBY-754	5.22%
ANF-15622	5.17%
DDD-12959	4.88%
HRI-32887	4.65%
GPS-3321	4.63%
BSX-1131	4.49%
LNG-22096	4.44%
NVDA-19725	4.35%
TEX-7408	4.34%
ADSK-67	4.32%
CLR-33856	4.28%
STT-7139	4.26%
NTAP-13905	4.26%
KLAC-4246	4.26%
DISC_A-36930	4.23%
SWKS-23821	4.23%
NBR-5214	4.22%
BG-22959	4.18%
MPC-41636	4.18%
CMI-1985	4.18%
WBA-8089	4.17%
PH-5956	4.17%
JPM-25006	4.17%
AAPL-24	4.16%
NAV-5199	4.16%
AET-168	4.15%
MS-17080	4.15%
PG-5938	4.13%
OC-32608	4.13%
APA-448	4.12%
...	...
ILMN-21774	0.78%
SJM-21935	0.77%
FLR-24833	0.69%
CHRW-17632	0.67%
FFIV-20208	0.66%
CE-26960	0.64%
KBH-4199	0.63%
EXC-22114	0.62%
FDO-2760	0.61%
KMI-40852	0.58%
DUK-2351	0.57%
INFA-19990	0.56%
MRX-13692	0.56%
TRW-25948	0.54%
FSLR-32902	0.51%
FIO-41554	0.46%
YNDX-41484	0.45%
RHI-6465	0.44%
GT-3384	0.41%
PII-6992	0.34%
STWD-38668	0.33%
DG-38936	0.31%
SD-35006	0.30%
PLD-24785	0.27%
ARUN-33588	0.26%
ORLY-8857	0.25%
ROST-6546	0.17%
GPRO-24003	0.12%
CCI-19258	0.08%
CHK-8461	0.08%
441 rows × 1 columns





#!/usr/bin/env python
# coding: utf-8

# # RCB vs KXIP

# **-by sindhura gundubogula**
# 
# **STEP-1 import all required python libraries**

# In[419]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# **STEP-2 Load the dataset**

# In[420]:


deliveries = pd.read_csv("deliveries.csv")
matches    = pd.read_csv("matches.csv")


# In[421]:


deliveries.head()


# In[422]:


matches.head()


# In[423]:


deliveries.info()


# In[424]:


matches.info()


# **QUESTION1 : WHO WILL WIN THE MATCH?**

# **performing exploratory data analysis only on RCB VS KXIP match data**

# In[425]:


matches['team1'].unique()


# In[426]:


BP = matches.loc[(matches['team1'] == 'Royal Challengers Bangalore') & (matches['team2'] == 'Kings XI Punjab')]
BP


# In[427]:


PB = matches.loc[(matches['team2'] == 'Royal Challengers Bangalore') & (matches['team1'] == 'Kings XI Punjab')]
PB


# In[428]:


rcb_vs_kp= pd.DataFrame({'team1':BP['team1'],'team2':BP['team2'],'winner':BP['winner']})  


# In[429]:


rcb_vs_kp


# In[430]:


kp_vs_rcb= pd.DataFrame({'team1':PB['team1'],'team2':PB['team2'],'winner':PB['winner']})  


# In[431]:


kp_vs_rcb


# In[432]:


frames = [rcb_vs_kp,kp_vs_rcb]
RCBvsKP = pd.concat(frames)


# In[433]:


RCBvsKP


# In[434]:


RCBvsKP['winner'].value_counts()


# we can see that both teams won equally against each other

# lets analyze overall win data

# In[435]:


plt.figure(figsize=(8,4))
ax = sns.countplot(x='winner',data=matches, order = matches['winner'].value_counts().index)

ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
plt.tight_layout()
plt.title('visualization based on number of wins of SRH and CSK in all the matches')
plt.show()


# From the above visualizations we can observe that **RCB** has more wins compared to **KXIP**

# Lets find out number of matches played by RCB and KXIP

# In[436]:


a = matches.loc[(matches['team1'] == 'Royal Challengers Bangalore')]


# In[437]:


b = matches.loc[(matches['team1'] == 'Kings XI Punjab')]


# In[438]:


c = matches.loc[(matches['team2'] == 'Royal Challengers Bangalore')]


# In[439]:


d = matches.loc[(matches['team2'] == 'Kings XI Punjab')]


# In[440]:


a1 = pd.DataFrame({'team':a['team1'],'winner':a['winner']})  


# In[441]:


b1 = pd.DataFrame({'team':b['team1'],'winner':b['winner']})  


# In[442]:


c1 = pd.DataFrame({'team':c['team2'],'winner':c['winner']})  


# In[443]:


d1 = pd.DataFrame({'team':d['team2'],'winner':d['winner']})  


# In[444]:


frames = [a1,b1,c1,d1]
total = pd.concat(frames)


# In[445]:


total


# In[446]:


total.index.unique()


# In[447]:


total.index.drop_duplicates(keep='first')


# In[448]:


total['team'].value_counts()


# In[449]:


total['winner'].value_counts()


# calculating the win probability manually = total wins/ total matches played

# In[450]:


win_probability_RCB = 96/180

win_probability_RCB


# In[451]:


win_probability_KXIP = 94/176

win_probability_KXIP


# **Answer:** BOTH TEAMS HAVE EQUAL PROBABILITY OF WINNING, HOWEVER KXIP HAS 0.1% HIGHER PROBABILITY THAN RCB

# **how many 6 will be hit in todays match?**

# In[452]:



run6kb =deliveries.loc[(deliveries['batting_team'] == 'Kings XI Punjab') & (deliveries['bowling_team'] == 'Royal Challengers Bangalore')]

run6kb


# In[453]:


run6kb = run6kb[run6kb['batsman_runs']==6]


# In[454]:


Total_6_per_matchkb = run6kb.groupby('match_id')['batsman_runs'].count()


# In[455]:


RUN6kb = pd.DataFrame({'total 6':Total_6_per_matchkb})  


# In[456]:


RUN6kb


# In[457]:


run6bk =deliveries.loc[(deliveries['batting_team'] == 'Royal Challengers Bangalore') & (deliveries['bowling_team'] == 'Kings XI Punjab')]

run6bk


# In[458]:


run6bk = run6bk[run6bk['batsman_runs']==6]


# In[459]:


Total_6_per_matchbk = run6bk.groupby('match_id')['batsman_runs'].count()


# In[460]:


RUN6bk = pd.DataFrame({'total 6':Total_6_per_matchbk})  


# In[461]:


RUN6bk


# In[462]:


frames = [RUN6kb,RUN6bk]

total = pd.concat(frames)


# In[463]:


total


# In[464]:


total = total.groupby('match_id')['total 6'].sum()


# In[465]:


total


# In[466]:


total.value_counts()


# In[467]:


total.describe()


# **Answer:** based on above conclusion,  Average most scored 6s are around 12 , so from given options i conclude they might hit 11-14 6's in todays match

# **QUESTION HOW MANY NO BALLS WILL BE BOWLED IN TODAYS MATCH?**

# In[468]:


k = deliveries.loc[(deliveries['bowling_team'] == 'Kings XI Punjab')]

k


# In[469]:


k = k.groupby('match_id')['noball_runs'].sum()

k


# In[470]:


Total_noballs_by_k = pd.DataFrame({'total noballs per match':k}) 

Total_noballs_by_k 


# In[471]:


Total_noballs_by_k['total noballs per match'].value_counts()


# In[472]:


Total_noballs_by_k.describe()


# In[473]:


r = deliveries.loc[(deliveries['bowling_team'] == 'Royal Challengers Bangalore')]

r


# In[474]:


r = r.groupby('match_id')['noball_runs'].sum()
r


# In[475]:


Total_noballs_by_r = pd.DataFrame({'total noballs per match':r}) 

Total_noballs_by_r


# In[476]:


Total_noballs_by_r['total noballs per match'].value_counts()


# In[477]:


Total_noballs_by_r.describe()


# In[478]:


fig, axes = plt.subplots(1, 2,  sharex=True, figsize=(10,5))

ax1 = sns.countplot(ax=axes[0],x='total noballs per match',data=Total_noballs_by_k,order =Total_noballs_by_k['total noballs per match'].value_counts().index)
ax1.set_title('visualization based on noballs in each match by kxip')
ax2 = sns.countplot(ax=axes[1],x='total noballs per match',data=Total_noballs_by_r,order = Total_noballs_by_r['total noballs per match'].value_counts().index)
ax2.set_title('visualization based on noballs in each match by rcb')
plt.show()


# **Answer:** based on both teams bowling analysis, 75% of the time both teams has bowled only 1 no ball per match . So i conclude 1-2 no balls might be bowled in todays match.

# **How many wickets will KXIP lose?**

# analysing kxip vd rcb wickets data

# In[479]:



kxip =deliveries.loc[(deliveries['batting_team'] == 'Kings XI Punjab') & (deliveries['bowling_team'] == 'Royal Challengers Bangalore')]

kxip


# In[480]:


Total_kxip_wickets_per_match =kxip.groupby('match_id')['player_dismissed'].count()


# In[481]:


Total_kxip_wickets_per_match.value_counts()


# In[482]:


Total_kxip_wickets_per_match.describe()


# analysing KPXI overall wickets data

# In[483]:


kxipdata =deliveries.loc[(deliveries['batting_team'] == 'Kings XI Punjab')]
kxipdata 


# In[484]:


Total_k_wickets_per_match =kxipdata.groupby('match_id')['player_dismissed'].count()


# In[485]:


Total_k_wickets_per_match


# In[486]:


Total_k_wickets_per_match.value_counts()


# In[487]:


Total_k_wickets_per_match.describe()


# RCB wickets taken data overall

# In[488]:


rcdata =deliveries.loc[(deliveries['bowling_team'] == 'Royal Challengers Bangalore')]

rcdata 


# In[489]:


Total_rc_wickets_per_match =dcdata.groupby('match_id')['player_dismissed'].count()


# In[490]:


Total_rc_wickets_per_match


# In[491]:


Total_rc_wickets_per_match.value_counts()


# In[492]:


Total_rc_wickets_per_match.describe()


# **Answer:** we analysed in all the possible senarios 
#             1. mean of 6.6 for rcb's total wickets taken data
#             2. mean of 6.1 for kxip's total lost wickets data
#             3. mean of 5.6 for kxip's lost wickets against rcb
#             
#            from the above solutions, i feel kxip might lose 3-5 wickets in todays match
#                                                      

# **how many runs partnership will beput up by kohli and dv villers?**

# In[493]:


part1 = deliveries.loc[(deliveries['batsman'] == 'V Kohli') & (deliveries['non_striker'] == 'AB de Villiers')]
part1                                                                         


# In[494]:


part1 = part1.groupby('match_id')['batsman_runs'].sum()
part1


# In[495]:


part2 = deliveries.loc[(deliveries['batsman'] == 'AB de Villiers') & (deliveries['non_striker'] == 'V Kohli')]
part2  


# In[496]:


part2 = part2.groupby('match_id')['batsman_runs'].sum()
part2


# In[497]:


frames = (part1,part2)

PART = pd.concat(frames)


# In[498]:


PART = PART.groupby('match_id').sum()


# In[499]:


PART


# In[500]:


PART.value_counts()


# In[501]:


PART.describe()


# **answer:** mean is around 40 anf 75% of the results were above 53. so from the provided options, i choose more than 40

# **end of day 3**

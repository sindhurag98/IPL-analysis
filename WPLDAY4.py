#!/usr/bin/env python
# coding: utf-8

# # Delhi capitals vs rajastan royals

# **-by sindhura gundubogula**
# 
# **STEP-1 import all required python libraries**

# In[127]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# **STEP-2 Load the dataset**

# In[128]:


deliveries = pd.read_csv("deliveries.csv")
matches    = pd.read_csv("matches.csv")


# In[129]:


deliveries.head()


# In[130]:


matches.head()


# In[131]:


deliveries.info()


# In[132]:


matches.info()


# **QUESTION1 : WHO WILL WIN THE MATCH?**

# **performing exploratory data analysis only on DC VS RR match data**

# In[133]:


matches['team1'].unique()


# In[134]:


DR = matches.loc[(matches['team1'] == 'Delhi Capitals') & (matches['team2'] == 'Rajasthan Royals')]
DR


# In[135]:


RD = matches.loc[(matches['team2'] == 'Delhi Capitals') & (matches['team1'] == 'Rajasthan Royals')]
RD


# In[136]:


dc_vs_rr= pd.DataFrame({'team1':RD['team1'],'team2':RD['team2'],'winner':RD['winner']})  


# In[137]:


dc_vs_rr


# In[138]:


dc_vs_rr['winner'].value_counts()


# we can see that DC won in both the matches

# In[139]:


matches['winner'].value_counts()


# In[140]:


plt.figure(figsize=(8,4))
ax = sns.countplot(x='winner',data=matches, order = matches['winner'].value_counts().index)

ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
plt.tight_layout()
plt.title('visualization based on number of wins of SRH and CSK in all the matches')
plt.show()


# From the above visualizations we can observe that **RR** has more wins compared to **DC**

# Lets find out number of matches played by DC and RR

# In[141]:


a = matches.loc[(matches['team1'] == 'Delhi Capitals')]


# In[142]:


b = matches.loc[(matches['team1'] == 'Rajasthan Royals')]


# In[143]:


c = matches.loc[(matches['team2'] == 'Delhi Capitals')]


# In[144]:


d = matches.loc[(matches['team2'] == 'Rajasthan Royals')]


# In[145]:


a1 = pd.DataFrame({'team':a['team1'],'winner':a['winner']})  


# In[146]:


b1 = pd.DataFrame({'team':b['team1'],'winner':b['winner']})  


# In[147]:


c1 = pd.DataFrame({'team':c['team2'],'winner':c['winner']})  


# In[148]:


d1 = pd.DataFrame({'team':d['team2'],'winner':d['winner']})  


# In[149]:


frames = [a1,b1,c1,d1]
total = pd.concat(frames)


# In[150]:


total


# In[151]:


total.index.unique()


# In[152]:


total.index.drop_duplicates(keep='first')


# In[153]:


total['team'].value_counts()


# In[154]:


total['winner'].value_counts()


# calculating the win probability manually = total wins/ total matches played

# In[155]:


win_probability_RR = 75/147

win_probability_RR


# In[156]:


win_probability_DC = 12/16

win_probability_DC


# **Answer:** We can conclude that DC can be a winner as it has win probability of 75%

# **how many runs will steve smith score?**

# In[157]:


deliveries['batsman'].unique()


# In[158]:


smith = deliveries.loc[(deliveries['batsman'] == 'SPD Smith')]

smith


# In[159]:


Total_runs_per_match = smith.groupby('match_id')['total_runs'].sum()


# In[160]:


Total_runs_per_match


# In[161]:


Total_runs_smith = pd.DataFrame({'total runs per match':Total_runs_per_match}) 


# In[162]:


Total_runs_smith


# In[163]:


Total_runs_smith['total runs per match'].value_counts()


# In[164]:


plt.figure(figsize=(20,4))
ax = sns.countplot(x='total runs per match',data=Total_runs_smith,order = Total_runs_smith['total runs per match'].value_counts().index)


plt.title('visualization based on runs score')
plt.show()


# In[165]:


Total_runs_smith.describe()


# **Answer:** based on above conclusion,  Average most scored runs are around 30 and mostly he scored 17, so from given options i conclude he might score 16 - 30runs in todays match

# **QUESTION HOW MANY WIDES WILL BE BOWLED IN TODAYS MATCH?**

# In[166]:


DC = deliveries.loc[(deliveries['bowling_team'] == 'Delhi Capitals')]

DC


# In[167]:


DC = DC.groupby('match_id')['wide_runs'].sum()

DC


# In[168]:


Total_wides_by_DC = pd.DataFrame({'total wides per match':DC}) 

Total_wides_by_DC


# In[169]:


Total_wides_by_DC['total wides per match'].value_counts()


# In[170]:


Total_wides_by_DC.describe()


# In[171]:


RR = deliveries.loc[(deliveries['bowling_team'] == 'Rajasthan Royals')]

RR


# In[172]:


RR = RR.groupby('match_id')['wide_runs'].sum()
RR


# In[173]:


Total_wides_by_RR = pd.DataFrame({'total wides per match':RR}) 

Total_wides_by_RR


# In[174]:


Total_wides_by_RR['total wides per match'].value_counts()


# In[175]:


Total_wides_by_RR.describe()


# In[176]:


fig, axes = plt.subplots(1, 2,  sharex=True, figsize=(10,5))

ax1 = sns.countplot(ax=axes[0],x='total wides per match',data=Total_wides_by_DC,order = Total_wides_by_DC['total wides per match'].value_counts().index)
ax1.set_title('visualization based on wides in each match by DC')
ax2 = sns.countplot(ax=axes[1],x='total wides per match',data=Total_wides_by_RR,order = Total_wides_by_RR['total wides per match'].value_counts().index)
ax2.set_title('visualization based on wides in each match by RR')
plt.show()


# **Answer:** based on both teams bowling wides analysis, 75% of the time both teams RR and DC has atleast 6 wides per match . So i conclude more than 6 wides might be bowled in todays match.

# **How many wickets will be taken in todays match?**

# analysing rr vd dc data

# In[177]:



DC_RR =deliveries.loc[(deliveries['batting_team'] == 'Delhi Capitals') & (deliveries['bowling_team'] == 'Rajasthan Royals')]

DC_RR


# In[178]:



RR_DC =deliveries.loc[(deliveries['batting_team'] == 'Rajasthan Royals') & (deliveries['bowling_team'] == 'Delhi Capitals')]

RR_DC


# In[179]:


Total_DC_RR_wickets_per_match =DC_RR.groupby('match_id')['player_dismissed'].count()


# In[180]:


Total_DC_RR_wickets_per_match


# In[181]:


Total_RR_DC_wickets_per_match =RR_DC.groupby('match_id')['player_dismissed'].count()


# In[182]:


Total_RR_DC_wickets_per_match


# analysing RR lost wickets data

# In[183]:


rrdata =deliveries.loc[(deliveries['batting_team'] == 'Rajasthan Royals')]

rrdata 


# In[184]:


Total_RR_wickets_per_match =rrdata.groupby('match_id')['player_dismissed'].count()


# In[185]:


Total_RR_wickets_per_match


# In[186]:


Total_RR_wickets_per_match.value_counts()


# In[187]:


Total_RR_wickets_per_match.describe()


# dc bowling data

# In[188]:


dcdata =deliveries.loc[(deliveries['batting_team'] == 'Delhi Capitals')]

dcdata 


# In[189]:


Total_DC_wickets_per_match =dcdata.groupby('match_id')['player_dismissed'].count()


# In[190]:


Total_DC_wickets_per_match


# In[191]:


Total_DC_wickets_per_match.value_counts()


# In[192]:


Total_DC_wickets_per_match.describe()


# **Answer:** In both the matches played by RR and Dc against each other, One match has count of 10 wickets and other has 14. means of individual wicket data is around 6 and So out of given options i fell 11-15 would fit right

# **end of day 3**

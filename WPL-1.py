#!/usr/bin/env python
# coding: utf-8

# ## Day-1 MI vs DC

# **-by sindhura gundubogula**
# 
# **STEP-1 import all required python libraries**

# In[224]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# **STEP-2 Load the dataset**

# In[225]:


deliveries = pd.read_csv("deliveries.csv")
matches    = pd.read_csv("matches.csv")


# In[226]:


deliveries


# In[227]:


matches


# In[228]:


deliveries.info()


# In[229]:


matches.info()


# **QUESTION1 : WHO WILL WIN THE MATCH?**
# **A) MI  B)DC**

# Obtaining all the game statictics of MI VS DC

# In[230]:


midc = matches.loc[(matches['team1'] == 'Mumbai Indians') & (matches['team2'] == 'Delhi Capitals')]

midc


# Obtaining all the game statictics of DC VS MI

# In[231]:


dcmi = matches.loc[(matches['team1'] == 'Delhi Capitals') & (matches['team2'] == 'Mumbai Indians')]
dcmi


# In[232]:


Dc= pd.DataFrame({'team1':dcmi['team1'],'team2':dcmi['team2'],'winner':dcmi['winner']})  


# In[233]:


Mi= pd.DataFrame({'team1':midc['team1'],'team2':midc['team2'],'winner':midc['winner']})  


# In[234]:


frames = [Mi,Dc]

result = pd.concat(frames)


# In[235]:


result


# so we have only 2 games where each of them won once. 

# plotting the number of wins 

# In[236]:


plt.figure(figsize=(8,4))
ax = sns.countplot(x='winner',data=matches, order = matches['winner'].value_counts().index)

ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
plt.tight_layout()
plt.title('visualization based on number of wins')
plt.show()


# From the above graph we can observe that **Mi** has more wins compared to **Dc**

# **Answer:** So without over analyzing the senario, We can conclude that MI can be a winner as it has more number of wins 

# **QUESTION2 : WHAT WILL THE TOSSING WINNING CAPTAIN WILL DECIDE TO DO FIRST? A) BAT B)BALL**

# Create a new dataframe with only MI and DC toss related data

# In[237]:


a = matches.loc[(matches['team1'] == 'Delhi Capitals')]
   
a


# In[238]:


b = matches.loc[(matches['team2'] == 'Delhi Capitals')]

b


# In[239]:


c=  matches.loc[(matches['team1'] == 'Mumbai Indians')]


# In[240]:


d = matches.loc[(matches['team2'] == 'Mumbai Indians')]


# In[241]:


a1 = pd.DataFrame({'team':a['team1'],'toss_winner':a['toss_winner'],'toss_decision':a['toss_decision']}) 


# In[242]:


b1 = pd.DataFrame({'team':b['team2'],'toss_winner':b['toss_winner'],'toss_decision':b['toss_decision']}) 


# In[243]:


c1 = pd.DataFrame({'team':c['team1'],'toss_winner':c['toss_winner'],'toss_decision':c['toss_decision']}) 


# In[244]:


d1 = pd.DataFrame({'team':d['team2'],'toss_winner':d['toss_winner'],'toss_decision':d['toss_decision']}) 


# In[245]:


frames = [a1,b1,c1,d1]

tossData = pd.concat(frames)


# In[246]:


tossData


# In[247]:


tossData['team'].unique()


# In[248]:


tossData['toss_winner'].value_counts()


# In[249]:


plt.figure(figsize=(8,4))
ax = sns.countplot(x='toss_winner',data=tossData,order = tossData['toss_winner'].value_counts().index)

ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
plt.tight_layout()
plt.title('visualization based on toss wins')
plt.show()


# In[250]:


tossData['toss_decision'] = tossData['toss_decision'].map({'bat':0,'field':1})


# In[251]:


tossData


# In[252]:


tossData['toss_decision'].value_counts()


# **Answer:** From above data, we can see that most of the toss winning captains choose to **Field**

# **QUESTION 3: HOW MANY RUNS WILL ROHITH SHARMA SCORE?**

# In[253]:


deliveries.head()


# In[254]:


deliveries['batsman'].unique()


# Create a new dataframe with Rsharma data

# In[255]:


Rohith = deliveries.loc[(deliveries['batsman'] == 'R Sharma')]


# In[256]:


Rohith


# In[257]:


Rohith['total_runs'].sum() 


# In[258]:


Total_runs_per_match = Rohith.groupby('match_id')['total_runs'].sum()


# In[259]:


Total_runs_per_match


# In[260]:


Total_runs_Rsharma = pd.DataFrame({'total runs per match':Total_runs_per_match}) 


# In[261]:


Total_runs_Rsharma


# In[262]:


plt.figure(figsize=(8,4))
ax = sns.countplot(x='total runs per match',data=Total_runs_Rsharma,order = Total_runs_Rsharma['total runs per match'].value_counts().index)


plt.title('visualization based on runs scord')
plt.show()


# In[263]:


Total_runs_Rsharma.describe()


# **Answer:** based on above conclusion, 75% of the time his most scored runs are around 7.5, so from given options i conclude he might score 0 - 15 runs in todays match

# **QUESTION 4: HOW MANY WICKETS WILL KAGISO RABADA TAKES IN THIS MATCH**

# In[264]:


deliveries['bowler'].unique()


# In[265]:


rabada = deliveries.loc[(deliveries['bowler'] == 'K Rabada')]

rabada


# In[266]:


rabada = rabada.dropna(axis = 0)

rabada


# In[267]:


Total_wickets_per_match = rabada.groupby('match_id')['player_dismissed'].count()


# In[268]:


Total_wickets_per_match 


# In[269]:


Total_wickets_by_Rabada = pd.DataFrame({'total wickets per match':Total_wickets_per_match}) 

Total_wickets_by_Rabada


# In[270]:


plt.figure(figsize=(8,4))
ax = sns.countplot(x='total wickets per match',data=Total_wickets_by_Rabada,order = Total_wickets_by_Rabada['total wickets per match'].value_counts().index)

plt.title('visualization based on wickets taken')
plt.show()


# In[271]:


Total_wickets_by_Rabada.describe()


# **Answer:** based on above conclusion, 75% of the time most taken wickets are around 2.5, so from given options i conclude he might take atleast 2 wickets in todays match

# **QUESTION 5: HOW MANY WIDES WILL BE BOWLED IN TODAYS MATCH?**

# In[272]:


deliveries.head()


# In[273]:


MI = deliveries.loc[(deliveries['bowling_team'] == 'Mumbai Indians')]

MI


# In[274]:


MI = MI.groupby('match_id')['wide_runs'].sum()

MI


# In[275]:


Total_wides_by_MI = pd.DataFrame({'total wides per match':MI}) 

Total_wides_by_MI


# In[276]:


Total_wides_by_MI['total wides per match'].value_counts()


# In[277]:


Total_wides_by_MI.describe()


# In[278]:


DC = deliveries.loc[(deliveries['bowling_team'] == 'Delhi Capitals')]

DC


# In[279]:


DC = DC.groupby('match_id')['wide_runs'].sum()

DC


# In[280]:


Total_wides_by_DC = pd.DataFrame({'total wides per match':DC}) 

Total_wides_by_DC


# In[281]:


Total_wides_by_DC['total wides per match'].value_counts()


# In[282]:


Total_wides_by_DC.describe()


# In[283]:


fig, axes = plt.subplots(1, 2,  sharex=True, figsize=(10,5))

ax1 = sns.countplot(ax=axes[0],x='total wides per match',data=Total_wides_by_DC,order = Total_wides_by_DC['total wides per match'].value_counts().index)
ax1.set_title('visualization based on wides in each match by DC')
ax2 = sns.countplot(ax=axes[1],x='total wides per match',data=Total_wides_by_MI,order = Total_wides_by_MI['total wides per match'].value_counts().index)
ax2.set_title('visualization based on wides in each match by MI')
plt.show()


# **Answer:** based on both teams bowling wides analysis, 75% of the time MI has atleast 7 wides and DC has bowled atleast 6 wides. So i conclude more than 6 wides might be bowled in todays match.

# **end of day 1**

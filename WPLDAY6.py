#!/usr/bin/env python
# coding: utf-8

# # MI vs KKR

# **-by sindhura gundubogula**
# 
# **STEP-1 import all required python libraries**

# In[608]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# **STEP-2 Load the dataset**

# In[609]:


deliveries = pd.read_csv("deliveries.csv")
matches    = pd.read_csv("matches.csv")


# In[610]:


deliveries.head()


# In[611]:


matches.head()


# In[612]:


deliveries.info()


# In[613]:


matches.info()


# **QUESTION1 : WHO WILL WIN THE MATCH?**

# **performing exploratory data analysis only on MI VS KKR match data**

# In[614]:


matches['team1'].unique()


# In[615]:


MK = matches.loc[(matches['team1'] == 'Mumbai Indians') & (matches['team2'] == 'Kolkata Knight Riders')]
MK


# In[616]:


KM = matches.loc[(matches['team2'] == 'Mumbai Indians') & (matches['team1'] == 'Kolkata Knight Riders')]
KM


# In[617]:


mi_vs_k= pd.DataFrame({'team1':MK['team1'],'team2':MK['team2'],'winner':MK['winner']})  


# In[618]:


mi_vs_k


# In[619]:


k_vs_mi= pd.DataFrame({'team1':KM['team1'],'team2':KM['team2'],'winner':KM['winner']})  


# In[620]:


k_vs_mi


# In[621]:


frames = [k_vs_mi,mi_vs_k]
mivskkr = pd.concat(frames)


# In[622]:


mivskkr


# In[623]:


mivskkr['winner'].value_counts()


# lets analyze overall win data

# In[624]:


plt.figure(figsize=(8,4))
ax = sns.countplot(x='winner',data=matches, order = matches['winner'].value_counts().index)

ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
plt.tight_layout()
plt.title('visualization based on number of wins of SRH and CSK in all the matches')
plt.show()


# From the above visualizations we can observe that **MI** has more wins compared to **KKR**

# Lets find out number of matches played by MI and KKR

# In[625]:


a = matches.loc[(matches['team1'] == 'Kolkata Knight Riders')]


# In[626]:


b = matches.loc[(matches['team1'] == 'Mumbai Indians')]


# In[627]:


c = matches.loc[(matches['team2'] == 'Kolkata Knight Riders')]


# In[628]:


d = matches.loc[(matches['team2'] == 'Mumbai Indians')]


# In[629]:


a1 = pd.DataFrame({'team':a['team1'],'winner':a['winner']})  


# In[630]:


b1 = pd.DataFrame({'team':b['team1'],'winner':b['winner']})  


# In[631]:


c1 = pd.DataFrame({'team':c['team2'],'winner':c['winner']})  


# In[632]:


d1 = pd.DataFrame({'team':d['team2'],'winner':d['winner']})  


# In[633]:


frames = [a1,b1,c1,d1]
total = pd.concat(frames)


# In[634]:


total


# In[635]:


total.index.unique()


# In[636]:


total.index.drop_duplicates(keep='first')


# In[637]:


total['team'].value_counts()


# In[638]:


total['winner'].value_counts()


# calculating the win probability manually = total wins/ total matches played

# In[639]:


win_probability_MI = 128/187

win_probability_MI 


# In[640]:


win_probability_KKR = 98/178

win_probability_KKR


# **Answer:** clearly MI has more probability of wining than kkr

# **how many 4 will be hit by kkr todays match?**

# In[641]:



run4k =deliveries.loc[(deliveries['batting_team'] == 'Kolkata Knight Riders') & (deliveries['bowling_team'] == 'Mumbai Indians')]

run4k


# In[642]:


run4k = run4k[run4k['batsman_runs']==4]


# In[643]:


Total_4_per_matchk = run4k.groupby('match_id')['batsman_runs'].count()


# In[644]:


RUN4k = pd.DataFrame({'total 4':Total_4_per_matchk})  


# In[645]:


RUN4k


# In[646]:


RUN4k['total 4'].value_counts()


# In[647]:


RUN4k.describe()


# analysing only kkr,s batting data

# In[648]:


runs4 =deliveries.loc[(deliveries['batting_team'] == 'Kolkata Knight Riders')]

runs4


# In[649]:


runs4= runs4[runs4['batsman_runs']==4]


# In[650]:


Total_4_bykkr = runs4.groupby('match_id')['batsman_runs'].count()


# In[651]:


RUNs4 = pd.DataFrame({'total 4':Total_4_bykkr})  


# In[652]:


RUNs4


# In[653]:


RUNs4['total 4'].value_counts()


# In[654]:


RUNs4.describe()


# **Answer:** based on above conclusion,  Average most scored 4s both individually and in against mi are around 13 , so from given options i conclude they might hit more than 13 4's in todays match

# **how will rohith sharma will be out?**

# analysing kxip vd rcb wickets data

# In[655]:



Rohith = deliveries.loc[(deliveries['batsman'] == 'R Sharma')]

Rohith


# In[656]:


outtyp = Rohith['dismissal_kind']


# In[657]:


outtyp


# In[658]:


outtyp.value_counts()


# **answer:** mostly he will be caught

# **Total runs in todays mtch will be?**

# In[659]:


MI_KKR =deliveries.loc[(deliveries['batting_team'] == 'Mumbai Indians') & (deliveries['bowling_team'] == 'Kolkata Knight Riders')]

MI_KKR


# In[660]:


Total_MI_KKR_runs_per_match = MI_KKR.groupby('match_id')['total_runs'].sum()


# In[661]:


Total_MI_KKR_runs_per_match


# In[662]:


KKR_MI =deliveries.loc[(deliveries['batting_team'] == 'Kolkata Knight Riders') & (deliveries['bowling_team'] == 'Mumbai Indians')]
KKR_MI


# In[663]:


Total_KKR_MI_runs_per_match = KKR_MI.groupby('match_id')['total_runs'].sum()


# In[664]:


Total_KKR_MI_runs_per_match


# In[665]:


KKRMI= pd.DataFrame({'Total runs':Total_KKR_MI_runs_per_match}) 


# In[666]:


MIKKR= pd.DataFrame({'Total runs':Total_MI_KKR_runs_per_match}) 


# In[667]:


frames = [ KKRMI, MIKKR]

MATCHruns = pd.concat(frames)


# In[668]:


MATCHruns 


# In[669]:


runs_per_match = MATCHruns.groupby('match_id')['Total runs'].sum()


# In[670]:


runs_per_match


# In[671]:


runs_match= pd.DataFrame({'Total runs':runs_per_match}) 


# In[672]:


runs_match


# In[673]:


runs_match['Total runs'].value_counts()


# In[674]:


runs_match.describe()


# In[675]:


plt.figure(figsize=(20,4))
ax = sns.countplot(x='Total runs',data=runs_match,order =runs_match['Total runs'].value_counts().index)


plt.title('visualization based on TOTAL runs scored in each match MI VS KKR')
plt.show()


# **answer:** by performing exploratory dataanalysis the mean is around 307, i conclude Todays total might be less than 320.

# **end of day 3**

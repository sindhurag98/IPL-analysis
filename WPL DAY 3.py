#!/usr/bin/env python
# coding: utf-8

# # srh vs csk

# **-by sindhura gundubogula**
# 
# **STEP-1 import all required python libraries**

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# **STEP-2 Load the dataset**

# In[2]:


deliveries = pd.read_csv("deliveries.csv")
matches    = pd.read_csv("matches.csv")


# In[3]:


deliveries.head()


# In[4]:


matches.head()


# In[5]:


deliveries.info()


# In[6]:


matches.info()


# **QUESTION1 : WHO WILL WIN THE MATCH?**

# **performing exploratory data analysis only on SRH VS CSK match data**

# In[7]:


sc = matches.loc[(matches['team1'] == 'Sunrisers Hyderabad') & (matches['team2'] == 'Chennai Super Kings')]
sc


# In[8]:


cs = matches.loc[(matches['team2'] == 'Sunrisers Hyderabad') & (matches['team1'] == 'Chennai Super Kings')]
cs


# In[9]:


SC= pd.DataFrame({'team1':sc['team1'],'team2':sc['team2'],'winner':sc['winner'],'win by runs':sc['win_by_runs'],'win by wickets':sc['win_by_wickets']})  


# In[10]:


CS= pd.DataFrame({'team1':cs['team1'],'team2':cs['team2'],'winner':cs['winner'],'win by runs':cs['win_by_runs'],'win by wickets':cs['win_by_wickets']})  


# In[11]:


frames = [SC,CS]

SRH_VS_CSK = pd.concat(frames)


# In[12]:


SRH_VS_CSK


# In[13]:


SRH_VS_CSK['winner'].value_counts()


# In[14]:


plt.figure(figsize=(8,4))
ax = sns.countplot(x='winner',data=SRH_VS_CSK, order = SRH_VS_CSK['winner'].value_counts().index)

plt.title('visualization based on number of wins SRH VS CSK')
plt.show()


# In[15]:


matches['winner'].value_counts()


# In[16]:


plt.figure(figsize=(8,4))
ax = sns.countplot(x='winner',data=matches, order = matches['winner'].value_counts().index)

ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
plt.tight_layout()
plt.title('visualization based on number of wins of SRH and CSK in all the matches')
plt.show()


# From the above visualizations we can observe that **CSK** has more wins compared to **SRK**

# **Answer:** So without over analyzing the senario, We can conclude that CSK can be a winner as it has more number of wins 

# **QUESTION 2 : HOW MANY WIDES WILL BE BOWLED?**

# Create a new dataframe with only SRH and CSK BOWLING related data

# In[17]:


SRH = deliveries.loc[(deliveries['bowling_team'] == 'Sunrisers Hyderabad')]
SRH


# In[18]:


CSK = deliveries.loc[(deliveries['bowling_team'] == 'Chennai Super Kings')]
CSK


# In[19]:


SRH = SRH.groupby('match_id')['wide_runs'].sum()

SRH


# In[20]:


CSK = CSK.groupby('match_id')['wide_runs'].sum()
CSK


# In[21]:


Total_wides_by_SRH = pd.DataFrame({'total wides per match':SRH}) 

Total_wides_by_SRH


# In[22]:


Total_wides_by_CSK = pd.DataFrame({'total wides per match':CSK}) 

Total_wides_by_CSK


# In[23]:


Total_wides_by_SRH['total wides per match'].value_counts()


# In[24]:


Total_wides_by_CSK['total wides per match'].value_counts()


# In[25]:


fig, axes = plt.subplots(1, 2,  sharex=True, figsize=(10,5))

ax1 = sns.countplot(ax=axes[0],x='total wides per match',data=Total_wides_by_SRH,order = Total_wides_by_SRH['total wides per match'].value_counts().index)
ax1.set_title('visualization based on wides in each match by SRH')
ax2 = sns.countplot(ax=axes[1],x='total wides per match',data=Total_wides_by_CSK,order = Total_wides_by_CSK['total wides per match'].value_counts().index)
ax2.set_title('visualization based on wides in each match by CSK')
plt.show()


# In[26]:


Total_wides_by_SRH.describe()


# In[27]:


Total_wides_by_CSK.describe()


# **answer:** using EDA, the means of SRK and CSK wides are around 4. So i conclude 4 or more wides might be bowled 

# **how many runs will david warner score?**

# In[28]:


warner = deliveries.loc[(deliveries['batsman'] == 'DA Warner')]

warner


# In[29]:


Total_runs_per_match = warner.groupby('match_id')['total_runs'].sum()


# In[30]:


Total_runs_per_match


# In[31]:


Total_runs_DAWarner = pd.DataFrame({'total runs per match':Total_runs_per_match}) 


# In[32]:


Total_runs_DAWarner 


# In[33]:


Total_runs_DAWarner['total runs per match'].value_counts()


# In[34]:


plt.figure(figsize=(20,4))
ax = sns.countplot(x='total runs per match',data=Total_runs_DAWarner,order = Total_runs_DAWarner['total runs per match'].value_counts().index)


plt.title('visualization based on runs score')
plt.show()


# In[35]:


Total_runs_DAWarner.describe()


# **Answer:** based on above conclusion,  Average most scored runs are around 40, so from given options i conclude he might score more than 40 runs in todays match

# **How many wickets will CSK loose?**

# In[ ]:





# **How many runs will be scored in todays match?**

# In[36]:


SRH_CSK =deliveries.loc[(deliveries['batting_team'] == 'Sunrisers Hyderabad') & (deliveries['bowling_team'] == 'Chennai Super Kings')]

SRH_CSK 


# In[37]:


Total_SRHCSK_runs_per_match = SRH_CSK .groupby('match_id')['total_runs'].sum()


# In[38]:


Total_SRHCSK_runs_per_match


# In[39]:


CSK_SRH =deliveries.loc[(deliveries['bowling_team'] == 'Sunrisers Hyderabad') & (deliveries['batting_team'] == 'Chennai Super Kings')]

CSK_SRH 


# In[40]:


Total_CSKSRH_runs_per_match = CSK_SRH .groupby('match_id')['total_runs'].sum()


# In[41]:


Total_CSKSRH_runs_per_match


# In[42]:


SRHCSK= pd.DataFrame({'Total runs':Total_SRHCSK_runs_per_match}) 


# In[43]:


CSKSRH= pd.DataFrame({'Total runs':Total_CSKSRH_runs_per_match}) 


# In[44]:


frames = [ SRHCSK,CSKSRH]

runs = pd.concat(frames)


# In[45]:


runs


# In[46]:


runs.index.unique()


# In[47]:


runs_per_match = runs.groupby('match_id')['Total runs'].sum()


# In[48]:


runs_per_match


# In[49]:


runs_match= pd.DataFrame({'Total runs':runs_per_match}) 


# In[50]:


runs_match


# In[51]:


runs_match.describe()


# In[52]:


runs_match['Total runs'].value_counts()


# In[53]:


plt.figure(figsize=(20,4))
ax = sns.countplot(x='Total runs',data=runs_match,order =runs_match['Total runs'].value_counts().index)


plt.title('visualization based on TOTAL runs scored in each match SRH VS CSK')
plt.show()


# **answer:** by performing exploratory dataanalysis the mean is around 345, i conclude Todays total might be 345 or higher.

# **end of day 3**

#!/usr/bin/env python
# coding: utf-8

# # JOB MARKET FOR DATA FIELD

# ### OBJECTIVE :
# 1. What roles are companies hiring the most -
# 2. what skills sets are needed
# 3. The state that offer the most opportunity

# In[1]:


import pandas as pd
import numpy as np
import math


# In[2]:


df=pd.read_csv('alldata.csv')
print(df.shape)
print(df.columns)


# In[3]:


df.head()


# In[4]:


df.isna().sum() # checking for nulls


# In[5]:


df=df.dropna()


# In[6]:


df.drop(columns=["reviews"]) #drop the column reviews


# In[7]:


df["position"].value_counts()


# ### LOCATIONS

# In[8]:


df["location"].value_counts()


# In[9]:


df[['state','code']] = df.location.str.split(',',expand=True)
df.head()


# **COMPANIES**

# In[10]:


total_no_company=df['company'].nunique()
print('total number of companies offerinf Data jobs:',total_no_company)


# THE COMPANIES WITH OPEN VACANCIES

# In[11]:


most_vacancy= df.groupby(['company'])['position'].count()
most_vacancy=most_vacancy.sort_values(ascending=False)
most_vacancy=most_vacancy.reset_index()
vacancy=most_vacancy.head(25)
vacancy


# # Building a dataframe for the qualification and tools required

# ### DATAFRAME 1 : Qualification

# In[12]:


qualifications = ['B.Sc', 'M.Sc','Bachelors','Masters','PhD']

counts= []
for qualification in qualifications:
    Q=len(df[df['description'].str.contains(qualification)])
    counts.append(Q)
print(counts)


# **Converting Into DataFrame**

# In[13]:


Q=pd.DataFrame(list(zip(qualifications, counts)),columns=['Qualification','Counts'])
Q #the df for the qualifications


# In[14]:


import matplotlib.pyplot as plot
Q.plot.bar(x="Qualification", y="Counts", rot=70, title="Qualification",edgecolor='black', color='green');


# ### DATAFRAME 2 : Tools

# ### FOR loop to get the count on the tools

# ### METHOD 1

# In[15]:


tools = ['Python','git','R','SQL','Tensor','Keras','Docker','Cloud','AWS','Tableau','Periscope','Sisense','Spark','kafta','Hive','Hadoop']

counts= []
for tool in tools:
    ctools=len(df[df['description'].str.contains(tool)])
    counts.append(ctools)
print(counts)


# In[16]:


T=pd.DataFrame(list(zip(tools, counts)),columns=['Tools','Counts'])
T.head() #the df for the tools used 


# In[17]:


import matplotlib.pyplot as plot
T.plot.bar(x="Tools", y="Counts", rot=70, title="Tools used",edgecolor='black', color='pink');


# ## DATA SCIENTIST

# In[18]:


df=df[df['position'].str.contains("Data Scientist")]
df.head()


# **COMPANIES**

# In[19]:


total_no_company=df['company'].nunique()
print('total number of companies offerinf Data jobs:',total_no_company)


# In[20]:


most_vacancy= df.groupby(['company'])['position'].count()
most_vacancy=most_vacancy.sort_values(ascending=False)
most_vacancy=most_vacancy.reset_index()
vacancy=most_vacancy.head(25)
vacancy


# **State offering positions for Data Scientist**

# In[21]:


S=df['state'].value_counts().loc[lambda x: x>5].reset_index()
S.head(5)


# In[22]:


import matplotlib.pyplot as plot
S.plot.bar(x="index", y="state", rot=70, title="Location",edgecolor='black', color='purple');


# **CONCLUSION**
# 
# Most of the Data Scientist roles are around New york , SFO and Chicago

# **QUALIFICATION**

# In[23]:


qualifications = ['B.Sc', 'M.Sc','Bachelors','Masters','PhD']

counts= []
for qualification in qualifications:
    Q=len(df[df['description'].str.contains(qualification)])
    counts.append(Q)
print(counts)


# In[24]:


Q=pd.DataFrame(list(zip(qualifications, counts)),columns=['Qualification','Counts'])
Q


# In[25]:


import matplotlib.pyplot as plot
Q.plot.bar(x="Qualification", y="Counts", rot=70, title="Qualification",edgecolor='black', color='green');


# **CONCLUSION** : The Role of Data Scientist requires  Phd
# 
#     
# |Qualification  | percentage |
# | -----------   | -----------|
# | PHD           | 74.9 %     |
# | Masters       | 20.53 %    |
# | Bacherlors    | 3.8 %      |
# | M.Sc          | 0.7 %      |
# | B.Sc          | 0 %        |

# **TOOLS**

# In[26]:


tools = ['Python','git','R','SQL','Tensor','Keras','Docker','Cloud','AWS','Tableau','Periscope','Sisense','Spark','kafta','Hive','Hadoop']

counts= []
for tool in tools:
    ctools=len(df[df['description'].str.contains(tool)])
    counts.append(ctools)
print(counts)


# In[27]:


T=pd.DataFrame(list(zip(tools, counts)),columns=['Tools','Counts'])
T.head()


# In[28]:


import matplotlib.pyplot as plot
T.plot.bar(x="Tools", y="Counts", rot=70, title="Tools used",edgecolor='black', color='pink');


# **CONCLUSION**
# 
# The Tool fairly required for Data Scientist is Python, R and Sql

# ### DATA ENGINEER

# In[29]:


df=df[df['position'].str.contains("Data Engineer")]
print(len(df))


# ### DATA ANALYST

# In[30]:


df=df[df['position'].str.contains("Data Analyst")]
print(len(df))


# In[ ]:






# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
                                'Budapest_PaRis', 'Brussels_londOn'],
                                'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
                                'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                                'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
                                '12. Air France', '"Swiss Air"']})


# In[3]:


df


# In[4]:


df.FlightNumber.fillna((df.FlightNumber.shift(1) + 10), inplace=True)


# In[5]:


df.FlightNumber = df.FlightNumber.astype(int)


# In[6]:


df


# In[7]:


df_temp = df.copy()


# In[8]:


df_temp['From'] = df_temp['From_To'].str.split('_')
df_temp['From'] = df_temp['From'].str[0]


# In[9]:


df_temp['To'] = df_temp['From_To'].str.split('_')
df_temp['To'] = df_temp['To'].str[1]


# In[10]:


df_temp.drop(columns=['From_To'])


# In[11]:


df_temp = df_temp[['Airline','FlightNumber','From','To','RecentDelays']]


# In[12]:


df_temp


# In[13]:



pd.options.mode.chained_assignment = None  # default='warn'
df_temp['From'] = df_temp['From'].str.capitalize()
df_temp['To'] = df_temp['To'].str.capitalize()


# In[14]:


df_temp


# In[15]:


df


# In[16]:


df.drop(columns='From_To', inplace=True)


# In[19]:


df = df.append(df_temp,ignore_index=True)
df.dropna(axis='rows',inplace=True)
df = df[['Airline','FlightNumber','From','To','RecentDelays']]
df


# In[20]:


colList = list()
for item in df['RecentDelays']:
    key = 0
    while(key < len(item)):
        key += 1        
        delay_col = 'delays_'+str(key)
        if delay_col not in colList:
            colList.append(delay_col)
colList


# In[21]:


df[colList] = pd.DataFrame(df['RecentDelays'].values.tolist(), index= df.index)


# In[22]:


df


# In[23]:


df.rename(index=str, columns={'RecentDelays':'delays'})


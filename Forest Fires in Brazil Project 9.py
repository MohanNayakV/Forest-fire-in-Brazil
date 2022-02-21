#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[10]:


data=pd.read_csv('C:\\Users\\Mohan\\Desktop\\Project CSV\\amazon.csv',encoding="iso-8859-1",parse_dates=['date'])


# In[8]:


data.dtypes


# In[13]:


#1. Display Top 5 Rows of The Dataset
data.head(15)


# In[14]:


#2. Check Last 5 Rows
data.tail(20)


# In[15]:


#3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
data.shape


# In[16]:


print("Number of Rows",data.shape[0])
print("Numbers of columns",data.shape[1])


# In[17]:


#4. Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
data.info()


# In[18]:


#5. Check For Duplicate Data and Drop Them
dup_data = data.duplicated().any()


# In[19]:


print("Are There Any Duplicated values in the data",dup_data)


# In[20]:


data.drop_duplicates()


# In[21]:


data = data.drop_duplicates()


# In[22]:


data.shape


# In[23]:


6454-6422


# In[24]:


#6. Check Null Values In The Dataset
data.isnull()


# In[25]:


data.isnull().sum()


# In[27]:


#7. Get Overall Statistics About The Dataframe
data.describe()


# In[30]:


data.describe(include='all')


# In[31]:


data.describe(include='all',datetime_is_numeric=True)


# In[32]:


#8. Rename Month Names To English
data.head()


# In[34]:


data['month_new']=data['month'].map({'Janeiro':'jan',
                                    'Fevereiro':'feb',
                                    'Março':'mar',
                                    'Abril':'apr',
                                    'Maio':'may',
                                    'Junho':'jun',
                                    'Julho':'jul',
                                    'Agosto':'aug',
                                    'Setembro':'sep',
                                    'Outubro':'oct',
                                    'Novembro':'nov',
                                    'Dezembro':'dec'
                                    })


# In[35]:


data.head()


# In[37]:


#9. Total Number of Fires Registered
data.shape


# In[38]:


#10. In Which Month Maximum Number of Forest Fires Were Reported?
data.columns


# In[40]:


data1 = data.groupby('month_new')['number'].sum()


# In[41]:


data1


# In[42]:


data1 = data.groupby('month_new')['number'].sum().reset_index()


# In[43]:


data1


# In[45]:


plt.figure(figsize=(18,6))
sns.barplot(x="month_new",y='number',data=data1)


# In[46]:


#11. In Which Year Maximum Number of Forest Fires Was Reported?
data2 = data.groupby('year')['number'].sum().reset_index()


# In[47]:


data2


# In[48]:


plt.figure(figsize=(15,5))
sns.barplot(x="year",y='number',data=data2)


# In[49]:


#12. In Which State Maximum Number of Forest Fires Was Reported?

data3 = data.groupby('state')['number'].sum().reset_index()


# In[50]:


data3


# In[56]:


plt.figure(figsize=(20,5))
sns.barplot(x="state",y='number',data=data3)
plt.xticks(rotation=75)
plt.show()


# In[57]:


#13. Find Total Number of Fires Were Reported In Amazonas
data.columns


# In[59]:


data['state']=="Amazonas"


# In[60]:


data[data['state']=="Amazonas"]


# In[61]:


data[data['state']=="Amazonas"]['number']


# In[62]:


data[data['state']=="Amazonas"]['number'].sum()


# In[63]:


#14. Display Number of Fires Were Reported In Amazonas (Year-Wise)
data.columns


# In[65]:


data[data['state']=="Amazonas"]


# In[66]:


data4 =data[data['state']=="Amazonas"]


# In[67]:


data4


# In[73]:


data5 = data4.groupby('year')['number'].sum().reset_index()


# In[72]:


data5


# In[75]:


plt.figure(figsize=(16,5))
sns.barplot(x="year",y="number",data=data5)


# In[76]:


#15. Display Number of Fires Were Reported In Amazonas (Day-Wise)
data.columns


# In[77]:


data6 = data[data['state']=="Amazonas"]


# In[83]:


day=data6.groupby(data6['date'].dt.dayofweek).sum().number

import calendar

day.index = [calendar.day_name[x] for x in range(0,7)]

day


# In[84]:


day = day.reset_index()


# In[85]:


day


# In[86]:


sns.barplot(x="index",y="number",data=day)


# In[88]:


plt.figure(figsize=(15,5))
sns.barplot(x="index",y="number",data=day)


# In[89]:


#16. Find Total Number of Fires  Were Reported In 2015 And Visualize Data Based on Each ‘Month’
data.columns


# In[90]:


data['year']==2015


# In[91]:


data[data['year']==2015]


# In[92]:


fire = data[data['year']==2015].groupby('month_new')['number'].sum()


# In[93]:


fire = data[data['year']==2015].groupby('month_new')['number'].sum().reset_index()


# In[94]:


fire


# In[95]:


sns.barplot(x="month_new",y="number",data=fire)


# In[98]:


plt.figure(figsize=(16,5))
sns.barplot(x="month_new",y="number",data=fire)


# In[99]:


# 17. Find Average Number of Fires Were Reported From Highest to Lowest (State-Wise)
data.columns


# In[100]:


data.groupby('state')['number'].mean().sort_values(ascending=False)


# In[103]:


data8 = data.groupby('state')['number'].mean().sort_values(ascending=False).reset_index()


# In[104]:


data8


# In[112]:


plt.figure(figsize=(16,5))
sns.barplot(x="state",y="number",data=data8)
plt.xticks(rotation=75)
plt.show()


# In[113]:


#18.  To Find The State Names Where Fires Were Reported In 'dec' Month
data.columns


# In[114]:


data['month_new']=="dec"


# In[117]:


data[data['month_new']=="dec"]['state'].unique()


# In[ ]:





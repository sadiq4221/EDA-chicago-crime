#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import os # accessing directory structure


# In[7]:


data = pd.read_csv('chicago.csv')


# In[8]:


data.head()


# In[4]:


data.info()


# In[47]:


primary_type = data['Primary Type'].value_counts()
print(primary_type)


# In[10]:


data.shape


# In[16]:


data["Primary Type"].value_counts().describe()


# In[45]:


order_df = data['Primary Type'].value_counts().iloc[:15].index
plt.figure(figsize = (15,10))
sns.countplot(y = 'Primary Type', data = data, order = order_df)



# In[24]:


data.value_counts("Location Description")


# In[12]:


duplicates = data[data.duplicated()]
print("Duplicated Values in the data set ", duplicates.shape[0])


# In[14]:


for col in data.dtypes.index:
    if data[col].dtype=='object':
        print('\n Total unique value in the colums {} is \n'.format(col),data[col])


# In[15]:


corr = data.corr()
fig,ax=plt.subplots(figsize=(10,6))
sns.heatmap(corr,annot=True,cmap='winter_r',fmt='.2f',
           square=True,
           linewidths=.5,ax=ax)
plt.title("Visualize the heatmap")
plt.show()


# In[24]:


# Get the value counts of each unique location description
location_counts = data['Location Description'].value_counts()
print(location_counts)


# In[29]:


plt.figure(figsize=(10, 40))  # Adjust the size as per your needs
sns.countplot(data=data, y="Location Description")
plt.show()


# In[38]:


order_loc = data['Location Description'].value_counts().iloc[:15].index


# In[41]:


plt.figure(figsize = (15,10))
sns.countplot(y = 'Location Description', data = data, order = order_loc)


# In[50]:


sns.histplot(data=data , x= 'Year', y = primary_type , bins=50 , prtresh=.1 , solor = 'red')
plt.show()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import os # accessing directory structure


# In[3]:


data = pd.read_csv('chicago.csv')


# In[4]:


data.head()


# In[4]:


data.info()


# In[19]:


columns = data[['Primary Type', 'Location Description', 'Arrest', 'Domestic', 'Year']]
columns.head()


# In[6]:


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


# In[17]:


plt.figure(figsize = (5,10))
sns.histplot(data=data, x='Year', y='Primary Type', bins=50, cbar=True, cmap='Reds', binwidth=0.5)
plt.show()




# In[4]:


data.isna().sum()


# In[4]:


data.fillna(0,inplace=True)
data.isna().sum()


# In[16]:


x = data['Primary Type'].astype(str)
y = data['Location Description'].astype(str)
plt.figure(figsize = (20,30))

plt.scatter(x, y)

plt.xlabel('Type')
plt.ylabel('Location')
plt.xticks(rotation='vertical')
plt.title('Scatter Plot')

plt.show()


# In[17]:


years = data['Year']
arrests = data['Arrest']

plt.hist(years, bins=10, edgecolor='black')

plt.xlabel('Year')
plt.ylabel('Arrest Count')
plt.title('Arrests by Year')

plt.show()


# In[5]:


years = data['Year']
domestic = data['Domestic']

plt.hist(years, bins=10, edgecolor='black')

plt.xlabel('Year')
plt.ylabel('domestic Count')
plt.title('Domestic count by Year')

plt.show()


# In[13]:


location_counts = data['Location Description'].value_counts()
location_labels = location_counts.index.astype(str)

plt.figure(figsize=(25, 9))

plt.bar(location_labels, location_counts)

plt.xlabel('Location Description')
plt.ylabel('Count')
plt.title('Bar Plot of Location Description')
plt.xticks(rotation='vertical')

plt.show()


# In[14]:


arrest_counts = data['Arrest'].value_counts()
plt.pie(arrest_counts, labels=arrest_counts.index, autopct='%1.1f%%')
plt.title('Pie Chart of Arrest')

plt.show()


# In[19]:


type_counts_by_year = data.groupby('Year')['Primary Type'].value_counts()

for crime_type in data['Primary Type'].unique():
    plt.plot(type_counts_by_year.loc[:, crime_type], label=crime_type)

plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Line Plot of Primary Type over Year')
plt.legend()

plt.show()


# In[ ]:





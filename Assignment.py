#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as nu
import pandas as pd
from geopy.geocoders import Nominatim
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data=pd.read_csv("E:/Python & R Project/new project/assignment_data.csv")
data


# In[3]:


data.head()


# In[4]:


data.columns


# In[5]:


data.info()


# In[6]:


data.describe()


# In[7]:


data.isnull().sum()


# In[8]:


data.corr()


# In[9]:


plt.figure(figsize=(14,8))
sns.heatmap(data.corr(),cmap='Spectral', annot = True)


# In[10]:


data.columns


# In[11]:


sns.pairplot(data,diag_kind='kde');


# In[12]:


from collections import Counter


# In[13]:


duplicate=data.duplicated()
print(duplicate)


# In[14]:


data1 = pd.DataFrame([duplicate])
print (data1)


# In[15]:


data1.describe()


# In[28]:


desc = data["name"].describe()
desc


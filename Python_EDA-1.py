#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib as plt


# In[2]:


# Function to read and transpose data
def read_and_transpose(filename):
    df = pd.read_csv(filename)
    df_years = df.set_index('country').T
    df_countries = df.set_index('year').T
    return df_years, df_countries

# Read and transpose data
df_years, df_countries = read_and_transpose('healthcare-dataset-stroke-data.csv')


# In[3]:


health.head()


# In[4]:


health.info()


# In[5]:


health.describe()


# In[6]:


health.drop('id', inplace=True, axis=1)


# In[7]:


health.head()


# In[8]:


health.head()


# In[9]:


health.info()


# In[10]:


health.isnull().sum()


# In[11]:


health['bmi'].mean()


# In[12]:


mean = health["bmi"].mean()

health['bmi'].replace(np.nan, mean ,inplace=True)


# In[13]:


health.isnull().sum()


# In[14]:


cat_features = health[["gender","ever_married","work_type","smoking_status","Residence_type"]]

numeric_features = health[["age","hypertension", "heart_disease", "avg_glucose_level", "bmi", "stroke"]]


numeric_features.head()

cat_features.head()


# In[15]:


numeric_features.hist(figsize=[10,10])


# In[16]:


sns.boxplot(x='stroke',y='avg_glucose_level',data=health)


# In[17]:


sns.boxplot(x='stroke',y='age',data=health)


# In[18]:


sns.boxplot(x='stroke',y='bmi',data=health)


# In[19]:


sns.boxplot(x='stroke',y='hypertension',data=health)


# In[20]:


sns.FacetGrid(health,hue="stroke",height = 5).map(sns.distplot,"age"). add_legend()


# In[21]:


sns.FacetGrid(health,hue="stroke",height = 5).map(sns.distplot,"bmi"). add_legend()


# In[22]:


counts = cat_features["gender"].value_counts()
percent100 = cat_features["gender"].value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
stroke_conditions=pd.DataFrame({'counts': counts, 'Percent': percent100})
print(stroke_conditions)


counts = cat_features["ever_married"].value_counts()
percent100 = cat_features["ever_married"].value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
stroke_conditions=pd.DataFrame({'counts': counts, 'Percent': percent100})
print(stroke_conditions)


counts = cat_features["work_type"].value_counts()
percent100 = cat_features["work_type"].value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
stroke_conditions=pd.DataFrame({'counts': counts, 'Percent': percent100})
print(stroke_conditions)


counts = cat_features["Residence_type"].value_counts()
percent100 = cat_features["Residence_type"].value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
stroke_conditions=pd.DataFrame({'counts': counts, 'Percent': percent100})

print(stroke_conditions)


# In[23]:


numeric_features = health[["age","gender","bmi"]]

sns.set_style("whitegrid")
sns.pairplot(numeric_features, hue = "gender", height = 5)


# In[24]:


smoke_vs_work_type = pd.crosstab(index=health["smoking_status"], columns=health["work_type"]) 
smoke_vs_work_type.plot(kind="bar", figsize=(8,8),stacked=True)


# In[25]:


sns.heatmap(health.corr(), annot = True,square=True)


# In[ ]:




#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import math
import io
import seaborn as sns


# In[2]:


df = pd.read_csv('https://pkgstore.datahub.io/machine-learning/cervical-cancer/cervical-cancer_csv/data/c43a91f09832cd9db8db84df08c942dc/cervical-cancer_csv.csv')


# In[3]:


df.head()


# In[4]:


df.columns


# In[5]:


df.tail


# In[6]:





# In[8]:


df.columns


# In[10]:


numerical_ds = ['Age', 'Number of sexual partners', 'First sexual intercourse','Num of pregnancies', 'Smokes (years)',
                'Smokes (packs/year)','Hormonal Contraceptives (years)','IUD (years)','STDs (number)']
categorical_ds = ['Smokes','Hormonal Contraceptives','IUD','STDs','STDs:condylomatosis','STDs:cervical condylomatosis',
                  'STDs:vaginal condylomatosis','STDs:vulvo-perineal condylomatosis', 'STDs:syphilis',
                  'STDs:pelvic inflammatory disease', 'STDs:genital herpes','STDs:molluscum contagiosum', 'STDs:AIDS', 
                  'STDs:HIV','STDs:Hepatitis B', 'STDs:HPV', 'STDs: Number of diagnosis','Dx:Cancer', 'Dx:CIN', 
                  'Dx:HPV', 'Dx', 'Hinselmann', 'Schiller','Citology', 'Biopsy']


# In[12]:


df = df.replace('?', np.NaN)
for feature in numerical_ds:
    print(feature,'',pd.to_numeric(df[feature]).median())
    feature_median = round(pd.to_numeric(df[feature]).median())
    df[feature]= df[feature].fillna(feature_median)


# In[13]:


for feature in categorical_ds:
    print(feature,'',pd.to_numeric(df[feature]).median())
    feature_median = round(pd.to_numeric(df[feature]).median())
    df[feature]= df[feature].fillna(feature_median)


# In[21]:


df = df.replace('?', np.NaN)


# In[22]:


df.head()


# In[14]:


df.drop('Hormonal Contraceptives',axis=1,inplace=True)


# In[15]:


df.shape


# In[18]:


df.plot()


# In[19]:


plt.plot()


# In[ ]:





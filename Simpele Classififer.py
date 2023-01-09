#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
from IPython.display import display
import random
from sklearn.metrics import recall_score, confusion_matrix, accuracy_score


# In[2]:


df_tags = pd.read_csv(f"/data/foodboost/tags.csv", index_col = 0) 
df_recipes = pd.read_csv(f"/data/foodboost/recipes.csv")
df_nutritions = pd.read_csv(f"/data/foodboost/nutritions.csv", index_col = 0)
df_ingredients = pd.read_csv(f"/data/foodboost/ingredients.csv", index_col = 0)


# In[3]:


df_ingredients


# In[4]:


list_of_ingredients = df_ingredients['ingredient'].unique().tolist()
list_of_recipes = df_ingredients['recipe'].unique().tolist()


# In[5]:


len(list_of_ingredients)


# In[6]:


Test = pd.DataFrame(0, list_of_recipes, list_of_ingredients)
for i in range(len(df_ingredients)):
    a = df_ingredients.iloc[i][1]
    b = df_ingredients.iloc[i][0]
    index_ingredient = list_of_ingredients.index(a)
    index_recipe = list_of_recipes.index(b)
    Test.iloc[index_recipe][index_ingredient] = 1


# In[7]:


Test


# In[8]:


y = Test['knoflook'].to_frame()


# In[9]:


y


# In[10]:


x = Test.drop('knoflook', axis = 1)


# In[11]:


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)


# In[12]:


y_train


# In[13]:


model = LogisticRegression()


# In[14]:


model.fit(X_train, y_train)


# In[15]:


y_pred = model.predict(X_test)


# In[16]:


y_pred


# In[17]:


recall_score(y_test, y_pred)


# In[18]:


confusion_matrix(y_true = y_test, y_pred = y_pred)


# In[19]:


accuracy_score(y_test, y_pred)


# In[20]:


#Er wordt nu in 80% van de gevallen door het model goed geschat of het voorspellende gerecht knoflook bevat.


# In[ ]:





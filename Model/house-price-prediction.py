#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


house_data = pd.read_csv('D:\\RESEARCH\\Dataset\\melbourne-housing-snapshot.csv')


# In[19]:


# Hiển thị toàn bộ bảng dữ liệu (không giới hạn số dòng, số cột)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print(house_data)


# In[4]:


print(house_data.columns)


# In[5]:


# Drop missing values

house_data = house_data.dropna(axis=0)


# In[12]:


y = house_data.Price


# In[8]:


house_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']


# In[ ]:


# X: Convention 
x = house_data[house_features]


# In[11]:


x.describe()


# In[14]:


from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
house_data_model = DecisionTreeRegressor(random_state=1)

house_data_model.fit(x,y)


# In[15]:


print("Making predictions for the following 5 houses:")
print(x.head())
print("The predictions are")
print(house_data_model.predict(x.head()))
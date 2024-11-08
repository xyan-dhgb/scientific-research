#!/usr/bin/env python
# coding: utf-8

import pandas as pd

house_data = pd.read_csv('D:\\RESEARCH\\Dataset\\melbourne-housing-snapshot.csv')

# Hiển thị toàn bộ bảng dữ liệu (không giới hạn số dòng, số cột)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print(house_data)

print(house_data.columns)

house_data = house_data.dropna(axis=0)

# Choose Target
y = house_data.Price 

# Choose features and assign to x
house_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
x = house_data[house_features]

x.describe()

from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
house_data_model = DecisionTreeRegressor(random_state=1)

house_data_model.fit(x,y)

print("Making predictions for the following 5 houses:")
print(x.head())
print("The predictions are")
print(house_data_model.predict(x.head()))

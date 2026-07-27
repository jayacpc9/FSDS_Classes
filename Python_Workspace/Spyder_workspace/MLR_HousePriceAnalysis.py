#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 20:12:30 2026

@author: chandra
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

assets_folder ="/Users/chandra/Desktop/FSDS_GenAI_Training/Spyder_workspace/assets/"
file_location = "House_data.csv"
full_file_path=assets_folder+file_location
print("File Path = ",full_file_path)

house_df = pd.read_csv(full_file_path)
print(house_df.head(10))

missing_value =house_df.isnull().any().sum()
print("Missing Values : ",missing_value)

print(house_df.columns)

# drop id and date since they are not important for this analysis

house_df = house_df.drop(["id","date"], axis =1)

print("After dropping id and date :\n",house_df.columns)

with sns.plotting_context("notebook", font_scale=2.5):
    g = sns.pairplot(house_df[['sqft_lot','sqft_above','price','sqft_living','bedrooms']], 
                 hue='bedrooms', palette='tab20',height=12)
    g.set(xticklabels=[]);
    
#x=house_df.iloc[:,1:]
#y=house_df.iloc[:,0]

x = house_df.iloc[:, 1:].values
y = house_df.iloc[:, 0].values

#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.33,random_state=0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# Predicting the Test set results
y_predict = regressor.predict(x_test)

m = regressor.coef_
print("m coef_ = ",m)

c = regressor.intercept_
print("C intercept_ = ",c)

# added a new column with the constant

no_of_items = len(x)
#print("no_of_items = ",no_of_items)
#print("len(x.columns) = ",len(x.columns))
X = np.append(arr=np.full((no_of_items,1),c).astype(int), values =x, axis=1)


import statsmodels.api as sm 
X_opt = X[:, [0, 1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17]] 

#OrdinaryLeastSquares
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()


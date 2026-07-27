#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 23:05:53 2026

@author: chandra
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

assets_folder ="/Users/chandra/Desktop/FSDS_GenAI_Training/Spyder_workspace/assets/"
file_location = "Investment.csv"
full_file_path=assets_folder+file_location
print("File Path = ",full_file_path)

investment_df = pd.read_csv(full_file_path)
print(investment_df.head(10))


missing_value =investment_df.isnull().sum()
print("Missing Values : ",missing_value)

X = investment_df.iloc[:,:-1]
y = investment_df.iloc[:,4]

#Convert categorical variable into dummy/indicator variables.

X = pd.get_dummies(X,dtype=int)

#Each variable is converted in as many 0/1 variables as there are different values. 
#Columns in the output are each named after a value; if the input is a DataFrame, 
#the name of the original variable is prepended to the value.

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2,random_state=0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)
y_pred = regressor.predict((X_test))

m = regressor.coef_
print("m coef_ = ",m)

c = regressor.intercept_
print("C intercept_ = ",c)

# added a new column with the constant

X = np.append(arr=np.full((50,1),42467).astype(int), values =X, axis=1)

import statsmodels.api as sm

X_opt =X[:,[0,1,2,3,4,5]]
# OrdinaryLeastSqure
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()


import statsmodels.api as sm
X_opt =X[:,[0,1,2,3,5]]
# OrdinaryLeastSqure
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()


import statsmodels.api as sm
X_opt =X[:,[0,1,2,3]]
# OrdinaryLeastSqure
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()



import statsmodels.api as sm
X_opt =X[:,[0,1,3]]
# OrdinaryLeastSqure
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()


import statsmodels.api as sm
X_opt =X[:,[0,1]]
# OrdinaryLeastSqure
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

bias = regressor.score(X_train,y_train)
print("bias = ",bias)

variance = regressor.score(X_test,y_test)
print("variance = ",variance)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 23:12:01 2026

@author: chandra
"""

# Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


assets_folder ="/Users/chandra/Desktop/FSDS_GenAI_Training/Spyder_workspace/assets/"
file_location = "emp_sal.csv"
full_file_path=assets_folder+file_location
print("File Path = ",full_file_path)

dataset = pd.read_csv(full_file_path)

X = dataset.iloc[:,1:2].values # experience at level
y = dataset.iloc[:,2].values # slary only


from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

plt.scatter(X, y,color ='red')
plt.plot(X, lin_reg.predict(X),color='blue')
plt.title("Linear Regression Graph")
plt.xlabel("Position Level")
plt.ylabel('Salary')
plt.show()


lin_model_pred = lin_reg.predict([[6.5]])
print("lin_model_pred = ",lin_model_pred)


from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=5)

X_poly=poly_reg.fit_transform(X)
poly_reg.fit(X_poly,y)
print("X_poly = ",X_poly)

lin_reg2= LinearRegression()
lin_reg2.fit(X_poly, y)


print(lin_reg)# linear regression with 1 degree poly
print(poly_reg) # polynomial regression wutg 2 degree
print(lin_reg2) # linear model with 2 degree


plt.scatter(X,y, color ='red')
plt.plot(X, lin_reg2.predict(poly_reg.fit_transform(X)), color='blue')
plt.title("Truth or Bluff (Polynomial Regression)")
plt.xlabel("Position Level")
plt.ylabel('Salary')
plt.show()


poly_model_predi = lin_reg2.predict(poly_reg.fit_transform([[6.5]]))
print("poly_model_predi = ",poly_model_predi)






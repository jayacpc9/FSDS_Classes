#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 23:06:41 2026

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

# polynomial
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


# Linear model predictions
print("lin_model_pred = ",lin_model_pred)
# poly model predictions

poly_model_predi = lin_reg2.predict(poly_reg.fit_transform([[6.5]]))
print("poly_model_predi = ",poly_model_predi)

# Support Vector Regression.
from sklearn.svm import SVR


svr_regressor = SVR(kernel='poly',degree=5,gamma='scale')
svr_regressor.fit(X,y)

svr_model_pred = svr_regressor.predict([[6.5]])
print("svr_model_pred = ",svr_model_pred)


#
# Loop to print all possibilities
#


kernal_list=[]
degree_list=[]
gama_list=[]
predicted_value_list=[]

print("Predicting for 6.5")

def print_all_possobilities(kernal, degree, gamma, predict_value=6.5):
    #print("print_all_possobilities : *********************")
    svr_regressor = SVR(kernel=kernal,degree=degree,gamma=gamma)
    svr_regressor.fit(X,y)

    svr_model_pred = svr_regressor.predict([[predict_value]])
    kernal_list.append(kernal)
    degree_list.append(degree)
    gama_list.append(gamma)
    predicted_value_list.append(svr_model_pred[0].round(2))
    
    #print(f" Kernal = {kernal}  Degree = {degree}  Gama = {gamma} svr_model_pred ={svr_model_pred}")
    #print("print_all_possobilities : svr_model_pred = ",svr_model_pred)

kernal =['linear', 'poly', 'rbf', 'sigmoid']
gamma =['scale', 'auto']
MAX_DEGREE = 6
degrees = range(1, MAX_DEGREE)

#for k in kernal:
#    for g in gamma:
#        for d in range(1, MAX_DEGREE):
#            print_all_possobilities(k,d,g)
#data_dict = {"Kernal":kernal_list,"Degree":degree_list,"Gamma":gama_list,"Predicted value":predicted_value_list}
#df = pd.DataFrame(data_dict)
#df


# optimized loop
import itertools

for k,g,d in itertools.product(kernal,gamma,degrees):
    print_all_possobilities(k,d,g)

data_dict22 = {"Kernal":kernal_list,"Degree":degree_list,"Gamma":gama_list,"Predicted_value":predicted_value_list}

df2 = pd.DataFrame(data_dict22)
df2['Predicted_value'] = df2['Predicted_value'].astype(float)
# print(df2)


#KNN Model


from sklearn.neighbors import KNeighborsRegressor
knn_reg = KNeighborsRegressor(n_neighbors=2, weights='distance', p=2, algorithm='auto')

knn_reg.fit(X, y)
predict_value=6.5
knn_reg_predict_value = knn_reg.predict([[predict_value]])
print("knn_reg_predict_value = ",knn_reg_predict_value)


# TREE Algorithm
#CART : CA - Classification RT - Regression
from sklearn.tree import DecisionTreeRegressor

dtr_reg = DecisionTreeRegressor() 
dtr_reg.fit(X, y)
dtr_reg_pred_value= dtr_reg.predict([[predict_value]])
print("dtr_reg_pred_value = ",dtr_reg_pred_value)


# RANDOM FOREST Agorithm

from sklearn.ensemble import RandomForestRegressor
#removing randome_state=0 will make it very random.
rf_reg = RandomForestRegressor(random_state=0, n_estimators=8)
rf_reg.fit(X, y)
rf_reg_predict_value=rf_reg.predict([[predict_value]])
print("rf_reg_predict_value = ",rf_reg_predict_value)









#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:30:00 2026

@author: chandra
"""

# Simple Linear Regression Algorithm 
# example of algorithm using the salary dataset.
# train a linear regression model using the historical data of salary.
# Predict the correct salary by using the x_test(years of experience data)
# Predict the salary of person with 12 years of exp, whose data was not part of the x_train data.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

assets_folder ="/Users/chandra/Desktop/FSDS_GenAI_Training/Spyder_workspace/assets/"
file_location = "Salary_Data.csv"
full_file_path=assets_folder+file_location
print("File Path = ",full_file_path)

salary_df = pd.read_csv(full_file_path)
print(salary_df.head(10))


missing_value =salary_df.isnull().sum()
print("Missing Values : ",missing_value)


x = salary_df.iloc[:,:-1]
y = salary_df.iloc[:,-1]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=0)



# How to train a model

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)


plt.scatter(x_test,y_test, color='red')
plt.plot(x_train,regressor.predict(x_train), color='blue')
plt.title("Salary vs Experience (Test set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")            
plt.show()



# to calculate the future salary , calcualte the coeffecient balue
# y^= mx+c
# calculate m and c and substiture the x as years of experience.

def predice_future_salary(years_of_experience = 12):
    m_coef = regressor.coef_
    print("Coefficient = ",m_coef)
    
    c_intercept = regressor.intercept_
    print("intercept = ", c_intercept)
    
    y_12 = m_coef * years_of_experience +c_intercept # y=mx+c
    
    print(f"Salary Prediction for {years_of_experience} years of experience = {y_12}")


predice_future_salary(10.5)
predice_future_salary(13)
predice_future_salary(20)

bias_score = regressor.score(x_train, y_train)
print("bias_score = ",bias_score)
variance_score = regressor.score(x_test, y_test)
print("variance_score = ",variance_score)


# Day 2 Cont..
# Statistics integration to ML model
print("*"*50)
print("salary_df.mean() = ",salary_df.mean())
salary_df['Salary'].mean()
salary_df['YearsExperience'].mean()
print("*"*50)

print("salary_df.median() = ",salary_df.median())
salary_df['Salary'].median()
salary_df['YearsExperience'].median()
print("*"*50)

print("salary_df.var() = ",salary_df.var())
salary_df['Salary'].var()
salary_df['YearsExperience'].var()
print("*"*50)


print("salary_df.std() = ",salary_df.std())
salary_df['Salary'].std()
salary_df['YearsExperience'].std()
print("*"*50)


from scipy.stats import variation

variation(salary_df.values)
variation(salary_df['Salary'])
variation(salary_df['YearsExperience'])


salary_df.corr() # this will give correlation of entire dataframe
salary_df['Salary'].corr(salary_df['YearsExperience']) # this will give us the correlation between these two attributes
salary_df['Salary'].corr(salary_df['Salary'])# will give correlation between salary.

salary_df.skew()# this will give skewness of entire dataframe
salary_df['Salary'].skew() # skewness of the given attribute


salary_df.sem() #this will provide the Standard error for the entire data frame
salary_df['Salary'].sem()
salary_df['YearsExperience'].sem()



import scipy.stats as stats

salary_df.apply(stats.zscore)



#ANOVA :  SSR,SSE, SST

y_mean =np.mean(y)
SSR = np.sum((y_pred - y_mean)**2)
print("SSR = ",SSR)

mean_total = np.mean(salary_df.values)
SST = np.sum((salary_df.values-mean_total)**2)
print("SST = ",SST)

y = y[0:6]
SSE=np.sum((y-y_pred)**2)
print("SSE = ",SSE)

r_square = 1-(SSE/SST)
print("r_square = ",r_square)
print("bias_score = ",bias_score)
print("variance_score = ",variance_score)



# Day 3 :  Cont...








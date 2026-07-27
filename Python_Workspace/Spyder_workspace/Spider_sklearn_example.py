#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 23:16:07 2026

@author: chandra
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

assets_folder ="/Users/chandra/Desktop/FSDS_GenAI_Training/Spyder_workspace/assets/"
file_location = "Data.csv"
full_file_path=assets_folder+file_location
print("File Path = ",full_file_path)
dataset = pd.read_csv(full_file_path )
print(dataset.head(10))

x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values


print(x)
print(y)

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan,strategy="median")
imputer = imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])


# converting all strings to variables.
from sklearn.preprocessing import LabelEncoder

# converting all city name to variables
labelendocer_x = LabelEncoder()
labelendocer_x.fit_transform(x[:,0])                              

x[:,0] = labelendocer_x.fit_transform(x[:,0])


#lable or onehot
labelencoder_y =LabelEncoder()
labelencoder_y.fit_transform(y)
y=labelencoder_y.fit_transform(y)



from sklearn.model_selection import train_test_split

x_train,x_test, y_train,y_test = train_test_split(x,y,train_size=0.7,test_size =0.3,random_state=0)










#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 23:02:04 2026

@author: chandra
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

folder_path =os.getcwd()+'/assets/'
file_name='Churn_Modelling.csv'
full_file_path = folder_path+file_name
print('Full File Path = ',full_file_path)


# Importing the dataset
dataset = pd.read_csv(full_file_path)
X = dataset.iloc[:, 3:-1].values
y = dataset.iloc[:, -1].values

print(X)
print(y)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X[:,2] = le.fit_transform(X[:,2])
print(X)


from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(),[1])],remainder='passthrough')

X = np.array(ct.fit_transform(X))


from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state=0)

from xgboost import XGBClassifier
classifier = XGBClassifier()

classifier.fit(X_train,y_train)
y_pred = classifier.predict( X_test)



##############################################################
#####                 Confusion MAetrics                 #####
##############################################################

# Using confusion matrix we can do the comparision
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

print("Confusion Matix = ",cm)

TN, FP, FN, TP = cm.ravel()
 
# Print them individually
print(f"True Positives  (TP): {TP}")
print(f"True Negatives  (TN): {TN}")
print(f"False Positives (FP): {FP}")
print(f"False Negatives (FN): {FN}")

##############################################################
# Confusion Matrix Display
##############################################################
#confusion MatrixDisplay
from sklearn.metrics import ConfusionMatrixDisplay

# Plot the matrix
ConfusionMatrixDisplay.from_estimator(classifier, X_test, y_test)
plt.show()


##############################################################
#####             check for model accuracy               #####
##############################################################

from sklearn.metrics import classification_report
cr = classification_report(y_test, y_pred)
print("Classification Report = ",cr)

print("Confusion Matix = ",cm)

from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test, y_pred)
print("Accuracy Score = ",ac)


bias = classifier.score(X_train, y_train)
print("Bias  = ",bias
      )
variance = classifier.score(X_test,y_test)
print("Variance = ",variance)




# Applying k-Fold Cross Validation

from sklearn.model_selection import cross_val_score
accuracies =  cross_val_score(estimator=classifier, X = X_train, y=y_train, cv =5)
print("accuracies = ",accuracies)
print("Accuracy: {:.2f} % ".format(accuracies.mean()*100))
print("Standard Deviation : {:.2f} % ".format(accuracies.std()*100))
















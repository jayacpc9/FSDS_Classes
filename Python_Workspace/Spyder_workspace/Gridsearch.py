#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 21:39:53 2026

@author: chandra
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

folder_path =os.getcwd()+'/assets/'
file_name='Social_Network_Ads.csv'

full_file_path = folder_path+file_name
print('Full File Path = ',full_file_path)

############################################################

dataset = pd.read_csv(full_file_path)

print("****" ,dataset.columns)

X = dataset.iloc[:, [2, 3]].values #get the Age and Salary
y = dataset.iloc[:, -1].values #get purchase status

############################################################

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train,y_test = train_test_split(X,y, test_size=0.2,random_state=0)


'''from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion='entropy', splitter='random',max_depth=5, random_state=0)
'''
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(max_depth=4, n_estimators=30, criterion='entropy', random_state=0)


classifier.fit(X_train,y_train)
y_pred = classifier.predict(X_test) # we got the y_predection using X_test, so it must match y_test


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






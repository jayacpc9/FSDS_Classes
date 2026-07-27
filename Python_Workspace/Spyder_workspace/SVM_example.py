#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 23:27:23 2026

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


############################################################

from sklearn.preprocessing import StandardScaler 
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
#we mentioned feature scaling only to independent variable not dependent variable at all

# Training the SVM model on the Training set
'''from sklearn.svm import SVC
classifier = SVC()
classifier.fit(X_train,y_train)'''

############################################################

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(X_train,y_train)

############################################################

#Next step is we are going to build the logistic model and appy this model into our dataset 
#This is linear model library thats why we called from sklear.linear_model
# Training the Logistic Regression model on the Training set

'''from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train,y_train)'''

y_pred = classifier.predict(X_test) # we got the y_predection using X_test, so it must match y_test


#now we compare X_test with y_pred, x-test we ha,ve age and salary , 
#if u look at the first observation this user is not be able to buy the car but if you look at observation 7 then that user is going to buy the car
#in this case logistic regression model classify the which users are going to buy the car or not 

#we build our logistic model and fit it to the training set & we predict our test set result 


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

from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test, y_pred)
print("Accuracy Score = ",ac)

from sklearn.metrics import classification_report
cr = classification_report(y_test, y_pred)
print("Classification Report = ",cr)

bias = classifier.score(X_train, y_train)
print("Bias  = ",bias
      )
variance = classifier.score(X_test,y_test)
print("Variance = ",variance)


##############################################################
#####                 Future Prediction                  #####
##############################################################

future_prediction_file_name='Futureprediction1.csv'
future_prediction_file_path = folder_path+ future_prediction_file_name
print('Future Prediction File Path = ',future_prediction_file_path)

fp_dataset = pd.read_csv(future_prediction_file_path)

dataset1 = fp_dataset.copy()
dataset1 = dataset1.iloc[:,[2,3]].values


from sklearn.preprocessing import StandardScaler 
sc1 = StandardScaler()
M = sc1.fit_transform(dataset1)
y_future_predict =classifier.predict(M)

##############################################################
# Write to the original csv.
# Add a new column y_pred1 and save the prediction data
##############################################################

fp_dataset['y_pred1'] = y_future_predict
fp_dataset.to_csv(future_prediction_file_path,index=False)



##############################################################
# ROC AUC
# ROC Curve
##############################################################

from sklearn.metrics import roc_auc_score, roc_curve
y_test_prob = classifier.predict_proba(X_test)[:,1] # using the salary

roc_auc_score = roc_auc_score(y_test,y_test_prob)

print("roc auc score = ",roc_auc_score)

fpr, tpr, thresholds = roc_curve(y_test, y_test_prob) # False Positive Rate and True Positive Rate

##############################################################
# Graph
##############################################################


plt.figure(figsize=(8,6))
plt.plot(fpr,tpr, label = f'Logistic Regression : AUC = {roc_auc_score:.2f}')
plt.plot([0,1], [0,1], 'k--')  # Random classifier line
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc='lower right')
plt.grid()
plt.show() 














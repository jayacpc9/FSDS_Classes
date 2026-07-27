#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 23:38:21 2026

@author: chandra
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

folder_path="/Users/chandra/Desktop/FSDS_GenAI_Training/Spyder_workspace/assets/"
file_name="logit classification.csv"

full_file_path = folder_path+file_name
dataset = pd.read_csv(full_file_path)

X = dataset.iloc[:,[2,3]].values
y = dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split

X_train,X_test,y_train, y_test = train_test_split(X,y,test_size=0.20,random_state=0)
 

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(penalty='l2',solver='newton-cg')
classifier.fit(X_train,y_train)
y_pred= classifier.predict(X_test)

score = classifier.score(X_test, y_test) # best way to check model accuracy
print("Score = ",score)


from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test,y_pred)
print("Confusion Matrix = ",cm)

TN, FP, FN, TP = cm.ravel()

# Print them individually
print(f"True Positives  (TP): {TP}")
print(f"True Negatives  (TN): {TN}")
print(f"False Positives (FP): {FP}")
print(f"False Negatives (FN): {FN}")

from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test, y_pred)
print("Accuracy Score = ",ac)

from sklearn.metrics import classification_report

cr = classification_report(y_test, y_pred)
print("Classification Report = ",cr)


bias = classifier.score(X_train,y_train)
print("Bias = ",bias)


variance = classifier.score(X_test, y_test)
print("Variance = ",variance)


import os
print("The current working directory  = ",os.getcwd())


# Future Prediction 
future_data_file_name="final1.csv"
future_prediction_full_file_path = folder_path+future_data_file_name
dataset1= pd.read_csv(future_prediction_full_file_path)

d2 = dataset1.copy()
dataset1 = dataset1.iloc[:,[3,4]].values
#dataset1 = dataset1[['Age','EstimatedSalary']]

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
M = sc.fit_transform(dataset1)
y_pred1 = pd.DataFrame()
d2['y_pred1'] = classifier.predict(M)

#update all the results to the file
d2.to_csv(future_prediction_full_file_path,index=False)
 
# End of Future Prediction

print("*" * 50)

 

# ROC AUC (area under curve)
from sklearn.metrics import roc_auc_score, roc_curve

y_pred_prob = classifier.predict_proba(X_test)[:,1]
auc_score = roc_auc_score(y_test,y_pred_prob)

print(auc_score)
fpr, tpr,thresholds = roc_curve(y_test,y_pred_prob)

plt.figure(figsize=(8,6))
plt.plot(fpr,tpr,label =f"Logistic Regresion AUC = {auc_score:.2f}")
plt.plot([0,1],[0,1],'k--')
plt.xlabel('False Positibe Rate')
plt.ylabel('True Posotive Rate')
plt.title('ROC Curve')
plt.legend(loc = 'lower right')
plt.grid()
plt.show()

# End of ROC AUC 



# loop to check the accuracy of model y_predict
# compare the y_pred data to y_test data
r = 0
for i in range(len(y_pred)):
    if y_pred[i] == y_test[i]:
        r += 1
   
print(f"Accuracy: {len(y_pred)} = {r} correct predictions, Accuracy = {r}%")

#confusion MatrixDisplay
from sklearn.metrics import ConfusionMatrixDisplay

# Plot the matrix
ConfusionMatrixDisplay.from_estimator(classifier, X_test, y_test)
plt.show()

print("*" * 50)
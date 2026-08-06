#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 22:51:56 2026

@author: chandra
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

folder_path =os.getcwd()+'/assets/'
file_name='Restaurant_Reviews.tsv'

full_file_path = folder_path+file_name
print('Full File Path = ',full_file_path)

dataset = pd.read_csv(full_file_path,delimiter='\t',quoting=3)

print("****" ,dataset.columns)
print("len(dataset) = ",len(dataset))

############################################################
dataset = pd.concat([dataset]*5, ignore_index=True)
length =len(dataset)
print("len(dataset) = ",length)


# Cleaning the text
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus=[]

for i in range(0,length):
    review = re.sub('[^a-zA-Z]',' ',dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in 
              set(stopwords.words('english'))]
    review= ' '.join(review)
    corpus.append(review)
    
    
# Creating the bag of words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(corpus).toarray() 
#y = dataset.iloc[:,1].values
y = dataset['Liked'].values

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf =TfidfVectorizer()
X_tfidf = tfidf.fit_transform(corpus).toarray()

# splitting the dataset in to the training set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, train_size=0.2, random_state=0)

from sklearn.ensemble import RandomForestClassifier
#rf_classifier = RandomForestClassifier(max_depth=6 , n_estimators=15, criterion='entropy' , random_state=10)
rf_classifier = RandomForestClassifier()
rf_classifier.fit(X_train,y_train)
y_pred = rf_classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

#print("Confusion Metrics : ",cm)
from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test, y_pred)

bias = rf_classifier.score(X_train, y_train)
variance = rf_classifier.score(X_test,y_test)

#print("Accuracy Score = ",ac)

'''



from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(max_depth=4,n_estimators=30, criterion="entropy", random_state=0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test, y_pred)
print(ac)


bias = classifier.score(X_train, y_train)
bias

variance = classifier.score(X_test, y_test)
variance


'''

print("Confusion Matix = ",cm)

print("Accuracy Score = ",ac)

print("Bias  = ",bias) 
print("Variance = ",variance)


  
'''from sklearn.feature_extraction.text import TfidfVectorizer
tfidf =TfidfVectorizer()
X_tfidf = tfidf.fit_transform(corpus).toarray()
'''



    
    
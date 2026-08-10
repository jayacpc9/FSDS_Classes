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
import all_classifiers
from com.ai.reviews.Constants import negative_stopwords_set

folder_path =os.getcwd()+'/assets/'
file_name='Restaurant_Reviews.tsv'

full_file_path = folder_path+file_name
print('Full File Path = ',full_file_path)

dataset = pd.read_csv(full_file_path,delimiter='\t',quoting=3)

print("****" ,dataset.columns)
print("Original : len(dataset) = ",len(dataset))

############################################################
COPY_TIMES = 5
dataset = pd.concat([dataset]*COPY_TIMES, ignore_index=True)
length =len(dataset)
print("After copying",COPY_TIMES,"times : len(dataset) = ",length)

# Cleaning the text
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus = []
results_list = []

# FIX: Do not strip out negative words that define low review scores!
custom_stopwords = set(stopwords.words('english'))
custom_stopwords = custom_stopwords - negative_stopwords_set # removing all negative stopwords from stopwords set.


for i in range(0, length):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in custom_stopwords]
    review = ' '.join(review)
    corpus.append(review)

# Creating the bag of words model

results_list = []
for vect_name,vect_tool in all_classifiers.vectorizers.items():
    X = vect_tool.fit_transform(corpus).toarray()
    y = y = dataset['Liked'].values

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.2, random_state=0)

    for model_name, model in all_classifiers.classifiers.items():
        print(f"--- Running Models using: {vect_name} --- {model_name}")
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        from sklearn.metrics import confusion_matrix
        cm = confusion_matrix(y_test, y_pred)
        # print("Confusion Metrics : ",cm)
        from sklearn.metrics import accuracy_score
        ac = accuracy_score(y_test, y_pred)
        bias = model.score(X_train, y_train)
        variance = model.score(X_test, y_test)

        # Determine Fit State
        score_gap = bias - variance
        if score_gap > 0.15:
            fit_status = "Overfitting (High Var)"
        elif bias < 0.70 and variance < 0.70:
            fit_status = "Underfitting (High Bias)"
        else:
            fit_status = "Balanced (Equal Scale)"

        # Store for tabular comparison
        results_list.append({
            "Vectorizer": vect_name,
            "Classifier": model_name,
            "Confusion Matix": cm,
            "Accuracy": round(ac, 4),
            "Train Score (Bias)": round(bias, 4),
            "Test Score (Variance)": round(variance, 4),
            "Fit Status": fit_status
        })

        # print("Confusion Matix = ", cm)
        # print("Accuracy Score = ", ac)
        # print("Bias  = ", bias)
        # print("Variance = ", variance)



result_df = pd.DataFrame(results_list)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(result_df)
print("\n\n")
from utils import Dispaly_Title_test as disp
disp.print_title("Accuracy > 90%",150)

print(result_df[result_df['Accuracy'] > 0.9])


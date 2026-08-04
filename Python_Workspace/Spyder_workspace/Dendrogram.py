#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 23:37:37 2026

@author: chandra
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

folder_path = os.getcwd()+'/assets/'
file_name='Mall_Customers.csv'

full_file_path = folder_path+file_name
print('Full File Path = ',full_file_path)

############################################################

dataset = pd.read_csv(full_file_path)

print("****" ,dataset.columns)

X = dataset.iloc[:, [3,4]].values # Annual income and Spending Score(1-100)

############################################################



import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X,method='ward'))
plt.title("Dendogram")
plt.xlabel('Customers')
plt.ylabel('Euclidean distance')
plt.show()


from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters=5, metric='euclidean',linkage='ward')
y_hc = hc.fit_predict(X)
print(y_hc)



plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(X[y_hc == 4, 0], X[y_hc == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

dataset['cluster'] = y_hc 


dataset.to_csv(folder_path+"Updated_Mall_Customer_hc.csv", index = False)

# Listing all customers who have a very high income and high sepending score
cluster_id = 2
dataset[dataset['cluster']==cluster_id]

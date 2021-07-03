# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 16:43:53 2021

@author: Payal
"""

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

StudentsPerformance= pd.read_csv('StudentsPerformance.csv')

X = StudentsPerformance[['math score', 'reading score']]
y = StudentsPerformance['writing score']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size= 0.3,random_state=101)

lm = LinearRegression()
lm.fit(X_train, y_train)

pickle.dump(lm, open('model.pkl', 'wb'))
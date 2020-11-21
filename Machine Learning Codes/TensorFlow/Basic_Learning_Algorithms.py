# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:31:00 2020

@author: Admin
"""


import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import sys
import sklearn as slk 
import tensorflow.compat.v2.feature_column as fc

#1.Linear Regression
dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv') # training data
dftest = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv') # testing data

y_train = dftrain.pop('survived')
y_test = dftest.pop('survived')

dftrain.age.hist(bins=20)

dftrain.sex.value_counts().plot(kind='barh')

dftrain['class'].value_counts().plot(kind='barh')

pd.concat([dftrain, y_train], axis=1).groupby('sex').survived.mean().plot(kind='barh').set_xlabel('% survive')


categorical = []
numerical = []
for i in dftrain.keys():
    if type(dftrain[i][0]) == str:
        categorical.append(i)
    else:
        numerical.append(i)

feature_cols= []        
for i in categorical:
    vocab = dftrain[i].unique()
    feature_cols.append(tf.feature_column.categorical_column_with_vocabulary_list(i, vocab))

for i in numerical:
    feature_cols.append(tf.feature_column.numeric_column(i, dtype=tf.float32))

print(feature_cols)

def make_input_fn(data_df, label_df, epochs=20, shuffle=True, batch_size=32):
    def input_function():
        df = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))
        if shuffle:
            df = df.shuffle(1000)
        df = df.batch(batch_size).repeat(epochs)
        return df
    return input_function

train_ip_fn = make_input_fn(dftrain, y_train)
eval_ip_fn = make_input_fn(dftest, y_test, epochs=1, shuffle=False)

linear_est = tf.estimator.LinearClassifier(feature_columns = feature_cols)

linear_est.train(train_ip_fn)

result = linear_est.evaluate(eval_ip_fn)

print(result)
print(result['accuracy'])    

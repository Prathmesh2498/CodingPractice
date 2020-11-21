# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 13:16:12 2020

@author: Admin
"""

import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import sys


#Creating a Tensor

number = tf.Variable(11, tf.int16)
st = tf.Variable("Abc", tf.string)
point = tf.Variable(7.5, tf.float64)

print("{} {} {}".format(number, st, point))

#Creating n-d tensors

rank1_tensor = tf.Variable([1,2,3], tf.int16)
rank2_tensor = tf.Variable([[1,2,3], [4,5,6]], tf.int16)

print(tf.rank(rank1_tensor))
print(tf.rank(rank2_tensor))

#Reshaping Tensors
rshaped_1 = tf.reshape(rank1_tensor, [1,3,1])
print(rshaped_1)

#Autoshape based on rows
#First len(rank2_tensor) % arg1 == 0
#Here arg1 = 2 and len(rank2_tensor) = 6
rauto = tf.reshape(rank2_tensor, [2,-1])
print(rauto)




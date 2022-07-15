# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 20:54:18 2022

@author: Nikhil
"""

""" importing libraries and datasets """

# importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# importing dataset
data = pd.read_csv('lalonde.csv')


""" Analysis """
without_training = data.query('treat==0')
with_training = data.query('treat==1')

sns.distplot(without_training, bins=20, kde=False, color="Blue", axlabel="re78")
sns.distplot(with_training, bins=20, kde=False, color="Red", axlabel="re78")

# from the graph, it seems that there the average salary without trainging is higher than average salary after training

# lets confirm this using the statistics

data.groupby('treat').aggregate({'re78':['mean','median']})

# statistics says the same thing as the values of mean and median is higher for the people without training

# lets check the balance of dataset among different parameters



sns.countplot(data=data, x="educ")
sns.countplot(data=data, x="married")
sns.distplot(data['age'], bins=10, kde=False)
sns.countplot(data=data, x="nodegree")
# as data is not balanced on these features, we cannot say that the mean and medians from the dataset is accurate and haveing a tranining program makes you less likely to make less money


data.columns







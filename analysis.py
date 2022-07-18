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
from causalgraphicalmodels import CausalGraphicalModel
import statsmodels.api as sm 
# importing dataset
data = pd.read_csv('lalonde.csv')
# deleting irrelevant columns
del data['Unnamed: 0']


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


# lets make the diagram using do why library
re78 = CausalGraphicalModel(
    nodes = ['treat','age','educ','black','hispan','married','nodegree','re78','race'],
    edges = [
            ('treat','re78'),
            ('age','treat'),
            ('age','re78'),
            ('educ','treat'),
            ('educ','re78'),
            ('married','treat'),
            ('married','re78'),
            ('nodegree','treat'),
            ('nodegree','re78'),
            ('black','race'),
            ('hispan','race'),
            ('race','treat'),
            ('race','re78')
        ]
    )

re78.draw()


data.columns



""" 
        Let's check if the variables are confounders or not 
        
        REGRESSION ANALYSIS    

"""

# Building the OLS on simple 
X = data[['treat']]
y = data[['re78']]

X = sm.add_constant(X)
mod = sm.OLS(y, X)
res = mod.fit()
res.summary()

# treat -> -635.0262 

# checking if age is potenitial confounder or not
X = data[['treat','age']]
y = data[['re78']]

X = sm.add_constant(X)
mod = sm.OLS(y, X)
res = mod.fit()
res.summary()

# treat -> -462.0603 

# checking if education is potential confounder or not
X = data[['treat','educ']]
y = data[['re78']]

X = sm.add_constant(X)
mod = sm.OLS(y, X)
res = mod.fit()
res.summary()

# treat -> -686.0253

# checking if education is potential confounder or not
X = data[['treat','married']]
y = data[['re78']]

X = sm.add_constant(X)
mod = sm.OLS(y, X)
res = mod.fit()
res.summary()

# treat -> 176.9906

# checking if education is potential confounder or not
X = data[['treat','nodegree']]
y = data[['re78']]

X = sm.add_constant(X)
mod = sm.OLS(y, X)
res = mod.fit()
res.summary()

# treat -> -394.1711


# checking if being black potential confounder or not
X = data[['treat','black']]
y = data[['re78']]

X = sm.add_constant(X)
mod = sm.OLS(y, X)
res = mod.fit()
res.summary()

# treat -> 857.1835

# checking if being hispanic potential confounder or not
X = data[['treat','hispan']]
y = data[['re78']]

X = sm.add_constant(X)
mod = sm.OLS(y, X)
res = mod.fit()
res.summary()

# treat -> -614.1596




















































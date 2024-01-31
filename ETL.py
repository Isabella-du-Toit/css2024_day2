# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 10:23:04 2024

@author: Isabella
"""

import pandas as pd

df = pd.read_csv("data_02/country_data_index.csv")

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None, names= column_names)
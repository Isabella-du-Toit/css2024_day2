# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 15:21:17 2024

@author: Isabella
"""

import pandas as pd

file = pd.read_csv("movie_dataset.csv")
print(file)

#remove nans or replace with average
revenue_avg = file["Revenue (Millions)"].mean()
file["Revenue (Millions)"].fillna(revenue_avg, inplace = True)
print(file)

metascore_avg = file["Metascore"].mean()
file["Metascore"].fillna(metascore_avg, inplace = True)
print(file)

print(file.info())#datatypes
print(file.describe())

#check visually for outliers and replace
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 10:40:33 2024

@author: Isabella
"""

#file locations
import pandas as pd

file = pd.read_csv("data_02/iris.csv")

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None, names= column_names)

#open txt file, seperator is ;
df = pd.read_csv("data_02/Geospatial Data.txt",sep=";")

#open excel file, using read_excel, can add sheet = "sheet1"
df = pd.read_excel("data_02/residentdoctors.xlsx")

#json file
df = pd.read_json("data_02/student_data.json")

url = "https://raw.githubusercontent.com/Asabele240701/css4_day02/main/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"

df = pd.read_csv(url)

print(df.info())
print(df.describe())

#remove index column
df = pd.read_csv("data_02/country_data_index.csv", index_col=0)

#add headings = column names
df = pd.read_csv("data_02/patient_data.csv")
column_names = ["duration", "pulse", "max_pulse", "calories"]

df = pd.read_csv("data_02/patient_data.csv", header=None, names=column_names)

#inconsistent data types and names
df = pd.read_excel("data_02/residentdoctors.xlsx")
print(df.info())
#datatype = objects - means datatypes are mixed

#fix, add column based on old column
#df["LOWER_AGE"] = df["AGEDIST"]
#now edit new column by  extracting lower range number
#df["LOWER_AGE"] = df["AGEDIST"].str.extract('(/d+)-')
#print(df.info())
#new column is still datatype = object, was extracted as string, convert to int
#df["LOWER_AGE"] = df["LOWER_AGE"].astype(int)
#print(df.info())

"""
looking at dates
30-01-2024 (UK standard)
01-30-2024 (US standard)
needs conversion
"""
df = pd.read_csv("data_02/time_series_data.csv", index_col=0)
print(df.info())
#convert date
df['Date'] = pd.to_datetime(df['Date'])
print(df.info())

df['Year'] = df['Date'].dt.year

"""
modify data
.dt - extract year and put in new column
.str
.extract
.astype
"""
#Nas and wrong format
#data frame contains empty values and outliers
df = pd.read_csv('data_02/patient_data_dates.csv')
print(df)

df.drop(index=26, inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
print(df.info())
print(df)

#remove nans or replace with average, fill in missing values withou scewing data
avg_cal = df["Calories"].mean()
df["Calories"].fillna(avg_cal, inplace = True)
#why inplace = True? All available nans
print(df)

#getting rid of nans
na = pd.read_csv('data_02/patient_data_dates.csv')
na.dropna(inplace = True)
print(na)
#rows containing nans were removed

#remove outlier - visually assessed
df.loc[7, 'Duration'] = 45
print(df) #replace specific value with loc

#data transformations
df = pd.read_csv("data_02/iris.csv")
#extract all column names
print(df.columns)#gives column names

col_names = df.columns.tolist()
print(col_names)

#add another column with squared lengths
df["sepal_length_sq"] = df["sepal_length"]**2
df["sepal_length_sq"] = df["sepal_length"].apply(lambda x: x**2)
print(df)

grouped = df.groupby("class")#calculate mean sepal length for each class
mean_square_values = grouped["sepal_length_sq"].mean()
print(mean_square_values)

#concat
df1 = pd.read_csv("data_02/person_split1.csv")
df2 = pd.read_csv("data_02/person_split2.csv")
df = pd.concat([df1,df2], ignore_index=True)
print(df)

#merge
df1 = pd.read_csv("data_02/person_education.csv")
df2 = pd.read_csv("data_02/person_work.csv")
df_merge_inner = pd.merge(df1,df2,on = "id")
print(df)

"""
clean data

1. Not filling in zeros - different to blank, a zero is actual data that was measured
2. Null Values - different to zero, null was not measured and thus should be ignored
3. Formatting to make data sheet pretty - highlighting and similar - add a new column instead with info
4. Comments in cells - place in separate column
5. Entering more than one piece of information in a cell - only one piece of information per cell
6. Using problematic field names - avoid spaces, numbers, and special characeters
7. Using special characters in data - avoid in your data

"""



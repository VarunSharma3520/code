import os
import pandas as pd

df = pd.read_csv('data.csv')

# print(type(df)) #<class 'pandas.core.frame.DataFrame'>
print(df.to_string()) 

# How to copy CSV data in Python 
# Shallow copy 
# Deep Copy

df.copy(deep = False) # deep copy if default

df.size #returns rows * column
df.index #returns list of rows in an object
df.shape # returns (rows , column)
df.memory_usage() #returns memory in bytes
df.ndim #returns arr dimension
df.head() #returns first 5 rows from dataframe
df.head(10) #returns first n rows from dataframe
df.tail() #returns last 5 rows from dataframe
df.tail(10) #returns last n rows from dataframe
df.at[4, 'total_rooms'] #seeks a value at df.at(index_value,column_name)
df.at[4, 'total_rooms'] = 10 # sets a value at df

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
df.shape # returns (column , rows)


import os
import pandas as pd

df = pd.read_csv('sample_data/california_housing_test.csv')
# df = pd.read_csv('sample_data/california_housing_test.csv',index_col=0)
# df = pd.read_csv('sample_data/california_housing_test.csv',na_values=['??','????'])

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
df.iat[4,3] #seeks a value at df.at(row_value,column_value)
df.iat[4,3] = 11 #sets a value at df.at(row_value,column_value)
df.loc[:,'total_rooms'] # gets a single table

# data Types in pandas 
# character: category, object
# numeric : int64, float64

df.dtypes # returns data types
df.dtypes.value_counts() # counts type of data types
df.select_dtypes(include=['float64']) # returns subset of selected datatypes.
df.info() # gives infomation about memory,total cloumn, rangeIndex, Dtype,non null datatype
np.unique(df['total_rooms']) # return unique dataTypes

#astypes is used convert datatype in python
'''

df.nbytes for getting storage of a column
df.replace([to_replace,value,inplace=True])
df.isnull.sum()


'''

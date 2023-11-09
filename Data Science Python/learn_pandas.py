import pandas as pd

# s1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9], index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']);print(s1)
# s2 = pd.Series({1:'a1',2:'b2'});print(s1)

#! slicing in pd
# print(s1[3])
# print(s1[::-1])
# print(s1)
# print(type(s1))

#! basic math operation
# print(s1+5)
# print(s1+s1)    #? Change the sign for other operation

#! creating Dataframes
# print(pd.DataFrame({'Name':['Bob', 'Sam', 'Anne'], 'Age':[17, 19, 20]}))

#! reading data
# df = pd.read_csv('sample_data/california_housing_test.csv')
# df = pd.read_csv('sample_data/california_housing_test.csv',index_col=0)
# df = pd.read_csv('sample_data/california_housing_test.csv',na_values=['??','????'])


# print(type(df)) #! <class 'pandas.core.frame.DataFrame'>
# print(df.to_string()) #! Render a DataFrame to a console-friendly tabular output 

#! How to copy CSV data in Python Document 
#1. Shallow copy 
#2. Deep Copy
# df.copy(deep = False) # deep copy if default

# df.size #! returns rows * column
# df.index #! returns list of rows in an object
# df.shape #! returns (rows , column)
# df.memory_usage() #! returns memory in bytes
# df.ndim #! returns arr dimension
# df.head() #! returns first 5 rows from dataframe
# df.head(10) #! returns first n rows from dataframe
# df.tail() #! returns last 5 rows from dataframe
# df.tail(10) #! returns last n rows from dataframe
# df.at[4, 'total_rooms'] #! seeks a value at df.at(index_value,column_name)
# df.at[4, 'total_rooms'] = 10 #! sets a value at df
# df.iat[4,3] #! seeks a value at df.at(row_value,column_value)
# df.iat[4,3] = 11 #! sets a value at df.at(row_value,column_value)
# df.loc[:,'total_rooms'] #! gets a portion of table table
# df['Name'].value_counts() #! return count of distinct values in a row
# df.sort_value(by = 'name') #! sort by name specified column


#! data Types in pandas 
# character: category, object
# numeric : int64, float64

# df.dtypes #! returns data types
# df.dtypes.value_counts() #! counts type of data types
# df.select_dtypes(include=['float64']) #! returns subset of selected datatypes.
# df.info() #! gives infomation about memory,total cloumn, rangeIndex, Dtype,non null datatype
# np.unique(df['total_rooms']) #! return unique dataTypes

#!astypes is used convert datatype

'''
df.nbytes for getting storage of a column
df.replace([to_replace,value,inplace=True])
df.isnull.sum()
'''

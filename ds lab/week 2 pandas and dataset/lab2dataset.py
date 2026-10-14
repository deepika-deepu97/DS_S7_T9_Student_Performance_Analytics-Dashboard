import pandas as pd
df=pd.read_csv('Iris.csv')
#print(df)
"""
#top rows 
print(df.head())
#only top n(eg 2 )rows
print(df.head(2))
#last rows
print(df.tail())
#last 3 rows
print(df.tail(3))

#details about dataset coloumns and their description
print(df.info())
"""
#no of rows and coloumns
print(df.shape)
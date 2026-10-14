import pandas as pd
data={'apples':[3,2,0,1],'oranges':[0,3,2,1]}
df=pd.DataFrame(data)
print(df)

df2 = pd.DataFrame(data, index=[1, 2, 3, 4])
print(df2)

df3 = pd.DataFrame(data, index=['first', 'second', 'third', 'fourth'])
print(df3)

 #access a particular location dataframe
print(df.loc[1])
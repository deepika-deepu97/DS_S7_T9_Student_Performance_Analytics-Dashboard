import pandas as pd
data=[1,2,3,10,20,30]
df=pd.DataFrame(data)
print(df)

data2={'Name':['AA','BB'],'Age':[30,45]}
df2=pd.DataFrame(data2)
print(df2)
"""
#to directly download dataframe to csv file
df.to_csv('abc.csv',index=True)
"""



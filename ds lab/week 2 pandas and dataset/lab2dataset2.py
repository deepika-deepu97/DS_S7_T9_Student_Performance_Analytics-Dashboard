import pandas as pd
df=pd.read_csv('Iris.csv')
#to print size rows and coloumns
print(df.shape)
#to duplicste all rows
dup_df = pd.concat([df, df], ignore_index=True)
print(dup_df.shape)
#to remove all duplicates
dup_df.drop_duplicates(inplace=True)
print(dup_df.shape)
#to print mean average mode etc
print(df.describe())
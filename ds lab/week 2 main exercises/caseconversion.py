import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'BOB', 'charle', 'DAVID']
})

df1 = df.copy()
df1['Name_lower'] = df1['Name'].str.lower()
print(df1)

df2 = df.copy()
df2['Name_upper'] = df2['Name'].str.upper()
print(df2)
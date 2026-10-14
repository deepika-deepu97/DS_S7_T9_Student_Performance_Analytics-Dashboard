import pandas as pd
import numpy as np
df=pd.DataFrame({'Age': [25,30,np.nan,40,35],'Department': ['HR','Finance','Finance',np.nan,'IT']})
print(df)
#mean for numeric
df['Age']=df['Age'].fillna(df['Age'].mean())

#mode for categorial
df['Department'] = df['Department'].fillna(df['Department'].mode()[0])

print("\nAfter Filling Missing Values:")
print(df)
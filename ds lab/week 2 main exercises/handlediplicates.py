import pandas as pd
import numpy as np
df = pd.DataFrame({
    'Id': [1,2,2,3,4,4],
    'Name': ['Nandini', 'Chetna', 'Chetna', 'deepika', 'Hasika','Hasika'],
    'Age': [25,30,30,35,40,40]
})
#print original dataset
print(df)
df_extract=df.drop_duplicates()
print(df_extract)
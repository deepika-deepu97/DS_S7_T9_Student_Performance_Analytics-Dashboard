import pandas as pd
import numpy as np
df = pd.DataFrame({
    'Id': [101, 102, 102, 103, 104, 105],
    'Name': ['Chetna', 'Deepika', 'Deepika', 'Hasika', 'Divya', 'Divya'],
    'Age': [20, 21, 21, 22, 23, 24]
})
#print original dataset
print(df)
#remove duplicates on id
df_subset_id=df.drop_duplicates(subset=['Id'])
print(df_subset_id)
#remove duplicaes on name
df_subset_name=df.drop_duplicates(subset=['Name'])
print(df_subset_name)
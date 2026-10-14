import pandas as pd
import numpy as np
df = pd.DataFrame({
    'Age': [25, 30, np.nan, 40, 35],
    'Department': ['HR', 'Finance', 'Finance', np.nan, 'IT']
})
# Display original dataset
print(df)

#both cols age and dept have both null values so both of the cols are removed
df_drop_cols=df.dropna(axis=1)
print(df_drop_cols)

#remives rows with null values
df_drop_cols1=df.dropna(axis=0)
print(df_drop_cols1)
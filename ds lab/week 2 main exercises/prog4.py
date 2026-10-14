import pandas as pd
import numpy as np
df = pd.DataFrame({
    'Age': [25, 30, np.nan, 40, 35],
    'Department': ['HR', 'Finance', 'Finance', np.nan, 'IT']
})
# Display original dataset
print(df)

#drop rows with missing values
df_drop_rows=df.dropna()
print(df_drop_rows)
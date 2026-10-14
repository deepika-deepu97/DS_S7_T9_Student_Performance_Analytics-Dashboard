import pandas as pd

data3 = {
    'row1': [3, 2, 1, 0],
    'row2': ['a', 'b', 'c', 'd']
}

df = pd.DataFrame.from_dict(
    data3,
    orient='index',
    columns=['A', 'B', 'C', 'D']
)

print(df)


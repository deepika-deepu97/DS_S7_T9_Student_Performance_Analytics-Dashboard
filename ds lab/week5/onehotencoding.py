import pandas as pd

# Example categorical data
df = pd.DataFrame({
    'color': ['red', 'blue', 'green', 'red']
})

print("Original data:")
print(df)

# One-hot encoding
one_hot = pd.get_dummies(df, columns=['color'])

print("\nOne-hot encoding:")
print(one_hot)
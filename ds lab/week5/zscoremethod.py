import pandas as pd
from sklearn.preprocessing import StandardScaler

# Sample dataset
data = pd.DataFrame({
    'A': [10, 20, 30, 40, 50],
    'B': [5, 15, 25, 35, 45]
})

print("Original data:")
print(data)

# Apply standardization
scaler = StandardScaler()
standardized_data = scaler.fit_transform(data)

# Convert back to DataFrame
standardized_df = pd.DataFrame(
    standardized_data,
    columns=data.columns
)

print("\nStandardized data (Z-score):")
print(standardized_df)
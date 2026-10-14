import pandas as pd
import seaborn as sns

# Load tips dataset
tips = sns.load_dataset("tips")

df = pd.DataFrame(tips)

print("First five rows:")
print(df.head())

# Select numerical columns
numeric_df = df.select_dtypes(include="number")

# Skewness
skewness_values = numeric_df.skew()

print("\nSkewness values:")
print(skewness_values)

# Kurtosis
kurtosis_values = numeric_df.kurt()

print("\nKurtosis values:")
print(kurtosis_values)
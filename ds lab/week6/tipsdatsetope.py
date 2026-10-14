import pandas as pd
import seaborn as sns

# Load tips dataset
tips = sns.load_dataset("tips")

# Convert to DataFrame
df = pd.DataFrame(tips)

print("First five rows:")
print(df.head())

# Select numerical columns
numeric_df = df.select_dtypes(include="number")

# Mean
mean_values = numeric_df.mean()
print("\nMean values:")
print(mean_values)

# Median
median_values = numeric_df.median()
print("\nMedian values:")
print(median_values)

# Mode
mode_values = numeric_df.mode().iloc[0]
print("\nMode values:")
print(mode_values)
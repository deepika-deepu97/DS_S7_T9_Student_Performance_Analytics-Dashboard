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

# Range
range_values = numeric_df.max() - numeric_df.min()

print("\nRange values:")
print(range_values)

# Variance
variance_values = numeric_df.var()

print("\nVariance values:")
print(variance_values)

# Standard deviation
std_values = numeric_df.std()

print("\nStandard deviation values:")
print(std_values)

# Interquartile Range (IQR)
Q1 = numeric_df.quantile(0.25)
Q3 = numeric_df.quantile(0.75)

IQR = Q3 - Q1

print("\nInterquartile Range (IQR):")
print(IQR)
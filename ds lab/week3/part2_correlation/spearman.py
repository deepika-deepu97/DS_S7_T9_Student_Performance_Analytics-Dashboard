import pandas as pd
from scipy.stats import spearmanr

# Spearman correlation for X and Y
df = pd.DataFrame({
    'X': [10, 20, 30, 40, 50],
    'Y': [12, 24, 33, 45, 60]
})

corr_value, p_value = spearmanr(df['X'], df['Y'])

print(f"Spearman Correlation Coefficient: {corr_value}")
print(f"P-Value: {p_value}")


# Spearman correlation matrix for subjects
df2 = pd.DataFrame({
    'TOC': [98, 76, 68, 77, 80],
    'QC': [72, 54, 33, 95, 50],
    'DS': [82, 49, 83, 87, 99]
})

corr_matrix = df2.corr(method='spearman')

print("Spearman Correlation Matrix for subjects:")
print(corr_matrix)
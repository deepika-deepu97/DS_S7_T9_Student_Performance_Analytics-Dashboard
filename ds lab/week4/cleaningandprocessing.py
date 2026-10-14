# Data cleaning and preprocessing
# Handle missing values
import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
# Fill missing values
df['age'].fillna(df['age'].median(), inplace=True)
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)
# Drop duplicates
df.drop_duplicates(inplace=True)
# Encode categorical variables
df = pd.get_dummies(
    df,
    columns=['sex', 'class', 'embarked'],
    drop_first=True
)
# Feature engineering: Family size
df['family_size'] = df['sibsp'] + df['parch']
print(df.head())
# Data cleaning and preprocessing
import pandas as pd
# Load dataset
df = pd.read_csv("student.csv")
print("Original shape:", df.shape)
# Fill missing numerical values with median
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Attendance'] = df['Attendance'].fillna(df['Attendance'].median())
df['Math_Score'] = df['Math_Score'].fillna(df['Math_Score'].median())
df['Science_Score'] = df['Science_Score'].fillna(df['Science_Score'].median())
# Fill missing email with mode
df['Email'] = df['Email'].fillna(df['Email'].mode()[0])
# Remove duplicate records
df.drop_duplicates(inplace=True)
# Remove unnecessary columns
df.drop(columns=['Student_ID', 'Name', 'Email'], inplace=True)
# Feature engineering: Average score
df['Average_Score'] = (
    df['Math_Score'] + df['Science_Score']
) / 2
# Create target variable
df['High_Performer'] = (
    (df['Average_Score'] >= 75) &
    (df['Attendance'] >= 75)
).astype(int)
# Encode categorical variables
df = pd.get_dummies(
    df,
    columns=['Gender', 'Department', 'City'],
    drop_first=True
)
print("Final shape:", df.shape)
print(df.head())
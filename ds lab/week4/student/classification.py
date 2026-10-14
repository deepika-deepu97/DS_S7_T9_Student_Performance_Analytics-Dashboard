# Student Performance Classification

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("student.csv")

# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Attendance'] = df['Attendance'].fillna(df['Attendance'].median())
df['Math_Score'] = df['Math_Score'].fillna(df['Math_Score'].median())
df['Science_Score'] = df['Science_Score'].fillna(df['Science_Score'].median())
df['Email'] = df['Email'].fillna(df['Email'].mode()[0])
# Remove duplicates
df.drop_duplicates(inplace=True)
# Remove unnecessary columns
df.drop(columns=['Student_ID', 'Name', 'Email'], inplace=True)
# Feature engineering
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
# Separate features and target
X = df.drop('High_Performer', axis=1)
y = df['High_Performer']
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
# Create model
model = LogisticRegression(max_iter=1000)
# Train model
model.fit(X_train, y_train)
# Make predictions
y_pred = model.predict(X_test)
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
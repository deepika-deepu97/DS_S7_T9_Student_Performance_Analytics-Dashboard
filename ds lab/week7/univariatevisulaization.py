import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Histogram
plt.figure(figsize=(6, 4))
sns.histplot(df['sepal length (cm)'], bins=20, kde=True)
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# Pie chart
species_counts = df['species'].value_counts().sort_index()

plt.figure(figsize=(6, 6))
plt.pie(
    species_counts,
    labels=iris.target_names,
    autopct='%1.1f%%'
)
plt.title("Species Distribution (Pie Chart)")
plt.show()
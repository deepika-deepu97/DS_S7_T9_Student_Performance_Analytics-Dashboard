import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

# --------------------------------
# BIVARIATE ANALYSIS
# --------------------------------

# 1. Scatter Plot
plt.figure(figsize=(6, 4))

sns.scatterplot(
    x=df['sepal length (cm)'],
    y=df['sepal width (cm)'],
    hue=df['species']
)

plt.title("Scatter Plot: Sepal Length vs Sepal Width")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.show()


# 2. Line Chart
plt.figure(figsize=(6, 4))

plt.plot(df['sepal length (cm)'])

plt.title("Line Chart of Sepal Length")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.show()


# 3. Bar Chart
plt.figure(figsize=(6, 4))

sns.barplot(
    x=df['species'],
    y=df['sepal length (cm)']
)

plt.title("Bar Chart: Mean Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Mean Sepal Length (cm)")

plt.xticks(
    [0, 1, 2],
    iris.target_names
)

plt.show()
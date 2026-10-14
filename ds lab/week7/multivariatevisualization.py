import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

#  HEATMAP
plt.figure(figsize=(8, 6))

sns.heatmap(
    df.iloc[:, :4].corr(),
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title("Correlation Heatmap of Iris Features")
plt.show()

# 2. BUBBLE CHART

plt.figure(figsize=(7, 5))

plt.scatter(
    df['sepal length (cm)'],
    df['sepal width (cm)'],
    s=df['petal length (cm)'] * 20,
    alpha=0.5,
    c=df['species'],
    cmap='viridis'
)

plt.title("Bubble Chart: Sepal Length vs Sepal Width")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")

plt.colorbar(label="Species")
plt.show()
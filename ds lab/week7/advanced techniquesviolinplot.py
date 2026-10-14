import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Violin Plot

plt.figure(figsize=(6, 4))

sns.violinplot(
    x=df['species'],
    y=df['sepal length (cm)']
)
plt.title("Violin Plot: Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")

plt.xticks(
    [0, 1, 2],
    iris.target_names
)

plt.show()
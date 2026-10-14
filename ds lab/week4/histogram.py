import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=sns.load_dataset("titanic")
#histogram of age

sns.histplot(df['age'],bins=20,kde=True)
plt.title("Age Distribution")
plt.show()


df=sns.load_dataset("tips")
sns.histplot(df['size'],bins=10,kde=True)
plt.title("Age Distribution")
plt.show()

df = pd.read_csv("student.csv")
sns.histplot(df['Attendance'],bins=10,kde=True)
plt.title("Attendance Distribution")
plt.show()
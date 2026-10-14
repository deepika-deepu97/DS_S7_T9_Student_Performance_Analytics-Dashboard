import pandas as pd
from sklearn.datasets import load_iris
from statistics import mode
#load iris dataset
iris=load_iris()
df=pd.DataFrame(iris.data,columns=iris.feature_names)
print("First five rows: ")
print(df.head())
#mean
mean_values=df.mean()
print("\nMean values:")
print(mean_values)
median_values=df.median()
print("\nMedian values:")
print(median_values)
#mode
mode_values=df.mode().iloc[0]
print("\nMode values:")
print(mode_values)
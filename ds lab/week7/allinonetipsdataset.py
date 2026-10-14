import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Tips dataset
df = sns.load_dataset("tips")

print(df.head())

# ==========================================
# 1. UNIVARIATE ANALYSIS
# ==========================================

# Histogram
plt.figure(figsize=(6, 4))

sns.histplot(
    df['total_bill'],
    bins=20,
    kde=True
)

plt.title("Distribution of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()


# Boxplot
plt.figure(figsize=(6, 4))

sns.boxplot(
    x=df['total_bill']
)

plt.title("Boxplot of Total Bill")
plt.xlabel("Total Bill")
plt.show()


# Pie Chart
day_counts = df['day'].value_counts()

plt.figure(figsize=(6, 6))

plt.pie(
    day_counts,
    labels=day_counts.index,
    autopct='%1.1f%%'
)

plt.title("Distribution of Customers by Day")
plt.show()


# ==========================================
# 2. BIVARIATE ANALYSIS
# ==========================================

# Scatter Plot
plt.figure(figsize=(6, 4))

sns.scatterplot(
    x=df['total_bill'],
    y=df['tip'],
    hue=df['sex']
)

plt.title("Scatter Plot: Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()


# Line Chart
plt.figure(figsize=(6, 4))

plt.plot(df['total_bill'])

plt.title("Line Chart of Total Bill")
plt.xlabel("Sample Index")
plt.ylabel("Total Bill")
plt.show()


# Bar Chart
plt.figure(figsize=(6, 4))

sns.barplot(
    x=df['day'],
    y=df['total_bill']
)

plt.title("Bar Chart: Mean Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Mean Total Bill")
plt.show()


# ==========================================
# 3. HEATMAP
# ==========================================

plt.figure(figsize=(8, 6))

sns.heatmap(
    df[['total_bill', 'tip', 'size']].corr(),
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title("Correlation Heatmap")
plt.show()


# ==========================================
# 4. BUBBLE CHART
# ==========================================

plt.figure(figsize=(7, 5))

plt.scatter(
    df['total_bill'],
    df['tip'],
    s=df['size'] * 50,
    alpha=0.5,
    c=df['size'],
    cmap='viridis'
)

plt.title("Bubble Chart: Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")

plt.colorbar(label="Party Size")

plt.show()


# ==========================================
# 5. VIOLIN PLOT
# ==========================================

plt.figure(figsize=(6, 4))

sns.violinplot(
    x=df['day'],
    y=df['total_bill']
)

plt.title("Violin Plot: Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")

plt.show()
import pandas as pd
df= pd.DataFrame({
    'TOC':[98,76,68,77,80],
    'QC':[72,54,33,95,50],
    'DS':[82,49,83,87,99]
})

corr_matrix=df.corr(method='pearson')
print("Pearson Correlation Matrix for subjects:\n",corr_matrix)


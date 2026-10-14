import pandas as pd
data = {
    'Roll No': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['chetna', 'Bhavya', 'Harika', 'Divya', 'Deepika',
             'Hasika', 'Tanvi', 'Hemanth', 'Arjun', 'Surya'],
    'Age': [19, 20, 19, 20, 19, 21, 20, 19, 20, 21],
    'Section': ['A', 'A', 'B', 'B', 'A', 'C', 'C', 'B', 'A', 'C'],
    'Data Science': [88, 91, 76, 95, 84, 73, 89, 67, 93, 81],
    'TOC': [82, 85, 80, 92, 78, 75, 91, 70, 89, 84],
    'QC': [79, 87, 74, 90, 81, 77, 88, 72, 94, 80]
}

df = pd.DataFrame(data)

print(df)
#to download the csv
df.to_csv('students.csv',index=True)

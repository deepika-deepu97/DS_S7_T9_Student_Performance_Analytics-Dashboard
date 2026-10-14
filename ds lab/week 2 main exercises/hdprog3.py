import pandas as pd
df=pd.DataFrame({
    'Data':['2025-91-05','03-03-2023','jan 4,2025','2025.01.05']
})
print("Original Data:\n",df)

#COVERT ALL DATES TO STANDARD ISO FORMAT (YYYY-MM-DD)
df['Data'] = pd.to_datetime(df['Data'], errors='coerce').dt.strftime('%Y-%m-%d')
print(df)
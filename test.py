import pandas as pd

# Muat dataset
df = pd.read_csv('amazon.csv')

# Tampilkan beberapa baris pertama dan info dasar
print(df.head())
print(df.info())
print(df.describe())

import pandas as pd

df = pd.read_excel(r'C:\Users\hp\Desktop\VS\Projet 2\Superstore.xlsx')

print("Shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())
print("\nStats:\n", df[['Sales', 'Profit', 'Quantity', 'Discount']].describe())

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Profit Margin'] = (df['Profit'] / df['Sales']) * 100

df.to_csv(r'C:\Users\hp\Desktop\VS\Projet 2\superstore_clean.csv', index=False)
print("\nClean file exported!")
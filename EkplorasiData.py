import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data dari file Excel
df = pd.read_excel('Handphone_Clear.xlsx')


# Menggambarkan distribusi jumlah terjual
plt.figure(figsize=(10, 6))
sns.histplot(df['Sold'], bins=30, kde=True)
plt.title('Distribusi Penjualan Handphone di Tokopedia (Kuartal 2 2024)')
plt.xlabel('Jumlah Terjual')
plt.ylabel('Frekuensi')
plt.show()


# Tren Penjualan Berdasarkan Harga
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Price', y='Sold')
plt.title('Tren Penjualan Berdasarkan Harga')
plt.xlabel('Harga')
plt.ylabel('Jumlah Terjual')
plt.show()


#Penjualan Berdasarkan Wilayah
plt.figure(figsize=(12, 8))
sns.countplot(data=df, y='Location', order=df['Location'].value_counts().index)
plt.title('Penjualan Handphone Berdasarkan Wilayah')
plt.xlabel('Jumlah Terjual')
plt.ylabel('Wilayah')
plt.show()


#Rating Produk dan Jumlah Penjualan
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Rating', y='Sold')
plt.title('Jumlah Penjualan Berdasarkan Rating Produk')
plt.xlabel('Rating')
plt.ylabel('Jumlah Terjual')
plt.show()


#Produk Terlaris
top_products = df.groupby('Name')['Sold'].sum().nlargest(10)

plt.figure(figsize=(12, 8))
sns.barplot(x=top_products.values, y=top_products.index)
plt.title('Produk Handphone Terlaris di Tokopedia (Kuartal 2 2024)')
plt.xlabel('Jumlah Terjual')
plt.ylabel('Nama Produk')
plt.show()

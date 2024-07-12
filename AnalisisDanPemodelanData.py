import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import math

df = pd.read_excel('Handphone_Clear.xlsx')

#Analisis Menggunakan Statistika Deskriptif--------------------------------------------------------
#Rata-Rata-----------------------------------------------------------------------------------------
mean_jumlah_terjual = df['Sold'].mean()
mean_harga = df['Price'].mean()
mean_rating = df['Rating'].mean()
print("Rata-rata jumlah terjual:", math.floor(mean_jumlah_terjual))
print("Rata-rata harga         :", math.floor(mean_harga))
print("Rata-rata rating        :", math.floor(mean_rating))

#Median---------------------------------------------------------------------------------------
median_jumlah_terjual = df['Sold'].median()
median_harga = df['Price'].median()
median_rating = df['Rating'].median()
print("Median jumlah terjual   :", math.floor(median_jumlah_terjual))
print("Median harga            :", math.floor(median_harga))
print("Median rating           :", math.floor(median_rating))

#Standar Deviasi------------------------------------------------------------------------------
StandarDeviasi_jumlah_terjual = df['Sold'].std()
StandarDeviasi_harga = df['Price'].std()
StandarDeviasi_rating = df['Rating'].std()
print("Standar Deviasi jumlah terjual :", math.floor(StandarDeviasi_jumlah_terjual))
print("Standar Deviasi harga          :", math.floor(StandarDeviasi_harga))
print("Standar Deviasi rating         :", math.floor(StandarDeviasi_rating))

#Varians------------------------------------------------------------------------------
Varians_jumlah_terjual = df['Sold'].var()
Varians_harga = df['Price'].var()
Varians_rating = df['Rating'].var()
print("Varians jumlah terjual:", math.floor(Varians_jumlah_terjual))
print("Varians harga         :", math.floor(Varians_harga))
print("Varians rating        :", math.floor(Varians_rating))

#Nilai Minimum-----------------------------------------------------------------------
min_jumlah_terjual = df['Sold'].min()
min_harga = df['Price'].min()
min_rating = df['Rating'].min()
print("Minimum Jumlah Terjual:", math.floor(min_jumlah_terjual))
print("Minimum Harga:", math.floor(min_harga))
print("Minimum Rating:", math.floor(min_rating))

#Nilai Maksimum-----------------------------------------------------------------------
max_jumlah_terjual = df['Sold'].max()
max_harga = df['Price'].max()
max_rating = df['Rating'].max()
print("Maksimum Jumlah Terjual:", math.floor(max_jumlah_terjual))
print("Maksimum Harga:", math.floor(max_harga))
print("Maksimum Rating:", math.floor(max_rating))

#Rentang Nilai--------------------------------------------------------------------
print("Range Jumlah Terjual:", math.floor(max_jumlah_terjual - min_jumlah_terjual))
print("Range Harga:", math.floor(max_harga - min_harga))
print("Range Rating:", math.floor(max_rating - min_rating))


#Pemodelan Data----------------------------------------------------------------------------------
#Analisis Regresi Linear----------------------------------------------------------------------------
# Memilih fitur dan target
X = df[['Price']]
y = df['Sold']

# Membagi data menjadi training dan testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat model regresi linier
model = LinearRegression()
model.fit(X_train, y_train)

# Memprediksi pada testing set
y_pred = model.predict(X_test)

# Menghitung metrik evaluasi
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# Plotting the regression line
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted')
plt.title('Regresi Linier Sederhana: Harga vs Jumlah Terjual')
plt.xlabel('Harga')
plt.ylabel('Jumlah Terjual')
plt.legend()
plt.show()



# Analisis MultiLinear Regression------------------------------------------------------------------
# Memilih fitur dan target
X = df[['Price', 'Rating']]
y = df['Sold']

# Membagi data menjadi training dan testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat model regresi linier berganda
model = LinearRegression()
model.fit(X_train, y_train)

# Memprediksi pada testing set
y_pred = model.predict(X_test)

# Menghitung metrik evaluasi
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# Visualisasi hasil regresi
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
plt.title('Regresi Linier Berganda: Prediksi vs Aktual')
plt.xlabel('Jumlah Terjual Aktual')
plt.ylabel('Jumlah Terjual Prediksi')
plt.show()



#Analisis Klasifikasi Menggunakan Decision Tree----------------------------------------------------
# Mengubah jumlah terjual menjadi kategori
df['Kategori'] = pd.qcut(df['Sold'], q=3, labels=['Rendah', 'Sedang', 'Tinggi'])

# Memilih fitur dan target
X = df[['Price', 'Rating']]
y = df['Kategori']

# Membagi data menjadi training dan testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat model decision tree
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Memprediksi pada testing set
y_pred = model.predict(X_test)

# Menghitung metrik evaluasi
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
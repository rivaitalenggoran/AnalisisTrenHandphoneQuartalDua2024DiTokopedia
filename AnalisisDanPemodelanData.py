import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier

df = pd.read_excel('Handphone_Clear.xlsx')

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
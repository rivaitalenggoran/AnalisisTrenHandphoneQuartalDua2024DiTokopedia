import pandas as pd
import os

# Tentukan folder yang berisi file-file CSV
folder_path = 'C:\MyFile\Project\AnalisisTrenHandphoneQ12024DiTokopedia'

# Buat list untuk menyimpan semua DataFrame
data_frames = []

# Loop melalui semua file di folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        # Baca setiap file CSV ke dalam DataFrame
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_csv(file_path)
        # Tambahkan DataFrame ke dalam list
        data_frames.append(df)

# Gabungkan semua DataFrame menjadi satu
combined_df = pd.concat(data_frames, ignore_index=True)

# Simpan DataFrame yang sudah digabungkan ke file CSV baru
combined_df.to_csv('C:\MyFile\Project\AnalisisTrenHandphoneQ12024DiTokopedia\dataGabung.csv', index=False)

print("Data berhasil digabungkan dan disimpan!")

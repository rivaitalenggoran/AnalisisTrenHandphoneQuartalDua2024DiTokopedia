# Analisis Tren Penjualan Handphone Di Tokopedia pada Kuartal 2 2024

# Rivai Hayashi Hendrik Talenggoran

## 1. Pendahuluan
- **Tujuan:** Menganalisa Tren Penjualan Handphone di Tokopedia pada Kuartal Kedua 2024.
- **Latar Belakang:** Handphone menjadi kebutuhan yang penting di zaman yang semakin berkembang. Membangun bisnis penjualan Handphone menjadi salah satu opsi yang menguntungkan,
     mengingat Handphone yang setiap tahunnya terus berkembang dan penjualan yang semakin meningkat menjadikan hal hal tersebut sebagai dasar mengapa bisnis handphone menjadi menarik.
     namun sebelum memulai bisnis, baiknya kita melihat menganalisa penjualanan handphone yang ada di platform E-commerce yang besar seperti Tokopedia. dengan menganalisa penjualan handphone
     beserta tren penjualan handphone dari tokopedia, kita bisa dengan mudah mengambil keputusan dalam memulai bisnis handphone, ataupun mengambil keputusan handphone apa yang layak kita beli 
     berdasarkan hasil analisis tren penjualan handphone di tokopedia. dari projek ini, kita bisa melakukan beberapa analisis dari projek ini untuk menunjang keputusan kita, baik dalam memulai bisnis
     ataupun dalam membeli handphone untuk kebutuhan

## 2. Sumber Data
- **Deskripsi Sumber Data:**
  - **Tokopedia**
  

- **Struktur Data:**
  - **Tipe data:**  `String`, `Float`, `List`
  - **Data yang dikumpulkan:** `nama_produk`, `jumlah_terjual`, `harga`, `wilayah`, `rating`.
  

- **Metode Pengumpulan Data:** 
   - **Data diambil melalui metode Scrapping**
   - **Fitur Scrapping Data terdapat pada file** `TokpedScrapper.py`
   - **Data yang dikumpulkan berjenis Data** `Kualitatif` dan `Kuantitatif`
   - **Kualitatif mencakup** `nama_produk` dan `wilayah`
   - **Kuantitatif mencakup** `jumlah_terjual`, `harga`, dan `rating`
  
## 3. Pra-Processing Data
- **Proses Pembersihan Data:**
  - **Fitur Proses Pembersihan Data terdapat pada file** `PraProcessing.py`
  - **Penanganan Missing Values** : Baris dengan nilai kosong dihapus
  - **Penanganan Duplikasi**      : Penanganan Duplikasi: Baris duplikat dihapus
  - **Penanganan Outlier**        : Baris dengan nilai variabel yang tidak normal dihapus


- **Pra-Pemrosesan Data:**
  - **Fitur Pra-Pemrosesan Data terdapat pada file** `PraProcessing.py`
  - **Normalisasi dan Standarisasi:** Data dinormalisasikan agar seragam
  - **Transformasi Data           :** Transformasi data sesuai kebutuhan

  
## 4. Eksplorasi Data
- **Fitur Eksplorasi Data terdapat pada file `EksplorasiData.py`**
- **Distribusi Penjualan Handphone      :** Menunjukkan sebaran jumlah penjualan yang terjadi selama kuartal kedua 2024
- **Tren Penjualan Berdasarkan Harga    :** Menunjukkan bagaimana harga mempengaruhi jumlah penjualan
- **Penjualan Berdasarkan Wilayah       :** Menunjukkan wilayah dengan penjualan tertinggi
- **Rating Produk dan Jumlah Penjualan  :** Menunjukkan hubungan antara rating produk dan jumlah penjualan
- **Produk Terlaris                     :** Menunjukkan produk yang paling banyak terjual selama periode tersebut

## 5. Analisis dan Pemodelan Data
- **Fitur Eksplorasi Data terdapat pada file `AnalisisDanPemodelanData.py`**
- **Fitur Eksplorasi Data untuk Microsoft Excel terdapat pada file `EksplorasiDanAnalisisExcel.xlsx`**
- **Analisis Regresi            :** Digunakan untuk memprediksi jumlah penjualan berdasarkan harga dan rating
  - **Analisis Regresi sederana :** Memprediksi jumlah penjualan berdasarkan harga
  - **Regresi Linier Berganda   :** Memprediksi jumlah penjualan berdasarkan harga dan rating
- **Analisis Klasifikasi        :** Digunakan untuk mengelompokkan produk berdasarkan performa penjualannya
  - **Klasifikasi Dengan Decision Tree :** Mengklasifikasikan produk berdasarkan harga dan rating

## 6. Kesimpulan dan Rekomendasi
**Dari hasil eksplorasi dan analisis data, berikut merupakan hasil kesimpulan dan rekomendasi sementara:**

- **Kesimpulan**
  - **Distribusi Penjualan    :** Sebagian besar penjualan handphone berada dalam kisaran 
                                  100 - 1500 yang menunjukkan tren penjualan handphone dengan 
                                  jumlah terjual yang cukup signifikan.
  - **Pengaruh Harga Terhadap Penjualan :** Terdapat hubungan negatif antara harga dan jumlah penjualan, 
                                            di mana handphone dengan harga lebih rendah cenderung terjual 
                                            lebih banyak. Ini menunjukkan bahwa harga adalah faktor penting 
                                            yang mempengaruhi keputusan pembelian konsumen.
  - **Wilayah Dengan Penjualan Tertinggi:** Penjualan handphone tertinggi terjadi di 
                                            Jakarta dan sekitarnya seperti tangerang,medan, yang menunjukkan adanya 
                                            pasar potensial di daerah-daerah tersebut. 
                                            Wilayah-wilayah dengan penjualan tertinggi ini 
                                            bisa menjadi target pemasaran yang lebih intensif.

  - **Pengaruh Rating Produk Terhadap Penjualan:** Rating produk juga mempengaruhi jumlah penjualan. 
                                                   Produk dengan rating lebih tinggi cenderung terjual 
                                                   lebih banyak, menunjukkan bahwa kualitas dan kepuasan 
                                                   pelanggan memainkan peran penting dalam meningkatkan penjualan.
  - **Produk Terlaris:** Iphone sebagai produk 
                        terlaris dengan jumlah penjualan yang sangat tinggi. Disusul dengan Samsung
                        diurutan kedua dan xiaomi diurutan yang ketiga.
                        Ini menunjukkan preferensi konsumen terhadap merek dan model tertentu.
- **Rekomendasi**
  - **Strategi Penetapan Harga     :** Menyesuaikan harga handphone di harga Rp.1-2 Juta dengan daya beli konsumen dapat
                                       meningkatkan volume penjualan. Diskon atau promosi khusus dapat
                                       digunakan untuk menarik lebih banyak pembeli.
  - **Fokus pada Wilayah Potensial :** Memperkuat strategi pemasaran di wilayah Jakarta atau sekitarnya dengan penjualan tertinggi dapat meningkatkan 
                                       penjualan secara keseluruhan. Kampanye pemasaran yang disesuaikan dengan karakteristik 
                                       demografis wilayah tersebut dapat lebih efektif.
  - **Meningkatkan Kualitas Produk :** Memastikan kualitas produk dan meningkatkan rating melalui layanan pelanggan yang baik dapat membantu meningkatkan penjualan. 
                                       Pelanggan yang puas cenderung memberikan rating tinggi dan merekomendasikan produk kepada orang lain
  - **Optimalisasi Produk Terlaris :** Meningkatkan stok dan variasi produk terlaris seperti Iphone dan Samsung dapat memenuhi permintaan yang tinggi dan mencegah kekurangan stok. 
                                       Produk-produk ini dapat dipromosikan lebih lanjut untuk meningkatkan penjualan
  - **Pemantauan Berkelanjutan     :** Melakukan pemantauan dan analisis penjualan secara berkala untuk mengidentifikasi tren baru dan perubahan dalam preferensi konsumen. 
                                       Data yang diperbarui secara teratur dapat membantu dalam membuat keputusan bisnis yang lebih baik.


## 7. Penutup
Analisis ini memberikan wawasan penting mengenai tren penjualan handphone di Tokopedia 
pada kuartal kedua 2024. Dengan memanfaatkan data dan analisis ini, bisnis dapat membuat 
keputusan yang lebih tepat dalam hal penetapan harga, pemasaran, dan manajemen produk untuk 
meningkatkan penjualan dan kepuasan pelanggan. Analisis lebih lanjut dan pemantauan berkelanjutan 
akan memastikan bahwa strategi tetap relevan dan efektif di pasar yang dinamis.
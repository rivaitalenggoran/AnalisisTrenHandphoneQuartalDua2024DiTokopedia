import pandas as pd
import re


dataframe = pd.read_csv('DataGabung.csv')

### PROSES PEMBERSIHAN DATA(duplikat,missing value)

#hapus duplikat
dfduplicate = dataframe.drop_duplicates()

#hapus data yang punya variabel null
dfnull = dfduplicate.dropna()


# Filter untuk hanya menyertakan baris dengan nama produk tertentu
filter_produk = dfnull['product_name'].str.contains('iphone|vivo|samsung|oppo|xiaomi|realme', case=False, na=False)


#Normalisasi data dan olah data
newdataframe = dfnull[filter_produk]


#olah data
Sell = newdataframe['sell']
Price = newdataframe['price']
Rating = newdataframe['rating']

#olah data kualitatif ke lowercase
Name = newdataframe['product_name'].str.lower()
Location = newdataframe['location'].str.lower()
Category = newdataframe['kategori'].str.lower()



#buat list untuk data baru
dataPrice = []
dataPriceoutlier=[]
dataSold = []
dataName = []
dataSeries = []
dataRamAndRom=[]
dataRating = []
dataLocation = []
dataCategory = []


########## Normalisasi   ##########
#hapus titik pada harga
for rows in Price:
    row_num = rows[2:]
    price = re.sub(r'\.', '', row_num)
    dataPrice.append(price)
print("jumlah harga",len(dataPrice))


#ubah format "rb,+,terjual"
for rows2 in Sell:
    row_num2 = rows2[:3]
    rb = re.sub(r'rb', '000', row_num2)
    rb1 = re.sub(r'\+', '', rb)
    sell = re.sub(r'r', '000', rb1)
    sell1 = re.sub(r't', '', sell)
    dataSold.append(sell1)
print("jumlah terjual",len(dataSold))


#filter data hanya untuk 6 kategori handphone
for rows3 in Name:
    name_product = re.findall('iphone|vivo|samsung|oppo|xiaomi|realme',rows3)
    dataName.append(name_product[0])
print("jumlah nama",len(dataName))


#masukkan rating
for rows4 in Rating:
    dataRating.append(rows4)
print("jumlah rating",len(dataRating))


#masukkan lokasi
for rows5 in Location:
    dataLocation.append(rows5)
print("jumlah lokasi",len(dataLocation))

#masukkan kategori
for rows6 in Category:
    dataCategory.append(rows6)
print("jumlah kategori",len(dataCategory))


new_dataframe = pd.DataFrame(dataName, columns=['Name'])
new_dataframe['Price'] = dataPrice
new_dataframe['Sold'] = dataSold
new_dataframe['Rating'] = dataRating
new_dataframe['Category'] = dataCategory
new_dataframe['Location'] = dataLocation
print(new_dataframe)

new_dataframe2 = pd.DataFrame(new_dataframe, columns=['Name','Price', 'Sold', 'Rating', 'Category', 'Location'])
new_dataframe2.to_excel('Data_Gabung_Clear.xlsx')
print('Done!')

































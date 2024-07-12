import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
inputan = input("silahkan masukkan data yang ingin dicari di tokopedia : ")
url = "https://www.tokopedia.com/search?st=&q="+inputan+"&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource="
driver = webdriver.Chrome()
driver.get(url)

data=[]

for i in range(1):
 WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#zeus-root')))
 time.sleep(5)
 for j in range(15):
  driver.execute_script("window.scrollBy(0,250)")
  time.sleep(2)
 soup = BeautifulSoup(driver.page_source, 'html.parser')
 driver.execute_script("window.scrollBy(50,0)")
 time.sleep(2)

 #ambil nama produk dan harga
 for item in soup.findAll('div',class_="css-5wh65g"):

  #nama
  name_element = item.find('span',class_="OWkG6oHwAppMn1hIBsC3pQ==")
  if name_element:
   product_name = name_element.text
   print("Nama Produk:", product_name)
  else:
   print("Elemen tidak ditemukan")

  #harga
  price_element= item.find('div',class_="_8cR53N0JqdRc+mQCckhS0g== Phc0SDQ0Yjt43vf3XuwYOg==")
  if price_element:
   price = price_element.text
   print("Harga Produk:", price)
  else:
   print("Elemen tidak ditemukan")

   # rata rata rating
  rating_element = item.find('span', class_="nBBbPk9MrELbIUbobepKbQ==")
  try:
    rating = rating_element.text
    print("Rating Produk:", rating)
  except:
    rating = None

  #terjual
  sell_element = item.find('span', class_="eLOomHl6J3IWAcdRU8M08A==")
  try:
    sell = sell_element.text
    print("Terjual:", sell)
  except:
    sell = None

  #wilayah
  location_element = item.find('span', class_="-9tiTbQgmU1vCjykywQqvA== flip")
  try:
    location = location_element.text
    print("Terjual:", location)
  except:
    location = None

  data.append((product_name, price, rating,sell,location))





df = pd.DataFrame(data, columns=['product_name','price','rating','sell','location'])
df['kategori'] = inputan
df.to_csv('Tokped_'+inputan+'.csv',index=False)
df = pd.read_csv('Tokped_'+inputan+'.csv')
df.to_csv('Tokped_'+inputan+'.csv',index=False)
print("data "+inputan+" berhasil disimpan")

driver.close()

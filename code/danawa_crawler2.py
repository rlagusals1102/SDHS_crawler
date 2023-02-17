import requests
from bs4 import BeautifulSoup
import time

query = "RTX 3080"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
url = "https://search.danawa.com/dsearch.php?query="+query

html = requests.get(url,headers=headers).text
soup = BeautifulSoup(html,"html.parser")
productList = soup.select(".prod_name")
print(soup)
for product in productList:
    try:
        print(product.text.strip())
    #name = product.select_one(".prod_name").text
    #print(name)
    except  e:
        print(e)

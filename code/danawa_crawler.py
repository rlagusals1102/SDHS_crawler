import requests
from bs4 import BeautifulSoup
import time

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
url = "https://prod.danawa.com/list/?cate=112782&shortcutKeyword=%ED%82%A4%EB%B3%B4%EB%93%9C"

html = requests.get(url,headers=headers).text
soup = BeautifulSoup(html,"html.parser")
productList = soup.select(".product_list")
product = productList[1].select(".prod_item")
for index in range(30) :
    link = product[index].select_one(".prod_name")\
        .find("a")
    print(link.text.strip())
    res = requests.get(link["href"],headers=headers).text
    soup2 = BeautifulSoup(res,"html.parser")
    price = soup2.select_one(".prc_c").text
    print(price)
    time.sleep(0.5)


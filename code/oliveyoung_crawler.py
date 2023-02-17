import requests
from bs4 import BeautifulSoup

COUNT = 10
# 스킨케어
CATNO1 = "10000010001"
# 클렌징
CATNO2 = "10000010010"
# 남성용
CATNO3 = "10000010007"

url = "https://www.oliveyoung.co.kr/store" \
      "/main/getBestList.do" \
      "?dispCatNo=900000100100001&fltDispCatNo=" + CATNO3
response = requests.get(url)
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    productList = soup.select(".prd_info")
    for i in range(COUNT):
        print(productList[i].select_one(".tx_name").text)
        print(productList[i].find("img")["src"])
        print(productList[i].select_one(".tx_cur").text)
        link = productList[i].find("a")["href"]
        result = requests.get(link).text
        soup2 = BeautifulSoup(result,"html.parser")
        rank = soup2.select_one("#repReview")
        print(rank.find("b").text.strip(),
              rank.find("em").text.strip())

else:
    print("에러발생")

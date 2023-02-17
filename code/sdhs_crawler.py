import requests
# pip install requests
from bs4 import BeautifulSoup
# pip install beautifulsoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

url = "https://www.kw.ac.kr/ko/life/facility11.jsp#zoom-out"

html = requests.get(url,headers=headers).text
soup = BeautifulSoup(html,"html.parser")

data = soup.select(".al")
for i in data:
    print(i.text)

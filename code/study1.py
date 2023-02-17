import requests
from bs4 import BeautifulSoup

# pip install beautifulsoup4
# https://jsonplaceholder.typicode.com/users/1

resource = requests.get("http://www.sdh.hs.kr/")
html = resource.text
soup = BeautifulSoup(html,"html.parser")
#soup.find("a","img-box")
images = soup.find_all("a","img-box")
for i in images:
    if i.find(attrs={"alt": "ko-text"}):
        print(i["href"])



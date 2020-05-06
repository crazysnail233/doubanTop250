import requests
from bs4 import BeautifulSoup

url = "http://www.santostang.com"
headers = {"user-agent":"Mozilla/5.0"}
r = requests.get(url,headers = headers)
r.raise_for_status = r.apparent_encoding

soup = BeautifulSoup(r.text,'lxml')
title = soup.find("h1",class_="post-title").a.text.strip()
print(title)

with open('title.txt',"a+") as f:
    f.write(title)
    f.close()
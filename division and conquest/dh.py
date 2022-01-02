import requests
from bs4 import BeautifulSoup

url='https://www.samsung.com/sec/smartphones/all-smartphones/?galaxy-z'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

req=requests.get(url,headers=headers)

soup=BeautifulSoup(req.text,'html.parser')

print(soup)
# for temps in soup.find_all():
#     print('--->',temps.get_text())
# print('\n')
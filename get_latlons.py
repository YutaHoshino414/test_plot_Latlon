import requests
from bs4 import BeautifulSoup
from time import sleep
from urllib.parse import urljoin
from rich import print
import re

url = 'https://www.keiostore.co.jp/business/store_list.html'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
target_list = soup.find_all('table', class_='storeList')
td_list = [td.find_all('td', class_='storeName') for td in target_list]

address_list = []
for target in td_list:
    for i, t in enumerate(target[:15]):
        a = t.find('a')['href']
        url = urljoin(url, a)
        print(i)
        print(url)
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')
        name = soup.find('h2').text
        target_list = soup.find('div', class_='storeOutline').table.select('tr')
        for tr in target_list:
            if tr.find_all('th', text='住所'):
                address = tr.find('th', text='住所').next_sibling.next_sibling.text.split('\u3000')[1]
        #print(address)
        print(name, repr(address),  '-------', sep="\n")
        address_list.append(address)
        sleep(1)
print(f'_/_/_/住所リスト_/_/_/：\n{address_list}')

url = 'http://www.geocoding.jp/api/'
latlon_list = []
for address in address_list:
    sleep(10)
    print(address)
    payload = {"v": 1.1, 'q': address}
    res = requests.get(url, params=payload)
    soup = BeautifulSoup(res.content,'html.parser')
    lat = soup.find('lat').text
    lon = soup.find('lng').text
    print(lat, lon)
    latlon_list.append([lat, lon])

print(f'_/_/_/緯度経度リスト_/_/_/：\n{latlon_list}')
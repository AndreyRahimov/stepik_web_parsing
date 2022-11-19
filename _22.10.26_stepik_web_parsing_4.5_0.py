from bs4 import BeautifulSoup
import requests

response = requests.get('https://parsinger.ru/html/index3_page_1.html').text
soup = BeautifulSoup(response, 'lxml')
tags = soup.find(class_='pagen').find_all('a')
FIRST_PART_OF_LINK = 'https://parsinger.ru/html/'
links = [FIRST_PART_OF_LINK + tag['href'] for tag in tags]
res = []
for link in links:
    response = requests.get(link)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    tags = soup.find_all(class_='name_item')
    goods = [tag.text for tag in tags]
    res.append(goods)

print(res)

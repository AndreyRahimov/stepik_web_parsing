'''Выберите 1 любую категорию на сайте тренажере и соберите все данные с карточек'''

import json
from bs4 import BeautifulSoup
import requests

start_response = requests.get('https://parsinger.ru/html/index3_page_1.html')
start_response.encoding = 'utf-8'
start_soup = BeautifulSoup(start_response.text, features='lxml')
pages = start_soup.find(class_='pagen')
URL_START = 'https://parsinger.ru/html/'
page_links = [URL_START + link['href'] for link in pages.find_all('a')]

names, description, prices = [], [], []
for page_link in page_links:
    page_link_response = requests.get(page_link)
    page_link_response.encoding = 'utf-8'
    page_link_soup = BeautifulSoup(page_link_response.text, features='lxml')
    names.extend(name.text.strip()
                 for name
                 in page_link_soup.find_all(class_='name_item'))
    description.extend(feature.text.strip().split('\n')
                       for feature
                       in page_link_soup.find_all(class_='description'))
    prices.extend(price.text.strip()
                  for price
                  in page_link_soup.find_all(class_='price'))

mouses = []
for name, features, price in zip(names, description, prices):
    mouse = {
        'Название': name,
        'Бренд': features[0].split(': ', 1)[1].strip(),
        'Тип': features[1].split(': ', 1)[1].strip(),
        'Подключение к компьютеру': features[2].split(': ', 1)[1].strip(),
        'Игровая': features[3].split(': ', 1)[1].strip(),
        'Цена': price
    }
    mouses.append(mouse)

with open('res.json', 'w', encoding='utf-8') as res:
    json.dump(mouses, res, indent=4, ensure_ascii=False)

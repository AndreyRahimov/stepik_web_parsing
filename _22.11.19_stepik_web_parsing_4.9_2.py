'''
Соберите данные со всех 5 категорий на сайте тренажере и соберите все
данные с карточек.
'''

import json
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm

start_response = requests.get('https://parsinger.ru/html/index1_page_1.html')
start_response.encoding = 'utf-8'
start_soup = BeautifulSoup(start_response.text, features='lxml')
categories = start_soup.find(class_='nav_menu')
URL_START = 'https://parsinger.ru/html/'
category_links = [URL_START + link['href'] for link in categories.find_all('a')]

names, description, prices = [], [], []
for category_link in tqdm(category_links):
    category_link_response = requests.get(category_link)
    category_link_response.encoding = 'utf-8'
    category_link_soup = BeautifulSoup(category_link_response.text, features='lxml')
    pages = category_link_soup.find(class_='pagen')
    page_links = [URL_START + link['href'] for link in pages.find_all('a')]
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

goods = []
for name, features, price in zip(names, description, prices):
    good = {
        'Название': name,
        'Бренд': features[0].split(':', 1)[1].strip(),
        features[1].split(':', 1)[0].strip(): features[1].split(':', 1)[1].strip(),
        features[2].split(':', 1)[0].strip(): features[2].split(':', 1)[1].strip(),
        features[3].split(':', 1)[0].strip(): features[3].split(':', 1)[1].strip(),
        'Цена': price
    }
    goods.append(good)

with open('res.json', 'w', encoding='utf-8') as res:
    json.dump(goods, res, indent=4, ensure_ascii=False)

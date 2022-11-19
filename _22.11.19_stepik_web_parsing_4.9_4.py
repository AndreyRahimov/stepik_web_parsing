'''
Соберите данные со всех 5 категорий на сайте тренажере и соберите все данные с
карточек + ссылка на карточку с товаром.
По результату выполнения кода в папке с проектом должен появится файл .json с
отступом в 4 пробела. Ключи в блоке description должны быть получены
автоматически из атрибутов HTML элементов.
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

names, description, prices, goods = [], [], [], []
for category_link in tqdm(category_links, desc='Scraping of categories...'):
    category_link_response = requests.get(category_link)
    category_link_response.encoding = 'utf-8'
    category_link_soup = BeautifulSoup(category_link_response.text, features='lxml')
    pages = category_link_soup.find(class_='pagen')
    page_links = [URL_START + link['href'] for link in pages.find_all('a')]
    for page_link in tqdm(page_links, desc='Scraping of pages...'):
        page_link_response = requests.get(page_link)
        page_link_response.encoding = 'utf-8'
        page_link_soup = BeautifulSoup(page_link_response.text, features='lxml')
        category = page_link_soup.find(class_='sale_button').find('a')['href'].split('/')[0]
        good_links = [
            URL_START + good_link.find('a')['href']
            for good_link
            in page_link_soup.find_all(class_='sale_button')]
        for good_link in good_links:
            good_link_response = requests.get(good_link)
            good_link_response.encoding = 'utf-8'
            good_link_soup = BeautifulSoup(good_link_response.text, features='lxml')
            good = {
                'category': category,
                'name': good_link_soup.find(id='p_header').text.strip(),
                'article': good_link_soup.find(class_='article').text.split(':')[1].strip(),
                'description': {
                    feature['id']: feature.text.split(':')[1].strip()
                    for feature
                    in good_link_soup.find(id='description').find_all('li')
                    },
                'count': int(good_link_soup.find(id='in_stock').text.split(':')[1]),
                'price': good_link_soup.find(id='price').text.strip(),
                'old_price': good_link_soup.find(id='old_price').text.strip(),
                'link': good_link
            }
            goods.append(good)

with open('res.json', 'w', encoding='utf-8') as res:
    json.dump(goods, res, indent=4, ensure_ascii=False)

'''
Выберите 1 любую категорию на сайте тренажёре, и соберите все данные с
карточек товаров + ссылка на карточку
'''

import json
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm

start_response = requests.get('https://parsinger.ru/html/index3_page_1.html')
start_response.encoding = 'utf-8'
start_soup = BeautifulSoup(start_response.text, features='lxml')
pages = start_soup.find(class_='pagen')
URL_START = 'https://parsinger.ru/html/'
page_links = [URL_START + link['href'] for link in pages.find_all('a')]

names, description, prices, mouses = [], [], [], []
for page_link in tqdm(page_links, desc='Page scraping...'):
    page_link_response = requests.get(page_link)
    page_link_response.encoding = 'utf-8'
    page_link_soup = BeautifulSoup(page_link_response.text, features='lxml')
    mouse_links = [
        URL_START + mouse_link.find('a')['href']
        for mouse_link
        in page_link_soup.find_all(class_='sale_button')]
    for mouse_link in mouse_links:
        mouse_link_response = requests.get(mouse_link)
        mouse_link_response.encoding = 'utf-8'
        mouse_link_soup = BeautifulSoup(mouse_link_response.text, features='lxml')
        mouse = {
            'category': 'mouses',
            'name': mouse_link_soup.find(id='p_header').text.strip(),
            'article': mouse_link_soup.find(class_='article').text.split(':')[1].strip(),
            'description': {
                feature['id']: feature.text.split(':')[1].strip()
                for feature
                in mouse_link_soup.find(id='description').find_all('li')
                },
            'count': int(mouse_link_soup.find(id='in_stock').text.split(':')[1]),
            'price': mouse_link_soup.find(id='price').text.strip(),
            'old_price': mouse_link_soup.find(id='old_price').text.strip(),
            'link': mouse_link
        }
        mouses.append(mouse)

with open('res.json', 'w', encoding='utf-8') as res:
    json.dump(mouses, res, indent=4, ensure_ascii=False)

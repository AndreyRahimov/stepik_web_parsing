'''
Напишите код, который собирает данные со всех страниц и категорий на сайте
тренажере и сохраните всё в таблицу.
'''

import csv
from bs4 import BeautifulSoup
import requests

start_response = requests.get('https://parsinger.ru/html/index1_page_1.html')
start_response.encoding = 'utf-8'
start_soup = BeautifulSoup(start_response.text, features='lxml')
categories = start_soup.find(class_='nav_menu')
URL_START = 'https://parsinger.ru/html/'
category_links = [URL_START + link['href'] for link in categories.find_all('a')]

rows = []
for category_link in category_links:
    category_link_response = requests.get(category_link)
    category_link_response.encoding = 'utf-8'
    category_link_soup = BeautifulSoup(category_link_response.text, features='lxml')
    pages = category_link_soup.find(class_='pagen')
    page_links = [URL_START + link['href'] for link in pages.find_all('a')]

    for page_link in page_links:
        page_link_response = requests.get(page_link)
        page_link_response.encoding = 'utf-8'
        page_link_soup = BeautifulSoup(page_link_response.text, features='lxml')
        goods = page_link_soup.find(class_='item_card').find_all(class_='img_box')
        
        for good in goods:
            description = [
                datum.text.split(':')[1].strip()
                for datum
                in good.find(class_='description').find_all('li')
                ]
            rows.append(
                [
                    good.find(class_='name_item').text,
                    *description,
                    good.find(class_='price').text
                    ]
                )

with open('res.csv', 'w', encoding='utf-8-sig', newline='') as res:
    writer = csv.writer(res, delimiter=';')
    writer.writerows(rows)

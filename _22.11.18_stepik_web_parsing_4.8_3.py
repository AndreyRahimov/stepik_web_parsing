'''
Напишите код, который собирает данные в категории watch c каждой карточки,
всего их 32.
'''

import csv
from bs4 import BeautifulSoup
import requests

start_response = requests.get('https://parsinger.ru/html/index1_page_1.html')
start_response.encoding = 'utf-8'
start_soup = BeautifulSoup(start_response.text, features='lxml')
pages = start_soup.find(class_='pagen')
URL_START = 'https://parsinger.ru/html/'
page_links = [URL_START + link['href'] for link in pages.find_all('a')]

rows = []
headers = [
    'Наименование',
    'Артикул',
    'Бренд',
    'Модель',
    'Тип',
    'Технология экрана',
    'Материал корпуса',
    'Материал браслета',
    'Размер',
    'Сайт производителя',
    'Наличие',
    'Цена',
    'Старая цена',
    'Ссылка на карточку с товаром'
    ]
for page_link in page_links:
    page_link_response = requests.get(page_link)
    page_link_response.encoding = 'utf-8'
    page_link_soup = BeautifulSoup(page_link_response.text, features='lxml')
    goods = page_link_soup.find_all(class_='sale_button')
    good_links = [URL_START + good.find('a')['href'] for good in goods]
    for good_link in good_links:
        good_link_response = requests.get(good_link)
        good_link_response.encoding = 'utf-8'
        page_link_soup = BeautifulSoup(good_link_response.text, features='lxml')
        row = {}
        row['Наименование'] = page_link_soup.find(id='p_header').text
        row['Артикул'] = page_link_soup.find(class_='article').text.split(': ')[1]
        description = {
            k: v.text.split(': ')[1]
            for k, v
            in zip(headers[2:10], page_link_soup.find(id='description').find_all('li'))}
        row = row | description
        row['Наличие'] = int(page_link_soup.find(id='in_stock').text.split(': ')[1])
        row['Цена'] = page_link_soup.find(id='price').text
        row['Старая цена'] = page_link_soup.find(id='old_price').text
        row['Ссылка на карточку с товаром'] = good_link
        rows.append(row)

with open('res.csv', 'w', encoding='utf-8-sig', newline='') as res:
    writer = csv.DictWriter(res, delimiter=';', fieldnames=headers)
    writer.writeheader()
    writer.writerows(rows)

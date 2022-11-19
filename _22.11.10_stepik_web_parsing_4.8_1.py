'''
Напишите код, который собирает данные в категории HDD со всех 4х страниц и
сохраняет всё в таблицу по примеру предыдущего степа. 
'''

import csv
import requests
from bs4 import BeautifulSoup

data = [['Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объём буф. памяти', 'Цена']]
start_response = requests.get('https://parsinger.ru/html/index4_page_1.html').text
start_soup = BeautifulSoup(start_response, 'lxml')
pages = start_soup.find(class_='pagen')
URL_START = 'https://parsinger.ru/html/'
links = [URL_START + link['href'] for link in pages.find_all('a')]

for link in links:
    link_response = requests.get(link)
    link_response.encoding = 'utf-8'
    link_soup = BeautifulSoup(link_response.text, 'lxml')
    for good in link_soup.find_all(class_='img_box'):
        good_data = []
        name = good.find(class_='name_item').text
        good_data.append(name)
        description = [desc.text.split(':')[1].strip() for desc in good.find(class_='description').find_all('li')]
        good_data.extend(description)
        price = good.find(class_='price').text
        good_data.append(price)
        data.append(good_data)

with open('res.csv', 'w', encoding='utf-8-sig', newline='') as res:
    writer = csv.writer(res, delimiter=';')
    writer.writerows(data)

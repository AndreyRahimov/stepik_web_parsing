'''
    На  сайте расположена таблица;
    Цель: Умножить число в оранжевой ячейке на число в голубой ячейке в той же строке и всё суммировать;
    Полученный результат вставить в поле ответа.
'''

import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/5/index.html').text
soup = BeautifulSoup(response, 'lxml')
oranges = [float(orange.text) for orange in soup.find_all(class_='orange')]
blues = [int(cell.text) for cell in soup.find_all('td') if '.' not in cell.text]
print(sum(orange * blue for orange, blue in zip(oranges, blues)))

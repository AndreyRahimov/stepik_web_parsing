'''
    На  сайте расположена таблица;
    Цель: Умножить число в оранжевой ячейке на число в голубой ячейке в той же строке и всё суммировать;
    Полученный результат вставить в поле ответа.
'''

import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/5/index.html').text
soup = BeautifulSoup(response, 'lxml')
keys = [cell.text for cell in soup.find_all('th')]
rows = soup.find_all('tr')
col_sum = [float(num.text) for num in rows[1].find_all('td')]
for row in rows[2:]:
    nums = [float(num.text) for num in row.find_all('td')]
    col_sum = [n_1 + n_2 for n_1, n_2 in zip(col_sum, nums)]
col_sum = [round(n, 3) for n in col_sum]

print(dict(zip(keys, col_sum)))

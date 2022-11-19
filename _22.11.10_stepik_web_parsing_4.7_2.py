'''
    На  сайте расположена таблица;
    Цель: Собрать числа которые выделены жирным шрифтом и суммировать их;
    Полученный результат вставить в поле ответа.
'''

from bs4 import BeautifulSoup
import requests

response = requests.get('https://parsinger.ru/table/3/index.html').text
soup = BeautifulSoup(response, 'lxml')
rows = soup.find_all('tr')
res = 0
for row in rows:
    cells = row.find_all('td')
    for cell in cells:
        if cell.find('b'):
            res += float(cell.find('b').text)

print(res)

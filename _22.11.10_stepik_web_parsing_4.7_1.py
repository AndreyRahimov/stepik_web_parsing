'''
    На  сайте расположена таблица;
    Цель: Собрать числа с 1го столбца и суммировать их;
    Полученный результат вставить в поле ответа.
'''

from bs4 import BeautifulSoup
import requests

response = requests.get('https://parsinger.ru/table/2/index.html').text
soup = BeautifulSoup(response, 'lxml')
rows = soup.find_all('tr')
res = 0
for row in rows:
    if row.find('td'):
        res += float(row.find('td').text)

print(res)

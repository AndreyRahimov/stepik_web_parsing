'''
    На  сайте расположена таблица;
    Цель: Собрать числа в зелёных ячейках и суммировать их;
    Полученный результат вставить в поле ответа.
'''

from bs4 import BeautifulSoup
import requests

response = requests.get('https://parsinger.ru/table/4/index.html').text
soup = BeautifulSoup(response, 'lxml')
cells = soup.find_all(class_='green')
res = 0
for cell in cells:
    res += float(cell.text)

print(res)

'''
    На  сайте расположена таблица;
    Цель: Собрать все уникальные числа из таблицы(кроме цифр в заголовке) и
    суммировать их;
    Полученный результат вставить в поле ответа.
'''

from bs4 import BeautifulSoup
import requests

response = requests.get('https://parsinger.ru/table/1/index.html').text
soup = BeautifulSoup(response, 'lxml')
cells = soup.find_all('td')
nums = set()
for cell in cells:
    nums.add(float(cell.text))
print(sum(nums))

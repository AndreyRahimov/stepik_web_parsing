'''
Используйте полученный по ссылке JSON чтоб посчитать количество товара в
каждой категории.
На вход ожидается словарь. {'watch': N, 'mobile': N, 'mouse': N, 'hdd': N,
'headphones': N} где N это общее количество товаров.
Количество вы найдёте в каждой карточке товара
'''

import requests

response = requests.get('https://parsinger.ru/downloads/get_json/res.json').json()
res = {}
for obj in response:
    category = obj['categories']
    amount = int(obj['count'])
    res[category] = res.get(category, 0) + amount
print(res)

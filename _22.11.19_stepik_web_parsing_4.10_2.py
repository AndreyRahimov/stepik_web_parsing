'''
Используйте полученный по ссылке JSON чтоб посчитать стоимость товаров в
каждой отдельной категории.
На вход ожидается словарь. {'watch': N, 'mobile': N, 'mouse': N, 'hdd': N,
'headphones': N} где N это общая стоимость товаров в категории.
'''

import requests

response = requests.get('https://parsinger.ru/downloads/get_json/res.json').json()
res = {}
for obj in response:
    category = obj['categories']
    amount = int(obj['count'])
    price = int(obj['price'].split()[0])
    res[category] = res.get(category, 0) + (price * amount)
print(res)

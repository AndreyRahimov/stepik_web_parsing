'''
    Открываем сайт
    Проходимся по всем категориям, страницам и карточкам с товарами(всего
    160шт)
    Собираем с каждой карточки стоимость товара умножая на количество товара в
    наличии
    Складываем получившийся результат
    Получившуюся цифру с общей стоимостью всех товаров вставляем в поле ответа.
'''

from bs4 import BeautifulSoup
import requests

start_response = requests.get('http://parsinger.ru/html/index1_page_1.html').text
start_soup = BeautifulSoup(start_response, 'lxml')
categories = start_soup.find(class_='nav_menu').find_all('a')
FIRST_PART_OF_LINK = 'https://parsinger.ru/html/'
category_links = [FIRST_PART_OF_LINK + category['href'] for category in categories]
res = 0

for category_link in category_links:
    category_response = requests.get(category_link).text
    category_soup = BeautifulSoup(category_response, 'lxml')
    pages = category_soup.find(class_='pagen').find_all('a')
    page_links = [FIRST_PART_OF_LINK + page['href'] for page in pages]

    for page_link in page_links:
        page_response = requests.get(page_link).text
        page_soup = BeautifulSoup(page_response, 'lxml')
        goods = page_soup.find_all(class_='sale_button')
        good_links = [FIRST_PART_OF_LINK + good.find('a')['href'] for good in goods]

        for good_link in good_links:
            good_response = requests.get(good_link).text
            good_soup = BeautifulSoup(good_response, 'lxml')
            price = int(good_soup.find(id='price').text.split()[0])
            amount = int(good_soup.find(id='in_stock').text.split()[-1])
            res += price * amount

print(res)

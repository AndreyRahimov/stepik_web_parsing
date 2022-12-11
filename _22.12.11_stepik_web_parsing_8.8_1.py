'''
Откройте сайт тренажёр;
Напишите асинхронный код, который обработает все карточки(160шт);
Необходимо вычислить общий размер скидки для всех товаров в рублях;
Вставьте полученное значение в поле для ответа:
'''

import asyncio
import aiohttp
from bs4 import BeautifulSoup
import requests

start_response = requests.get('https://parsinger.ru/html/index1_page_1.html')
start_response.encoding = 'utf-8'
start_soup = BeautifulSoup(start_response.text, features='lxml')
categories = start_soup.find(class_='nav_menu')
URL_START = 'https://parsinger.ru/html/'
category_links = [URL_START + link['href'] for link in categories.find_all('a')]
page_links, good_links, discounts, tasks = [], [], [], []


async def make_soup(link: str, session):
    async with session.get(link) as response:
        link_response = await response.text()
        return BeautifulSoup(link_response, features='lxml')


async def get_page_links(link: str, session) -> None:
    soup = await make_soup(link, session)
    pages = soup.find(class_='pagen')
    page_links.extend([URL_START + link['href']
                       for link
                       in pages.find_all('a')])


async def get_good_links(link: str, session) -> None:
    soup = await make_soup(link, session)
    good_links.extend([
            URL_START + good_link.find('a')['href']
            for good_link
            in soup.find_all(class_='sale_button')])


async def get_discounts(link: str, session) -> None:
    soup = await make_soup(link, session)
    price = int(soup.find(id='price').text.split()[0])
    old_price = int(soup.find(id='old_price').text.split()[0])
    amount = int(soup.find(id='in_stock').text.split()[-1])
    discounts.append(amount * (old_price - price))


def make_tasks(links: list, func, session) -> list:
    tasks.clear()
    for link in links:
        task = asyncio.create_task(func(link, session))
        tasks.append(task)
    return tasks


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*make_tasks(
            category_links,
            get_page_links,
            session
            ))
        await asyncio.gather(*make_tasks(
            page_links,
            get_good_links,
            session
            ))
        await asyncio.gather(*make_tasks(
            good_links,
            get_discounts,
            session
            ))


asyncio.run(main())
print(sum(discounts))

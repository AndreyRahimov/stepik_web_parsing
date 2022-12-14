'''
    Откройте сайт, там есть 500 ссылок, секретный код лежит только на четырёх
    из них;
    Напишите асинхронный код, который найдёт все четыре кода и суммирует их;
    Суммируйте все полученный цифры и вставьте результат в поле для ответа:
'''

import asyncio
import aiohttp
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm

url_begin = 'https://parsinger.ru/asyncio/create_soup/1/'
start_response = requests.get('https://parsinger.ru/asyncio/create_soup/1/index.html')
start_response.encoding = 'utf-8'
start_soup = BeautifulSoup(start_response.text, features='lxml')
links = [url_begin + attr['href']
         for attr
         in start_soup.find_all(class_='lnk_img')]
codes = []


async def get_code(link: str) -> None:
    '''Returns a secret code, if there is one on the link'''
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            if response.status == 200:
                link_response = await response.text()
                soup = BeautifulSoup(link_response, features='lxml')
                codes.append(int(soup.find(class_='text').text))


tasks = [get_code(link)
         for link
         in links]
asyncio.run(asyncio.wait(tqdm(tasks)))
print(sum(codes))

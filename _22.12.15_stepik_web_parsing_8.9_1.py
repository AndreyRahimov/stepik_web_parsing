'''
Откройте сайт, на нём есть 50 ссылок, в каждой ссылке лежит по 10 изображений;
Ваша задача: Написать асинхронный код который скачает все уникальные
изображения которые там есть (они повторяются, а уникальных всего 449) ;
Вставьте размер всех скачанных изображений в поле для ответа
'''

import asyncio
import os
import aiofiles
import aiohttp
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm

start_response = requests.get('https://parsinger.ru/asyncio/aiofile/2/index.html')
start_response.encoding = 'utf-8'
start_soup = BeautifulSoup(start_response.text, features='lxml')
url_begin = 'https://parsinger.ru/asyncio/aiofile/2/'
links = [url_begin + attr['href']
         for attr
         in start_soup.find_all(class_='lnk_img')]
img_links = set()
progress = tqdm(total=450, desc='Downloading images...')


async def download_img(link: str,
                       image_name: str,
                       session: aiohttp.ClientSession) -> None:
    '''Downloads image from URL and saves it as image_name'''
    async with aiofiles.open('images/' + image_name, 'wb') as image:
        async with session.get(link) as response:
            async for chunk in response.content.iter_chunked(1024):
                await image.write(chunk)
                progress.update(1)


async def get_img_links(link: str,
                        session: aiohttp.ClientSession) -> None:
    '''Saves all image URLs from link in img_links list'''
    async with session.get(link) as response:
        global img_links
        soup = BeautifulSoup(await response.text(), 'lxml')
        img_links |= {tag['src'] for tag in soup.find_all(class_='picture')}


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_img_links(link, session))
                 for link
                 in links]
        await asyncio.gather(*tasks)
        tasks = [download_img(link, link.split('/')[-1], session)
                 for link
                 in img_links]
        await asyncio.gather(*tasks)


def get_folder_size(dirpath, size=0):
    for root, _, files in os.walk(dirpath):
        for file in files:
            size += os.path.getsize(os.path.join(root, file))
    return size


asyncio.run(main())
progress.close()
print(get_folder_size('images/'))

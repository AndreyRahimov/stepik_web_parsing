'''
Откройте сайт, на нём есть 100 ссылок, в каждой из них есть ещё 10 ссылок, в
каждой из 10 ссылок есть 8-10 изображений
Ваша задача: Написать асинхронный код который скачает все уникальные
изображения которые там есть (они повторяются, в это задании вам придётся
скачать 2615 изображений) ;
Вставьте размер всех скачанных изображений в поле для ответа
'''

import asyncio
import os
import aiofiles
import aiohttp
from aiohttp_retry import RetryClient, ExponentialRetry
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm

start_response = requests.get('https://parsinger.ru/asyncio/aiofile/3/index.html')
start_response.encoding = 'utf-8'
start_soup = BeautifulSoup(start_response.text, features='lxml')
link_begin = 'https://parsinger.ru/asyncio/aiofile/3/'
links = [link_begin + attr['href']
         for attr
         in start_soup.find_all(class_='lnk_img')]

imd_downloading_progress = tqdm(total=2615, desc='Downloading images...')
img_links = set()
img_link_progress = tqdm(total=999, desc='Searching image links...')
url_link_begin = 'https://parsinger.ru/asyncio/aiofile/3/depth2/'
url_links = []
url_link_progress = tqdm(total=1_000, desc='Searching URL links...')


async def download_img(link: str,
                       image_name: str,
                       client) -> None:
    '''Downloads image from URL and saves it as image_name'''
    try:
        async with aiofiles.open('images/' + image_name, 'wb') as image:
            async with client.get(link) as response:
                async for chunk in response.content.iter_chunked(4096):
                    await image.write(chunk)
        imd_downloading_progress.update(1)
    except Exception as ex:
        print(ex)
        download_img(link,
                     image_name,
                     client)


async def get_img_links(link: str,
                        client) -> None:
    '''Saves all URL links from link in img_links set'''
    async with client.get(link) as response:
        global img_links
        soup = BeautifulSoup(await response.text(), 'lxml')
        img_links |= {tag['src'] for tag in soup.find_all(class_='picture')}
        img_link_progress.update(1)


async def get_url_links(link: str,
                        client) -> None:
    '''Saves all URL links from link in url_links list'''
    async with client.get(link) as response:
        soup = BeautifulSoup(await response.text(), 'lxml')
        url_links.extend([url_link_begin + attr['href']
                          for attr
                          in soup.find_all(class_='lnk_img')])
        url_link_progress.update(10)


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        options = ExponentialRetry(attempts=10)
        retry_client = RetryClient(raise_for_status=False,
                                   retry_options=options,
                                   client_session=session)
        tasks = [asyncio.create_task(get_url_links(link, retry_client))
                 for link
                 in links]
        await asyncio.gather(*tasks)
        url_link_progress.close()
        tasks = [asyncio.create_task(get_img_links(link, retry_client))
                 for link
                 in url_links]
        await asyncio.gather(*tasks)
        img_link_progress.close()
        tasks = [download_img(link, link.split('/')[-1], retry_client)
                 for link
                 in img_links]
        await asyncio.gather(*tasks)
        imd_downloading_progress.close()


def get_folder_size(dirpath, size=0):
    for root, _, files in os.walk(dirpath):
        for file in files:
            size += os.path.getsize(os.path.join(root, file))
    return size


asyncio.run(main())
print(get_folder_size('images/'))

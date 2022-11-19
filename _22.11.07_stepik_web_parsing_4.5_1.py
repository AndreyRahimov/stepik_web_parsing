from bs4 import BeautifulSoup
import requests

response = requests.get('https://parsinger.ru/html/index3_page_4.html').text
soup = BeautifulSoup(response, 'lxml')
pages = soup.find(class_='pagen').find_all('a')
FIRST_PART_OF_LINK = 'https://parsinger.ru/html/'
links = [FIRST_PART_OF_LINK + page['href'] for page in pages]
res = 0

for link in links:
    link_response = requests.get(link).text
    link_soup = BeautifulSoup(link_response, 'lxml')
    good_pages = link_soup.find_all(class_='sale_button')
    good_links = [FIRST_PART_OF_LINK + good_page.find('a')['href'] for good_page in good_pages]
    for good_link in good_links:
        good_link_response = requests.get(good_link).text
        good_link_soup = BeautifulSoup(good_link_response, 'lxml')
        article = good_link_soup.find(class_='article').text
        article = int(article.split()[-1])
        res += article

print(res)
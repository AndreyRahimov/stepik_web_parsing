'''
    Откройте сайт с помощью Selenium;
    На сайте есть определённое количество секретных cookie;
    Ваша задача получить все значения и суммировать их;
    Полученный результат вставить в поле для ответа.
'''

from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/3/index.html')
    cookies = browser.get_cookies()
    print(sum(int(value['value']) for value in cookies))

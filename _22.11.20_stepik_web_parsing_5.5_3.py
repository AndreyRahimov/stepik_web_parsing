'''
    Откройте сайт с помощью Selenium;
    На сайте есть 42 ссылки, у каждого сайта по ссылке есть cookie с
    определёнными сроком жизни;
    Цель: написать скрипт, который сможет найти среди всех ссылок страницу с
    самым длинным сроком жизни cookie и получить с этой страницы число;
    Вставить число в поле для ответа.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/5/index.html')
    max_cookie_expiry = 0
    res = ''
    links = browser.find_elements(By.CLASS_NAME, 'urls')
    for link in links:
        link.click()
        cookies = browser.get_cookies()
        for cookie in cookies:
            expiry = int(cookie['expiry'])
            if expiry > max_cookie_expiry:
                max_cookie_expiry = expiry
                res = browser.find_element(By.ID, 'result').text
        browser.back()
    print(res)

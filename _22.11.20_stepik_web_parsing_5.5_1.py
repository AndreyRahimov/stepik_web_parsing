'''
    Откройте сайт с помощью Selenium;
    При обновлении сайта, в id="result" появится число;
    Обновить страницу возможно придется много раз, т.к. число появляется не
    часто;
    Вставьте полученный результат в поле для ответа:
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/1/index.html')
    while browser.find_element(By.ID, 'result').text == 'refresh page':
        browser.refresh()
    print(browser.find_element(By.ID, 'result').text)

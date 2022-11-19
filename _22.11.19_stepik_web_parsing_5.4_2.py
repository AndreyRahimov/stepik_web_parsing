'''
    Откройте сайт;
    Извлеките данные из каждого тега <p>;
    Сложите все значения, их всего 300 шт;
    Напишите получившийся результат в поле ниже.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    print(sum(int(tag.text) for tag in browser.find_elements(By.TAG_NAME, 'p')))

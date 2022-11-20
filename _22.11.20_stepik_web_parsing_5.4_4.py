'''
    Откройте сайт;
    Извлеките данные из каждого  второго тега <p>;
    Сложите все значения, их всего 100 шт;
    Напишите получившийся результат в поле ответа.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    print(sum(int(tag.text.split('\n')[1]) for tag in browser.find_elements(By.CLASS_NAME, 'text')))

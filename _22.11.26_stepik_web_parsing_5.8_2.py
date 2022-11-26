'''
    Откройте сайт при помощи Selenium;
    На сайте есть кнопка, которая становится активной после загрузки страницы
    с рандомной задержкой, от 1 до 3 сек;
    После нажатия на кнопку, в title начнут появляться коды, с рандомным
    временем, от 0,1 до 0.6 сек;
    В этот раз второй раз на кнопку кликать не нужно, а нужно получить title
    целиком, если title содержит "JK8HQ"
    Используйте метод title_contains(title) с прошлого урока;
    Вставьте полный текст заголовка который совпадает с частью заголовка из
    условия.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/expectations/4/index.html')
    WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable((By.ID, 'btn'))).click()
    WebDriverWait(driver, 60).until(expected_conditions.title_contains('JK8HQ'))
    print(driver.title)

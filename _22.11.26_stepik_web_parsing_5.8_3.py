'''
    Откройте сайт при помощи Selenium;
    На сайте есть кнопка, поведение которой вам знакомо;
    После нажатие на кнопку, на странице начнётся создание элементов class с
    рандомными значениями;
    Ваша задача применить метод, чтобы он вернул содержимое элемента с классом
    "BMH21YY", когда он появится на странице;
    Полученное значение вставить в поле для ответа.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/expectations/5/index.html')
    WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable((By.ID, 'btn'))).click()
    WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'BMH21YY')))
    print(driver.find_element(By.CLASS_NAME, 'BMH21YY').text)

'''
    Откройте сайт с помощью selenium;
    Необходимо открыть окно таким размером, чтобы рабочая область страницы
    составляла 555px на 555px;
    Учитывайте размеры границ браузера;
    Результат появится в id="result";
    Вставьте полученный результат в поле для ответа.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/window_size/1/')
    driver.set_window_size(555, 673)
    print(driver.find_element(By.ID, 'result').text)

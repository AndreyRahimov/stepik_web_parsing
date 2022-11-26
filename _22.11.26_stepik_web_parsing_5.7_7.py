'''
    Откройте сайт с помощью Selenium;
    На сайте есть 10 buttons, каждый button откроет сайт в новой вкладке;
    Каждая вкладка имеет в title уникальное число;
    Цель - собрать числа с каждой вкладки и суммировать их;
    Полученный результат вставить в поле для ответа.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/blank/3/index.html')
    for button in driver.find_elements(By.CLASS_NAME, 'buttons'):
        button.click()

    counter = 0
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        if driver.execute_script('return document.title;').isdigit():
            counter += int(driver.execute_script('return document.title;'))
    print(counter)

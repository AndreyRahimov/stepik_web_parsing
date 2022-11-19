'''
    Открыть сайт с помощью selenium;
    Заполнить все существующие поля;
    Нажмите на кнопку;
    Скопируйте результат который появится рядом с кнопкой в случае если вы уложились в 5 секунд;
    Вставьте результат в поле ниже.
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    input_forms = browser.find_elements(By.CLASS_NAME, 'form')
    for form in input_forms:
        form.send_keys('Text')
    send_button = browser.find_element(By.ID, 'btn').click()
    time.sleep(10)

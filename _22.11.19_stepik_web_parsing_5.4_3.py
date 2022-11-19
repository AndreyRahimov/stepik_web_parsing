'''
    Открыть сайт с помощью selenium;
    Заполнить все существующие поля;
    Нажмите на кнопку;
    Скопируйте результат который появится рядом с кнопкой в случае если вы уложились в 5 секунд;
    Вставьте результат в поле ниже.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/2/2.html')
    link = browser.find_element(By.LINK_TEXT, '16243162441624').click()
    res = browser.find_element(By.ID, 'result').text
    print(res)

'''
    Откройте сайт при помощи selenium;
    Решите уравнение на странице;
    Найдите и выберите в  выпадающем списке элемент с числом, которое у вас
    получилось после решения уравнения;
    Нажмите на кнопку;
    Скопируйте число и вставьте в поле ответа.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.html')
    value = eval(browser.find_element(By.ID, 'text_box').text)
    value_list = browser.find_elements(By.TAG_NAME, 'option')
    for v in value_list:
        if int(v.text) == value:
            v.click()
            break
    browser.find_element(By.ID, 'sendbutton').click()
    print(browser.find_element(By.ID, 'result').text)

'''
    Открываем сайт с помощью selenium;
    Получаем значения всех элементов выпадающего списка;
    Суммируем(плюсуем) все значения;
    Вставляем получившийся результат в поле на сайте;
    Нажимаем кнопку и копируем длинное число;
    Вставляем конечный результат в поле ответа.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.html')
    value = sum(int(n.text)
                for n
                in browser.find_elements(By.TAG_NAME, 'option'))
    browser.find_element(By.ID, 'input_result').send_keys(value)
    browser.find_element(By.ID, 'sendbutton').click()
    print(browser.find_element(By.ID, 'result').text)

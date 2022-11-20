'''
    Откройте сайт с помощью Selenium;
    На сайте есть 50 кнопок, которые визуально перекрыты блоками;
    После нажатия на кнопку в id="result" появляется уникальное для каждой 
    кнопки число;
    Цель: написать скрипт который нажимает поочерёдно все кнопки и собирает
    уникальные числа;
    Все полученные числа суммировать, и вставить результат в поле для ответа.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/scroll/4/index.html')
    buttons = browser.find_elements(By.CLASS_NAME, 'btn')
    counter = 0
    for button in buttons:
        browser.execute_script('return arguments[0].scrollIntoView(true);',
                               button)
        button.click()
        counter += int(browser.find_element(By.ID, 'result').text)
    print(counter)

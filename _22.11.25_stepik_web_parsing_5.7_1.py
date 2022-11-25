'''
    Откройте сайт при помощи Selenium;
    На сайте есть 100 buttons;
    При нажатии на одну из кнопок в  теге <p id="result">Code</p> появится код;
    Вставьте секретный код в поле для ответа.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/blank/modal/2/index.html')
    buttons = driver.find_elements(By.CLASS_NAME, 'buttons')
    for button in buttons:
        button.click()
        driver.switch_to.alert.accept()
        if driver.find_element(By.ID, 'result').text:
            print(driver.find_element(By.ID, 'result').text)
            break

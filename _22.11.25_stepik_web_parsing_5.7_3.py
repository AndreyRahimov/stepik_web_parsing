'''
    Откройте сайт при помощи Selenium;
    На сайте есть список пин-кодов и только один правильный;
    Для проверки пин-кода используйте кнопку "Проверить"
    Ваша задача, найти правильный пин-код и получить секретный код;
    Вставьте секретный код в поле для ответа.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/blank/modal/4/index.html')
    check_button = driver.find_element(By.ID, 'check')
    for pin in driver.find_elements(By.CLASS_NAME, 'pin'):
        to_check = pin.text
        check_button.click()
        alert = driver.switch_to.alert
        alert.send_keys(to_check)
        alert.accept()
        if driver.find_element(By.ID, 'result').text != 'Неверный пин-код':
            print(driver.find_element(By.ID, 'result').text)
            break

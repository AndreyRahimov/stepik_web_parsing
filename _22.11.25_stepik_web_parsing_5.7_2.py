'''
    Откройте сайт при помощи Selenium;
    На сайте есть 100 buttons;
    При нажатии на любую кнопку появляется confirm с пин-кодом;
    Текстовое поле под кнопками проверяет правильность пин-кода;
    Ваша задача, найти правильный пин-код и получить секретный код;
    Вставьте секретный код в поле для ответа.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/blank/modal/3/index.html')
    buttons = driver.find_elements(By.CLASS_NAME, 'buttons')
    input_field = driver.find_element(By.ID, 'input')
    check_button = driver.find_element(By.ID, 'check')
    for button in buttons:
        button.click()
        alert = driver.switch_to.alert
        code = alert.text
        alert.accept()
        input_field.send_keys(code)
        check_button.click()
        if driver.find_element(By.ID, 'result').text != 'Неверный пин-код':
            print(driver.find_element(By.ID, 'result').text)
            break

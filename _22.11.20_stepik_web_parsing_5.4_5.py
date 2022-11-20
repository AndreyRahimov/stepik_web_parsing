'''
    Откройте сайт;
    Установите все чек боксы в положение checked при помощи selenium и метода
    click();
    Когда все чек боксы станут активны, нажмите на кнопку;
    Скопируйте число которое появится на странице;
    Результат появится в <p id="result">Result</p>;
    Вставьте число в поле для ответа.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/4/4.html')
    checkboxes = browser.find_elements(By.CLASS_NAME, 'check')
    for checkbox in checkboxes:
        checkbox.click()
    browser.find_element(By.CLASS_NAME, 'btn').click()
    print(browser.find_element(By.ID, 'result').text)

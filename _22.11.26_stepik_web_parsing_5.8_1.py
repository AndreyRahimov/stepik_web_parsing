'''
    Откройте сайт при помощи Selenium;
    На сайте есть кнопка, которая становится активной после загрузки страницы
    с рандомной задержкой, от 1 до 3 сек;
    После нажатия на кнопку, в title начнут появляться коды, с рандомным
    временем, от 0.1 до 0.6 сек;
    Ваша задача успеть скопировать код из id="result", когда  title будет
    равен "345FDG3245SFD";
    Вставить  появившийся  код в поле для ответа.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/expectations/3/index.html')
    WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable((By.ID, 'btn'))).click()
    WebDriverWait(driver, 60).until(expected_conditions.title_is('345FDG3245SFD'))
    print(driver.find_element(By.ID, 'result').text)

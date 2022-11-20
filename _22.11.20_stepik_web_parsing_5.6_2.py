'''
    Откройте сайт с помощью Selenium;
    На сайте есть 100 чекбоксов, 25 из них вернут число;
    Ваша задача суммировать все появившиеся числа;
    Отправить получившийся результат в поля ответа.
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/scroll/2/index.html')
    actions = ActionChains(driver)
    items = driver.find_elements(By.CLASS_NAME, 'item')
    counter = 0
    for item in items:
        checkbox = item.find_element(By.CLASS_NAME, 'checkbox_class')
        actions.move_to_element(checkbox)
        actions.click()
        actions.perform()
        if item.find_element(By.TAG_NAME, 'span').text:
            counter += int(item.find_element(By.TAG_NAME, 'span').text)
    print(counter)

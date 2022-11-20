'''
    Откройте сайт сайт с помощью Selenium;
    Ваша задача, получить числовое значение id="число" с каждого тега <input>
    который при нажатии вернул число;
    Суммируйте все значения и отправьте результат в поле ниже.
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/scroll/3/')
    actions = ActionChains(driver)
    items = driver.find_elements(By.CLASS_NAME, 'item')
    counter = 0
    for item in items:
        checkbox = item.find_element(By.CLASS_NAME, 'checkbox_class')
        actions.move_to_element(checkbox)
        actions.click()
        actions.perform()
        if item.find_element(By.TAG_NAME, 'span').text:
            counter += int(checkbox.get_attribute('id'))
    print(counter)

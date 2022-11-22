'''
    Откройте сайт с помощью Selenium;
    На сайте есть список из 100 элементов, которые генерируются при скроллинге;
    Необходимо прокрутить окно в самый низ;
    Цель: получить все значение в элементах, сложить их;
    Получившийся результат вставить в поле ответа.
'''

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/infiniti_scroll_2/')
    window = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div')
    actions = ActionChains(driver)
    for _ in range(9):
        actions.move_to_element(window).scroll_by_amount(0, 500).perform()

    counter = 0
    scroll_container = driver.find_element(By.ID, 'scroll-container')
    p_tags = scroll_container.find_elements(By.TAG_NAME, 'p')
    for p_tag in p_tags:
        counter += int(p_tag.text)
    print(counter)

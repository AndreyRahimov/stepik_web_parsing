'''
    Откройте сайт с помощью Selenium 
    На сайте есть 5 окошек с подгружаемыми элементами, в каждом по 100
    элементов;
    Необходимо прокрутить все окна в самый низ;
    Цель: получить все значение в каждом из окошек и сложить их;
    Получившийся результат вставить в поле ответа.
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    actions = ActionChains(driver)
    driver.get('https://parsinger.ru/infiniti_scroll_3/')
    paths = ('/html/body/div/div[1]/div[1]/div',
             '/html/body/div/div[2]/div[1]/div',
             '/html/body/div/div[3]/div[1]/div',
             '/html/body/div/div[4]/div[1]/div',
             '/html/body/div/div[5]/div[1]/div')
    for path in paths:
        window = driver.find_element(By.XPATH, path)
        for _ in range(8):
            actions.move_to_element(window).scroll_by_amount(0, 500).perform()

    counter = 0
    spans = driver.find_elements(By.TAG_NAME, 'span')
    for span in spans:
        counter += int(span.text)
    print(counter)

'''
    Откройте сайт с помощью selenium;
    У вас есть 2 списка с размера окон size_x и size_y;
    Цель: определить размер окна, при котором,  в id="result" появляется число;
    Результат должен быть в виде словаря {'width': size_x, 'height': size_y}
'''

from itertools import product
from selenium import webdriver
from selenium.webdriver.common.by import By

widths = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
heights = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/window_size/2/index.html')
    for width, height in product(widths, heights):
        driver.set_window_size(width, height + 118)
        if res := driver.find_element(By.ID, 'result').text:
            print({'width': width,
                   'height': height})
            break

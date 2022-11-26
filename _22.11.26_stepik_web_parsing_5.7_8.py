'''
    У вас есть список сайтов, 6 шт;
    На каждом сайте есть chekbox, нажав на этот chekbox появится код;
    Ваша задача написать скрипт, который открывает при помощи Selenium все
    сайты во вкладках (.window_handles);
    Проходит в цикле по каждой вкладке, нажимает на chekbox и сохранеят код;
    Из каждого числа, необходимо извлечь корень, функцией sqrt();
    Суммировать получившиеся корни и вставить результат в поле для ответа.
'''

import math
from selenium import webdriver
from selenium.webdriver.common.by import By

sites = ['http://parsinger.ru/blank/1/1.html',
         'http://parsinger.ru/blank/1/2.html',
         'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html',
         'http://parsinger.ru/blank/1/5.html',
         'http://parsinger.ru/blank/1/6.html']

with webdriver.Chrome() as driver:
    for site in sites:
        driver.execute_script(f"window.open('{site}');")

    counter = 0
    for handle in driver.window_handles[1:]:
        driver.switch_to.window(handle)
        driver.find_element(By.CLASS_NAME, 'checkbox_class').click()
        counter += math.sqrt(int(driver.find_element(By.ID, 'result').text))
print(counter)

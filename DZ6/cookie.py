from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

my_cookie = {  # переменная с объектом
    'name': 'cookie_policy',
    'value': '1'}

driver.get("https://labirint.ru/")  # переход на страницу
driver.add_cookie(my_cookie)  # добавление cookie

cookie = driver.get_cookie('PHPSESSID')  # положили метод в переменную cookie
print(cookie)  # попросили вывести данных по этой cookie в терминал

driver.refresh()  # обновление страницы
driver.delete_all_cookies()  # удаление всех cookie


driver.refresh()  # обновление страницы

cookies = driver.get_cookies()  # переменная, в которую соберутся cookies
print(cookies)  # запрос на вывод данных в терминал

sleep(10)
driver.quit()

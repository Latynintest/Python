from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru")  # переход на сайт

element = driver.find_element(By.CSS_SELECTOR, "#text")  # поиск элемента
print(element)  # отображение результата в терминале
element.clear()  # очищаем текстовое поле
element.send_keys("test skypro")  # отправляем текст
driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
sleep(10)

driver.quit()

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import TimeoutException, NoSuchElementException


cookie = {'name': 'cookie_policy', 'value': '1'}


def test_card_counter():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.maximize_window()

    # Открыть сайт лабиринта
    driver.get("https://www.labirint.ru/")
    driver.implicitly_wait(4)
    driver.add_cookie(cookie)

    # Найти все книги по слову Python
    driver.find_element(By.CSS_SELECTOR, '#search-field').send_keys('Python')
    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

    # Добавить все книги в корзину и посчитать
    buy_buttons = driver.find_elements(By.CSS_SELECTOR, '[data-carttext]')
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1

    # Перейти в корзину
    driver.get("https://www.labirint.ru/cart/")

    # Проверить счетчик товаров. Должен быть равен числу нажатий
    # Получить текущее значение
    txt = driver.find_element(
        By.CSS_SELECTOR, '#basket-default-prod-count2').text
    # Сравнить c counter
    assert counter == int(txt.split()[0])

    driver.quit()

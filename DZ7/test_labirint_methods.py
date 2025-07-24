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
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))


def open_labirint():
    # Открыть сайт лабиринта
    driver.get("https://www.labirint.ru/")
    driver.implicitly_wait(4)
    driver.add_cookie(cookie)


def search(term):
    # Найти все книги по слову
    driver.find_element(By.CSS_SELECTOR, '#search-field').send_keys(term)
    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()


def add_books():
    # Добавить все книги в корзину и посчитать
    buy_buttons = driver.find_elements(By.CSS_SELECTOR, '[data-carttext]')
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1
    return counter


def go_to_cart():
    # Перейти в корзину
    driver.get("https://www.labirint.ru/cart/")


def get_cart_counter():
    # Проверить счетчик товаров. Должен быть равен числу нажатий
    txt = driver.find_element(
        By.CSS_SELECTOR, '#basket-default-prod-count2').text
    # Возвращаем число
    return int(txt.split()[0])


def close_driver():
    # Закрываем браузер
    driver.quit()


def test_card_counter():
    try:
        driver.maximize_window()
        open_labirint()  # Открываем сайт
        search("Python")  # Ищем книги по слову
        added = add_books()  # Добавляем книги и сохраняем результат в переменную
        go_to_cart()  # Идем в корзину
        cart_counter = get_cart_counter()  # Забираем значение счетчика из корзины
    finally:
        close_driver()  # закрываем браузер

    assert added == cart_counter  # Сравниваем counter со счетчиком корзины


def test_empty_search():
    try:
        open_labirint()
        search("12345678901234567890")
        txt = driver.find_element(
            By.CSS_SELECTOR, ".b-rfooter-info-e-text").text.strip()
    finally:
        close_driver()

    assert txt.split("?")[0].strip() == \
        "Пока не нашли для себя ничего в Лабиринте"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import TimeoutException, NoSuchElementException

cookie = {'name': 'cookie_policy', 'value': '1'}  # Исправлено имя cookie


def test_card_counter():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:
        # Открыть сайт лабиринта
        driver.get("https://www.labirint.ru/")
        driver.add_cookie(cookie)

        # Поиск книг по Python
        search_field = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#search-field')))
        search_field.send_keys('Python')
        driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

        # Ожидание загрузки результатов поиска
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[data-carttext]')))

        # Добавление книг в корзину
        buy_buttons = driver.find_elements(
            By.CSS_SELECTOR, 'a._btn.btn-tocart.buy-link:not(.btn-more)')
        counter = 0

        for btn in buy_buttons:
            try:
                btn.click()
                counter += 1
                # Ждём появления всплывающего окна
                wait.until(EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, '.basket-in-cart-a')))
            except Exception as e:
                print(f"Не удалось добавить товар: {e}")
                continue

        # Переход в корзину
        driver.get("https://www.labirint.ru/cart/")

        # Проверка счетчика
        cart_counter = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '#basket-default-prod-count2')))
        cart_count = int(cart_counter.text.split()[0])

        assert counter == cart_count, f"Ожидалось {counter} товаров, но в корзине {cart_count}"

    except Exception as e:
        print(f"Тест упал с ошибкой: {e}")
        raise
    finally:
        driver.quit()

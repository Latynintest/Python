import pytest
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage
from checkout_overview_page import CheckoutOverviewPage


# Данные для теста
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
FIRST_NAME = "Sergey"
LAST_NAME = "Latynin"
ZIP_CODE = "302023"
EXPECTED_TOTAL = "$58.29"
ITEMS_TO_ADD = [
    "add-to-cart-sauce-labs-backpack",
    "add-to-cart-sauce-labs-bolt-t-shirt",
    "add-to-cart-sauce-labs-onesie"
]


@pytest.fixture(scope="function")
def browser():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(
        service=FirefoxService(
            GeckoDriverManager().install()), options=options)
    yield driver
    driver.quit()


def test_saucedemo(browser):
    # 1. Авторизация
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login(USERNAME, PASSWORD)

    # 2. Добавление товаров в корзину
    inventory_page = InventoryPage(browser)
    for item in ITEMS_TO_ADD:
        inventory_page.add_item_to_cart(item)
        print(f"Добавлен товар: {item.replace('add-to-cart-', '')}")

    # 3. Переход в корзину и оформление заказа
    inventory_page.go_to_cart()
    cart_page = CartPage(browser)
    cart_page.proceed_to_checkout()

    # 4. Заполнение формы доставки
    checkout_page = CheckoutPage(browser)
    checkout_page.fill_shipping_info(FIRST_NAME, LAST_NAME, ZIP_CODE)

    # 5. Проверка итоговой суммы
    overview_page = CheckoutOverviewPage(browser)
    total_value = overview_page.get_total_amount()
    assert total_value == EXPECTED_TOTAL, f"Ожидалась сумма {EXPECTED_TOTAL}, получено {total_value}"
    print(f"Тест пройден! Итоговая сумма: {total_value}")

from selenium import webdriver
from pages.CartPage import CartPage
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage


def test_cart_counter():
    browser = webdriver.Chrome()  # Открываем браузер
    main_page = MainPage(browser)  # Экземпляр класса с передачей драйвера
    main_page.set_cookie_policy()  # Вызываем метод
    main_page.search('Python')

    result_page = ResultPage(browser)
    to_be = result_page.add_books()

    cart_page = CartPage(browser)
    cart_page.get()  # Переход на страницу с корзиной
    as_is = cart_page.get_counter()  # Текущее значение счетчика на странице

    assert as_is == to_be


def test_empty_search():
    browser = webdriver.Chrome()
    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.search("12345678901234567890")

    result_page = ResultPage(browser)
    msg = result_page.get_empty_result_message()

    assert msg == "Пока не нашли для себя ничего в Лабиринте?"

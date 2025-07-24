import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()


def test_slow_calculator(browser):
    calculator = CalculatorPage(browser)

    # 1. Открыть страницу калькулятора
    calculator.open()

    # 2. Установить задержку 45 секунд
    calculator.set_delay(45)

    # 3. Нажать кнопки 7 + 8 =
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")

    # 4. Ожидать результат и проверить его
    calculator.wait_for_result(46, "15")
    assert "15" in calculator.get_result(
    ), f"Ожидался результат 15, получено: {calculator.get_result()}"
    print("Тест пройден! Результат 15 отобразился корректно")

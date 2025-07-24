from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


# Оформление заказа
class CheckoutPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def fill_shipping_info(self, first_name: str, last_name: str, zip_code: str):
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys(zip_code)
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

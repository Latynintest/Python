from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


# Корзина
class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def proceed_to_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()

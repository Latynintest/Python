from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Страница товаров
class InventoryPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_item_to_cart(self, item_id: str):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f"[data-test='{item_id}']")))
        button.click()

    def go_to_cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link").click()

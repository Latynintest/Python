from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def get(self):
        self.driver.get("https://www.labirint.ru/cart/")

    def get_counter(self):
        txt = self.driver.find_element(
            By.ID, 'basket-default-prod-count2').text
        # Забираем только число из строки "26 товаров"
        number_str = txt.split()[0]
        return int(number_str)

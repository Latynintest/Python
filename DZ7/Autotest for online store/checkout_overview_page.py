from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Подтверждение заказа
class CheckoutOverviewPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_total_amount(self) -> str:
        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".summary_total_label")))
        return total_element.text.split()[-1]

from selenium.webdriver.common.by import By


class ResultPage:

    def __init__(self, driver):
        self.driver = driver

    def add_books(self):
        buy_buttons = self.driver.find_elements(
            By.CSS_SELECTOR, "[data-carttext]")

        counter = 0
        for btn in buy_buttons:
            btn.click()
            counter += 1

        return counter

    def get_empty_result_message(self):
        element = self.driver.find_element(
            By.CSS_SELECTOR, ".b-rfooter-info-e-text"
        )
        full_text = element.text.strip()
        # для получения только первой строчки
        first_part = full_text.split("?")[0].strip()
        return f"{first_part}?"

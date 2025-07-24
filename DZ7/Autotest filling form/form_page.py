from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class FormPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

# Открывает страницу
    def open(self):
        self.driver.get(self.url)

# Заполняет поле
    def fill_field(self, field_name: str, value: str):
        self.driver.find_element(
            By.CSS_SELECTOR, f'input[name="{field_name}"]').send_keys(value)

# Отправляет форму
    def submit(self):
        self.driver.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]').click()

# Проверяет подсветку поля
    def get_field_alert_class(self, field_id: str) -> str:
        element = self.driver.find_element(By.CSS_SELECTOR, field_id)
        return element.get_attribute("class")

# Получает текст из поля
    def get_field_text(self, field_id: str) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, field_id).text

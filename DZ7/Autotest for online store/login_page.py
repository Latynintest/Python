from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


# Авторизация
class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def open(self):
        self.driver.get(self.url)

    def login(self, username: str, password: str):
        self.driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys(username)
        self.driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

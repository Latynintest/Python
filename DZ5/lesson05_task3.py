from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Инициализация драйвера

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))


# Переход на страницу
driver.get("http://the-internet.herokuapp.com/inputs")


# Ожидание и ввод первого текста
input_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[type='number']")))

input_field.send_keys("Sky")


# Очистка поля
input_field.clear()


# Ввод нового текста
input_field.send_keys("Pro")


driver.quit()

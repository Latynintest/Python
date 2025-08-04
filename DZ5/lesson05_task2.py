from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Инициализация драйвера
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=options)

# Переход на страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Поиск и клик по синей кнопке
blue_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary")))
blue_button.click()
print("Синяя кнопка успешно нажата")

driver.quit()

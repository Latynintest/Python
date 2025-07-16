from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")  # Явный размер окна


# Инициализация драйвера
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=options)


# Переходим на страницу
driver.get("http://uitestingplayground.com/ajax")

# Нажимаем на синюю кнопку
ajax_button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# Ожидаем появления зеленой плашки и получаем текст
success_message = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success")))

# Выводим текст в консоль
print(success_message.text)  # "Data loaded with AJAX get request."


driver.quit()

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

# Открываем страницу
driver.get("http://the-internet.herokuapp.com")

# Ожидаем появления элемента с текстом "A/B Testing"
ab_testing = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/abtest"]')))
print(f"Элемент '{ab_testing.text}' найден и виден")


# Устанавливаем неявное ожидание 10 секунд
driver.implicitly_wait(10)

# Открываем страницу
driver.get("https://www.seleniumeasy.com/lander")

# Поиск элемента
element = driver.find_element(By.CSS_SELECTOR, "#getButton")
print(f"Элемент найден: {element.text}")

driver.quit()

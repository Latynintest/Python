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
driver.get("http://uitestingplayground.com/textinput")

# Вводим текст "SkyPro" в поле ввода
input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_field.clear()  # Очищаем поле
input_field.send_keys("SkyPro")

# Нажимаем на синюю кнопку
button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()

# Получаем обновленный текст кнопки
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((
        By.CSS_SELECTOR, "#updatingButton"), "SkyPro"))

# Выводим текст кнопки в консоль
print(f"Текст кнопки: '{driver.find_element(
    By.CSS_SELECTOR, "#updatingButton").text}'")

driver.quit()

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


# Задача 1

# Переходим на страницу
driver.get("http://uitestingplayground.com/ajax")

# Нажимаем на синюю кнопку
ajax_button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# Ожидаем появления зеленой плашки и получаем текст
success_message = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success")))

# Выводим текст в консоль
print(success_message.text)  # "Data loaded with AJAX get request."


# Задача 2

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


# Задача 3

# Установка неявного ожидания
driver.implicitly_wait(10)

# Переходим на страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Ждём загрузки всех картинок (4 изображения)
images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
while len(images) < 4:
    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")

# Получаем src третьей картинки
third_image_src = images[2].get_attribute("src")
print(f"Атрибут src 3-й картинки: {third_image_src}")


driver.quit()

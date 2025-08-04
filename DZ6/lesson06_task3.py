from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")  # Явный размер окна


# Инициализация драйвера
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=options)

# Переходим на страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Ждем загрузки всех изображений
WebDriverWait(driver, 30).until(lambda d: all(d.find_element(
    By.ID, img_id).get_attribute("src")
    for img_id in ["compass", "calendar", "award", "landscape"]))

# Получаем третье изображение (award) по ID
image = driver.find_element(By.ID, "award")
image_src = image.get_attribute("src")
print(f"Атрибут src 3-й картинки: {image_src}")

driver.quit()

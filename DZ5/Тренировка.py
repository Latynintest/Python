import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import (TimeoutException,
                                        NoSuchElementException,
                                        StaleElementReferenceException,
                                        ElementClickInterceptedException)

options = webdriver.ChromeOptions()


# Настройки для подавления логов
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--disable-logging")
options.add_argument("--disable-cloud-services")
options.add_argument("--disable-gcm")

# Настройки приватности и анти-детекта
options.add_argument("--disable-webgl")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# Инициализация драйвера
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=options)

# JavaScript-инъекция для скрытия автоматизации
driver.execute_script(
    "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.maximize_window()


# Задача 1
url = "https://www.example.com"

try:
    driver.get(url)
    print("Заголовок страницы:", driver.title)
except Exception as e:
    print("Ошибка:", e)
driver.save_screenshot("./ya.png")


# Задача 2
try:
    driver.get("https://www.python.org")

    #  Закрываем куки-баннер (если есть)
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.ID, "cookie-consent-button"))).click()
        print("✅ Куки-баннер успешно закрыт")
    except TimeoutException:
        print("ℹ️ Куки-баннер не появился в течение 10 секунд")
    except NoSuchElementException:
        print("ℹ️ Элемент куки-баннера не найден в DOM")
    except Exception as e:
        print(f"⚠️ Неожиданная ошибка: {type(e).__name__}: {str(e)}")

    #  Кликаем на кнопку Donate (новый XPath)
    donate_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.donate-button')))
    time.sleep(2)  # Пауза 2 секунды перед кликом
    donate_button.click()

    #  Ждём загрузки страницы доната (проверяем URL)
    WebDriverWait(driver, 5).until(
        EC.url_contains("psfmember.org/civicrm/contribute"))

    #  Проверяем финальный URL
    final_url = driver.current_url
    if "psfmember.org/civicrm/contribute" in final_url:
        print("✅ Успех! Открыта страница доната:", final_url)
    else:
        print("❌ Ошибка: открыт неверный URL:", final_url)

except Exception as e:
    print(f"❌ Ошибка: {e}")


# Задача 3
driver.get("https://www.google.com/")

search_box = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#APjFqb")))
search_box.send_keys("Selenium" + Keys.ENTER)
time.sleep(2)  # Даем время для загрузки результатов


driver.quit()

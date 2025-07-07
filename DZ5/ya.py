
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import TimeoutException, NoSuchElementException


# Настройка для подавления логов
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # TensorFlow
os.environ['NO_PROXY'] = '127.0.0.1'      # Для DevTools

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--disable-logging")
options.add_argument("--disable-features=VoiceTranscription")
options.add_argument("--disable-cloud-services")
options.add_argument("--disable-gcm")


# Для headless-режима:
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
options.add_argument("--headless=new")  # Новый headless-режим
options.add_argument("--window-size=1920,1080")  # Фиксированный размер окна
options.add_argument("--no-sandbox")  # Для Docker/CI
options.add_argument("--disable-dev-shm-usage")  # Для ограниченной памяти


# Эмуляция мобильного устройства
mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 ("
    "iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15"}
options.add_experimental_option("mobileEmulation", mobile_emulation)

# Отключение автоматического управления сервисными процессами
options.add_experimental_option("useAutomationExtension", False)

# Не закрывать браузер после теста
options.add_experimental_option("detach", True)

# Игнорирование SSL-ошибок (для тестовых окружений)
options.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))


# Отладка headless-режима
# Логирование консоли:
options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
driver.get("https://example.com")
logs = driver.get_log("browser")

# Подключение DevTools:
driver.execute_cdp_cmd("Network.enable", {})


driver.get("https://ya.ru/")  # открывается первая страница
driver.get("https://vk.com/")  # открывается вторая страница
driver.get("https://ya.ru/")
driver.get("https://vk.com/")
driver.back()
driver.get("https://ya.ru/")
driver.get("https://vk.com/")
driver.back()  # Вернуться назад
driver.forward()  # Перейти вперед
driver.get("https://ya.ru/")
driver.get("https://vk.com/")
for x in range(1, 10):
    driver.back()
    driver.forward()
driver.refresh()  # Обновить страницу
driver.get("https://ya.ru/")  # браузер откроет страницу
driver.get("https://vk.com/")  # перейдет на следующую страницу
driver.set_window_size(640, 460)  # окно браузера уменьшится под параметры
driver.maximize_window  # открыть окно по размеру экрана
driver.minimize_window  # свернуть окно браузера
driver.fullscreen_window  # развернуть окно на весь экран, аналог F11
driver.get("https://ya.ru/")
driver.get("https://vk.com/")
driver.set_window_size(640, 460)
sleep(10)
driver.save_screenshot("./ya.png")

# Закрываем куки-баннер (если есть)
try:
    cookie_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.cookie-policy"))
    )
    cookie_button.click()
    print("✅ Куки-баннер успешно закрыт")
except TimeoutException:
    print("ℹ️ Куки-баннер не появился в течение 10 секунд")
except NoSuchElementException:
    print("ℹ️ Элемент куки-баннера не найден в DOM")
except Exception as e:
    print(f"⚠️ Неожиданная ошибка: {type(e).__name__}: {str(e)}")

sleep(50)
# Убирает пробелы и переносы в Локатор
# $x("//span[normalize-space()='Везде']").length

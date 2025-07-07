from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Автоматическая установка и настройка драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Открытие страницы
driver.get("https://google.com")
print("Заголовок страницы:", driver.title)

# Закрыть браузер
driver.quit()

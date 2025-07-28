import pytest
from selenium import webdriver
from google_page_object import GoogleMainPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


# Фикстура для инициализации и закрытия браузера
@pytest.fixture()
def driver():
    # Инициализация опций (первая строка сохранена)
    options = webdriver.ChromeOptions()

    # Настройки для подавления логов
    options.add_experimental_option(
        "excludeSwitches", ["enable-logging", "enable-automation"])
    options.add_argument("--log-level=3")  # FATAL уровень логов
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-cloud-services")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-gcm")
    options.add_argument("--silent")

    # Настройки приватности и анти-детекта
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # Инициализация драйвера
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options)

    # Устанавливаем неявные ожидания (5 сек)
    driver.implicitly_wait(5)  # Fallback-ожидания для всех элементов

    # JavaScript-инъекция для скрытия автоматизации
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    yield driver
    # После теста автоматически закрываем браузер
    driver.quit()


# Фикстура для инициализации страницы Google
@pytest.fixture()
def google_page(driver):
    # Получаем driver из основной фикстуры
    page = GoogleMainPage(driver)
    # Открываем главную страницу Google
    driver.get("https://www.google.com/")
    # Возвращает экземпляр GoogleMainPage
    return page


# Проверка качества поиска
def test_search_quality(google_page):
    # Выполняем поиск
    query = "Python"
    google_page.search(query)

    # Получаем результаты
    results = google_page.get_search_results()

    assert len(results) > 0, "Результаты поиска не найдены."

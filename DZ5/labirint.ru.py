from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import TimeoutException, NoSuchElementException


driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.maximize_window()

# Открыть сайт лабиринта
driver.get("https://www.labirint.ru/")

# Найти книги по слову Python
search_field = "#search-field"
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
search_input.send_keys("Python")
search_input.send_keys(Keys.ENTER)
sleep(5)  # Подождать 5 секунд, чтобы страница успела загрузиться

# Закрываем куки-баннер (если есть)
button_selector = "button.cookie-policy__button.js-cookie-policy-agree"
locator = (By.CSS_SELECTOR, button_selector)
clickable_condition = EC.element_to_be_clickable(locator)

try:
    cookie_button = WebDriverWait(driver, 10).until(clickable_condition)
    cookie_button.click()
    print("✅ Куки-баннер успешно закрыт")
except TimeoutException:
    print("ℹ️ Куки-баннер не появился в течение 10 секунд")
except NoSuchElementException:
    print("ℹ️ Элемент куки-баннера не найден в DOM")
except Exception as e:
    print(f"⚠️ Неожиданная ошибка: {type(e).__name__}: {str(e)}")

# Собрать все карточки товаров
books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")
print(len(books))


# Вывести в консоль инфо: название + автор + цена
for book in books:
    title = book.find_element(By.CSS_SELECTOR, "a.product-card__name").text
    price = book.find_element(
        By.CSS_SELECTOR, "div.product-card__price-current").text
    author = " "
    try:
        author = book.find_element(
            By.CSS_SELECTOR, "div.product-card__author").text
    except NoSuchElementException:
        author = "Автор не указан"
    print(author + "\t" + title + "\t" + price)

sleep(10)
driver.quit()

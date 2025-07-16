from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru")


txt = driver.find_element(
    By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.1"]').text
tag = driver.find_element(
    By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.1"]').tag_name
# собираем информацию об идентификаторе
id = driver.find_element(
    By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.1"]').id
href = driver.find_element(
    By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.1"]').get_attribute("href")
ff = (driver.find_element(By.CSS_SELECTOR,
      '[data-statlog="2informers.stocks.item.1"]').value_of_css_property("font-family"))
ffc = (driver.find_element(By.CSS_SELECTOR,
                           '[data-statlog="2informers.stocks.item.1"]').value_of_css_property("color"))
ffh = (driver.find_element(By.CSS_SELECTOR,
                           '[data-statlog="2informers.stocks.item.1"]').value_of_css_property("height"))
ffl = (driver.find_element(By.CSS_SELECTOR,
                           '[data-statlog="2informers.stocks.item.1"]').value_of_css_property("letter-spacing"))

print(txt)  # запрос выведет информацию из переменной в терминал
print(tag)  # выводим информацию из переменной в терминал
print(id)  # выводим информацию из переменной в терминал
print(href)  # выводим информацию по атрибуту
print(ff)
print(ffc)  # информация о цвете элемента
print(ffh)  # информация о высоте элемента
print(ffl)  # информация о расстоянии между буквами


driver.get("http://uitestingplayground.com/visibility")  # переход на сайт

# проверка видимости кнопки Opacity 0
is_displayed = driver.find_element(
    By.CSS_SELECTOR, "#transparentButton").is_displayed()
print(is_displayed)  # вывод статуса видимости Opacity 0

driver.find_element(By.CSS_SELECTOR, "#hideButton").click()  # нажатие на Hide
# Opacity 0 окажется скрытой
sleep(2)

# еще раз проверим видимость Opacity 0:
is_displayed = driver.find_element(
    By.CSS_SELECTOR, "#transparentButton").is_displayed()
print(is_displayed)  # еще раз выводим статус видимости Opacity 0


driver.get("https://demoqa.com/radio-button")
is_enabled = driver.find_element(By.CSS_SELECTOR, "#yesRadio").is_enabled()
print(is_enabled)
is_enabled = driver.find_element(By.CSS_SELECTOR, "#noRadio").is_enabled()
print(is_enabled)


driver.get("https://the-internet.herokuapp.com/checkboxes")
cb = driver.find_element(By.CSS_SELECTOR, "input[type=checkbox]")
is_selected = cb.is_selected()
print(is_selected)
sleep(3)
cb.click()
is_selected = cb.is_selected()
print(is_selected)


# идем на страницу:
driver.get("https://the-internet.herokuapp.com/checkboxes")

# записываем верхнюю html-ветку в переменную div
div = driver.find_element(By.CSS_SELECTOR, "#page-footer")

# через div идем по ветке до элемента с тегом a
a = div.find_element(By.CSS_SELECTOR, "a")

# запрашиваем ссылку из элемента с тегом a
print(a.get_attribute("href"))


# переходим на страницу:
driver.get("https://the-internet.herokuapp.com/checkboxes")

# ищем все элементы по тегу div и записываем в переменную divs:
divs = driver.find_elements(By.CSS_SELECTOR, "div")
l = len(divs)
print(l)


# переходим на сайт:
driver.get("https://the-internet.herokuapp.com/checkboxes")
# ищем все элементы по тегу div и записываем в переменную divs:
divs = driver.find_elements(By.CSS_SELECTOR, "div")
# в переменную div помещаем элемент с индексом = 6 из списка divs:
div = divs[6]


driver.get("https://the-internet.herokuapp.com/checkboxes")

divs = driver.find_elements(By.CSS_SELECTOR, "div")

div = divs[6]
# запрашиваем атрибуты и помещаем в переменную css_class:
css_class = div.get_attribute("class")
# выводим в терминал:
print(css_class)


driver.get("https://demoqa.com/browser-windows")
driver.find_element(By.CSS_SELECTOR, "#tabButton").click()
driver.get("https://demoqa.com/browser-windows")
driver.find_element(By.CSS_SELECTOR, "#tabButton").click()
sleep(5)
driver.get("https://demoqa.com/browser-windows")
driver.find_element(By.CSS_SELECTOR, "#tabButton").click()
sleep(5)
driver.close()
sleep(5)

driver.quit()  # закрываем драйвер

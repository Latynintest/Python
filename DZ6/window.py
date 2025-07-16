from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru")
driver.maximize_window()  # развернуть окно под размер экрана
sleep(10)
driver.minimize_window()  # свернуть окно
sleep(10)
driver.fullscreen_window()  # развернуть окно на весь экран (аналог F11)
sleep(10)
driver.set_window_size(1000, 600)
sleep(10)

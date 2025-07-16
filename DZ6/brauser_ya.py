from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from selenium.webdriver.opera.service import Service as OperaService
# from webdriver_manager.opera import OperaDriverManager
import time


def make_screenshot(browser, browser_name):
    try:
        browser.maximize_window()
        browser.get("https://ya.ru/")

        # Явное ожидание появления поисковой строки
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input#text")))

        browser.save_screenshot(f"./ya_{browser_name}.png")
        print(f"Скриншот {browser_name} сохранён!")

    except Exception as e:
        print(f"Ошибка в {browser_name}: {str(e)}")
    finally:
        browser.quit()


# Запуск браузеров по очереди с паузами
try:
    # Chrome
    chrome = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    make_screenshot(chrome, "chrome")
    time.sleep(2)

    # Firefox
    ff = webdriver.Firefox(service=FirefoxService(
        GeckoDriverManager().install()))
    make_screenshot(ff, "firefox")
    time.sleep(2)

    # Edge
    # edge = webdriver.Edge(service=EdgeService(
    #     EdgeChromiumDriverManager().install()))
    # make_screenshot(edge, "edge")
    # time.sleep(2)

    # Opera
    # opera = webdriver.Opera(service=OperaService(
    #     OperaDriverManager().install()))
    # make_screenshot(opera)
    # time.sleep(2)

except Exception as e:
    print(f"Критическая ошибка: {str(e)}")

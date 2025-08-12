from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class GoogleMainPage:
    def __init__(self, driver):
        self.driver = driver
        # Селектор поля поиска
        self.search_box = (By.NAME, 'q')
        # Селектор результатов
        self.results_selector = (By.CSS_SELECTOR, 'div#search .tF2Cxc')

    def human_like_typing(self, element, text):
        # Имитация человеческого ввода
        actions = ActionChains(self.driver)
        for char in text:
            actions.send_keys(char).pause(0.1)
        actions.perform()

    def search(self, query):
        # Выполняет поиск по запросу.
        # Безопасный поиск с обходом капчи
        self.driver.get("https://www.google.com/ncr")  # Отключение локализации
        # Ожидает кликабельности поля поиска.
        search_box_element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.search_box))
        # Очищает поле.
        search_box_element.clear()
        # Вводит текст и имитирует нажатие Enter
        self.human_like_typing(search_box_element, query)
        search_box_element.send_keys(Keys.RETURN)

    def get_search_results(self, min_results=1):
        # Возвращает список результатов поиска
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.results_selector))
        # Возвращает все найденные элементы.
        return self.driver.find_elements(*self.results_selector)

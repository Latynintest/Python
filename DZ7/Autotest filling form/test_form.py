import pytest
from selenium.webdriver.edge.service import Service
from selenium import webdriver
from form_page import FormPage


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Edge(service=Service(
        executable_path='C:/Users/Сергей/Desktop/Edge/msedgedriver.exe'))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_validation(browser):
    page = FormPage(browser)
    page.open()

    # Заполнение полей
    fields_to_fill = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_name, value in fields_to_fill.items():
        page.fill_field(field_name, value)

    page.submit()

    # Проверки
    assert "alert-danger" in page.get_field_alert_class(
        "#zip-code"), "Zip code не красный"

    success_fields = [
        ("#first-name", "Иван"),
        ("#last-name", "Петров"),
        ("#address", "Ленина, 55-3"),
        ("#e-mail", "test@skypro.com"),
        ("#phone", "+7985899998787"),
        ("#city", "Москва"),
        ("#country", "Россия"),
        ("#job-position", "QA"),
        ("#company", "SkyPro")
    ]

    for field_id, expected_value in success_fields:
        assert "alert-success" in page.get_field_alert_class(
            field_id), f"Поле {field_id} не зеленое"
        assert expected_value in page.get_field_text(
            field_id), f"Текст в {field_id} не совпадает"

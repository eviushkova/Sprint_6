import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from pages.main_page import MainPage
from pages.order_scooter_page import OrderScooter
from pages.header_page import HeaderPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    # options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def main_page(driver):
    main_page_url = 'https://qa-scooter.praktikum-services.ru/'
    page = MainPage(driver)
    page.get_url(main_page_url)
    page.accept_cookies()
    return page


@pytest.fixture()
def order_page(driver, main_page):
    page = OrderScooter(driver)
    return page


@pytest.fixture()
def header(driver):
    order_page_url = 'https://qa-scooter.praktikum-services.ru/order'
    page = HeaderPage(driver)
    page.get_url(order_page_url)
    page.accept_cookies()
    return page

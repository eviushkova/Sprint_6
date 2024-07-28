from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    def formatted_locator(self, locator, num):
        method, locator = locator
        locator = locator.format(num)
        return method, locator

    def accept_cookies(self):
        self.find_element_with_wait(MainPageLocators.COOKIE_LOCATOR)
        self.click_on_element(MainPageLocators.COOKIE_LOCATOR)

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_last_opened_browser_tab(self):
        browser_tabs = self.driver.window_handles
        self.driver.switch_to.window(browser_tabs[-1])

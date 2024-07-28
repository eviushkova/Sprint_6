import allure

from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):
    @allure.step('Клик на логотип "Самокат"')
    def click_on_scooter_logo_in_header(self):
        self.click_on_element(HeaderLocators.LOGO_SCOOTER)

    @allure.step('Клик на лототип "Яндекс"')
    def click_on_logo_yandex_in_header(self):
        self.click_on_element(HeaderLocators.YANDEX_LOGO)

    @allure.step('Проверить наличие кнопки "Найти" на странице Dzen')
    def check_find_button_in_new_tab(self):
        self.find_element_with_wait(HeaderLocators.FIND_BUTTON)

import allure
from faker import Faker

from locators.order_scooter_locators import OrderScooterLocators
from pages.base_page import BasePage

fake = Faker('ru_RU')


class OrderScooter(BasePage):

    @allure.step('Нажать на кнопку "Заказать"')
    def click_on_order_button(self, order_button_locator):
        self.click_on_element(order_button_locator)

    @allure.step('Заполнить поле "Имя"')
    def fill_name(self, name):
        self.click_on_element(OrderScooterLocators.INPUT_NAME)
        self.set_text_to_element(OrderScooterLocators.INPUT_NAME, name)

    @allure.step('Заполнить поле "Фамилия"')
    def fill_last_name(self, last_name):
        self.click_on_element(OrderScooterLocators.INPUT_LAST_NAME)
        self.set_text_to_element(OrderScooterLocators.INPUT_LAST_NAME, last_name)

    @allure.step('Заполнить поле "Адрес"')
    def fill_address(self, address):
        self.click_on_element(OrderScooterLocators.INPUT_ADDRESS)
        self.set_text_to_element(OrderScooterLocators.INPUT_ADDRESS, address)

    @allure.step('Выбрать станцию метро')
    def choose_metro_station(self):
        self.click_on_element(OrderScooterLocators.INPUT_SEARCH_METRO_STATION)
        self.click_on_element(OrderScooterLocators.METRO_STATION_ROKOSSOVSKOGO)

    @allure.step('Заполнить поле "Телефон"')
    def fill_phone_numer(self, phone):
        self.click_on_element(OrderScooterLocators.INPUT_PHONE)
        self.set_text_to_element(OrderScooterLocators.INPUT_PHONE, phone)

    @allure.step('Нажать кнопку "Далее"')
    def click_on_button_next(self):
        self.click_on_element(OrderScooterLocators.NEXT_BUTTON)

    @allure.step('Выбрать дату доставки самоката')
    def choose_delivery_date(self):
        self.click_on_element(OrderScooterLocators.DATE_INPUT)
        self.click_on_element(OrderScooterLocators.DATE_PICKER_DAY)

    @allure.step('Выбрать срок аренды')
    def choose_rental_period(self):
        self.find_element_with_wait(OrderScooterLocators.RENTAL_PERIOD_DROPDOWN)
        self.click_on_element(OrderScooterLocators.RENTAL_PERIOD_DROPDOWN)
        self.click_on_element(OrderScooterLocators.RENTAL_PERIOD_OPTION)

    @allure.step('Выбрать цвет самоката')
    def choose_scooter_color(self):
        self.click_on_element(OrderScooterLocators.CHECKBOX_GREY_BY_ID)

    @allure.step('Написать комментарий для курьера')
    def write_comment_for_courier(self, comment):
        self.click_on_element(OrderScooterLocators.INPUT_COMMENT)
        self.set_text_to_element(OrderScooterLocators.INPUT_COMMENT, comment)

    @allure.step('Клик на кнопку "Заказать"')
    def click_on_order_button_final(self):
        self.click_on_element(OrderScooterLocators.ORDER_BUTTON)

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.click_on_element(OrderScooterLocators.YES_BUTTON)

    @allure.step('Получить подтверждение об успешном заказе')
    def get_confirmation_order(self):
        successful_order = self.get_text_from_element(OrderScooterLocators.SUCCESS_ORDER_MODAL_WINDOW)
        return successful_order

    def fill_form(self, locator, name, last_name, address, phone, comment):
        self.click_on_order_button(locator)
        self.fill_name(name)
        self.fill_last_name(last_name)
        self.fill_address(address)
        self.choose_metro_station()
        self.fill_phone_numer(phone)
        self.click_on_button_next()
        self.choose_delivery_date()
        self.choose_rental_period()
        self.choose_scooter_color()
        self.write_comment_for_courier(comment)
        self.click_on_order_button_final()
        self.confirm_order()

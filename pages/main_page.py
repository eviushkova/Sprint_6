import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Прокрутить до последнего вопроса')
    def scroll_to_last_question(self):
        self.scroll_to_element(MainPageLocators.LAST_QUESTION_LOCATOR)

    @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        formatted_question_locator = self.formatted_locator(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_element(formatted_question_locator)
        self.click_on_element(formatted_question_locator)

    @allure.step('Получить текст ответа')
    def get_answer(self, num):
        formatted_answer_locator = self.formatted_locator(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(formatted_answer_locator)

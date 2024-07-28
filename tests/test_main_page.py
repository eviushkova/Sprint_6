import allure
import pytest

from data import Answers
from locators.main_page_locators import MainPageLocators


class TestsMainPage:
    @allure.title('Проверка соответсвия ответов на вопросы в блоке "Вопросы о важном"')
    @pytest.mark.parametrize(
        "question_number, expected_result",
        [
            (0, Answers.ANSWER_QUESTION_1),
            (1, Answers.ANSWER_QUESTION_2),
            (2, Answers.ANSWER_QUESTION_3),
            (3, Answers.ANSWER_QUESTION_4),
            (4, Answers.ANSWER_QUESTION_5),
            (5, Answers.ANSWER_QUESTION_6),
            (6, Answers.ANSWER_QUESTION_7),
            (7, Answers.ANSWER_QUESTION_8),
        ]

    )
    def test_click_on_question_get_answer(self, main_page, question_number, expected_result):
        main_page.scroll_to_element(MainPageLocators.LAST_QUESTION_LOCATOR)
        main_page.click_to_question(question_number)
        result = main_page.get_answer(question_number)
        assert result == expected_result

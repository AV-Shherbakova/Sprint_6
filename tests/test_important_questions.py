import pytest

from conftest import driver
from data import *
from page_objects.home_page import HomePage
from urls import BASE_URL


class TestImportantQuestions:

    @pytest.mark.parametrize(
        "index, text",
        [
            (0, QUESTION_ANSWER_1),
            (1, QUESTION_ANSWER_2),
            (2, QUESTION_ANSWER_3),
            (3, QUESTION_ANSWER_4),
            (4, QUESTION_ANSWER_5),
            (5, QUESTION_ANSWER_6),
            (6, QUESTION_ANSWER_7),
            (7, QUESTION_ANSWER_8)
        ]
    )
    def test_check_answer_text(self, driver, index, text):
        driver.get(BASE_URL)
        home_page = HomePage(driver)
        panel_text = home_page.click_question_and_return_text(index)
        assert panel_text == text

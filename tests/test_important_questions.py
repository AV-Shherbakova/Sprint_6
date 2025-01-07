import pytest
from selenium import webdriver

from conftest import *
from page_objects.important_questions import ImportantQuestions


class TestImportantQuestions:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

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
    def test_check_answer_text(self, index, text):
        self.driver.get(BASE_URL)
        questions_page = ImportantQuestions(self.driver)
        panel_text = questions_page.click_element_and_return_hidden(index)
        assert panel_text == text

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

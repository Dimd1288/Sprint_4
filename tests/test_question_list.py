from selenium import webdriver
import pytest
from constants import MAIN_URL, QUESTIONS, ANSWERS
from pages.main_page import MainPage


class TestQuestions:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(MAIN_URL)

    @pytest.mark.parametrize('question, answer', map(lambda x, y: (x, y), QUESTIONS, ANSWERS))
    def test_questions_and_answers(self, question, answer):
        main_questions = MainPage(self.driver)
        main_questions.scroll_to_questions()
        main_questions.check_question_and_answer(question, answer)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

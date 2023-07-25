import pytest
from constants import QUESTIONS, ANSWERS
from pages.main_page import MainPage


@pytest.mark.usefixtures("cls_driver")
class TestQuestions:

    @pytest.mark.parametrize('question, answer', map(lambda x, y: (x, y), QUESTIONS, ANSWERS))
    def test_questions_and_answers(self, question, answer):
        main_questions = MainPage(self.driver)
        main_questions.scroll_to_questions()
        main_questions.check_question_and_answer(question, answer)

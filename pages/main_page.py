from selenium.webdriver.common.by import By
from pages.common_elements import CommonElements

from locators import main_page_locators


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def check_home_header_is_displayed(self):
        assert self.driver.find_element(*main_page_locators.home_header).is_displayed()

    def check_question_and_answer(self, question, answer):
        question_elem = main_page_locators.question_xpath.format(question=question)
        answer_elem = main_page_locators.answer_xpath.format(question=question)
        self.driver.find_element(By.XPATH, question_elem).click()
        CommonElements(self.driver).wait_for_element_displayed([By.XPATH, answer_elem])
        assert self.driver.find_element(By.XPATH, answer_elem).text == answer, "Ответ не соответствует вопросу"

    def scroll_to_questions(self):
        element = self.driver.find_element(*main_page_locators.questions_header)
        CommonElements(self.driver).scroll_to_element(element)

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import main_page_locators


class MainQuestions:

    def __init__(self, driver):
        self.driver = driver

    def check_question_and_answer(self, question, answer):
        question_elem = main_page_locators.question_locator.format(question=question)
        answer_elem = main_page_locators.answer_locator.format(question=question)
        self.driver.find_element(By.XPATH, question_elem).click()
        self.wait_for_element_displayed([By.XPATH, answer_elem])
        assert self.driver.find_element(By.XPATH, answer_elem).text == answer

    def wait_for_element_displayed(self, element):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(element))

    def scroll_to_questions(self):
        questions_header = self.driver.find_element(*main_page_locators.questions_header)
        self.driver.execute_script("arguments[0].scrollIntoView();", questions_header)

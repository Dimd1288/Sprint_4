from selenium.webdriver.common.by import By

from locators.header_locators import HeaderLocators
from locators.main_page_locators import order_button
from pages.base_page import BasePage

from locators import main_page_locators


class MainPage(BasePage):

    def check_home_header_is_displayed(self):
        self.check_element_is_displayed(*main_page_locators.home_header)

    def check_question_and_answer(self, question, answer):
        question_elem = main_page_locators.question_xpath.format(question=question)
        answer_elem = main_page_locators.answer_xpath.format(question=question)
        self.driver.find_element(By.XPATH, question_elem).click()
        BasePage(self.driver).wait_for_element_displayed([By.XPATH, answer_elem])
        assert self.driver.find_element(By.XPATH, answer_elem).text == answer, "Ответ не соответствует вопросу"

    def scroll_to_questions(self):
        element = self.driver.find_element(*main_page_locators.questions_header)
        BasePage(self.driver).scroll_to_element(element)

    def click_order_button(self, element='header'):
        if element == 'header':
            self.driver.find_element(*HeaderLocators().order_button_locator).click()
        else:
            self.scroll_to_element(self.driver.find_element(*order_button))
            self.wait_for_element_displayed(order_button)
            self.driver.find_element(*order_button).click()

    def click_status_button(self):
        self.driver.find_element(*HeaderLocators().status_button_locator).click()

    def click_home_link(self):
        self.driver.find_element(*HeaderLocators().home_link_locator).click()

    def check_yandex_link(self):
        self.driver.find_element(*HeaderLocators().yandex_link_locator).click()
        child_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(child_window)
        self.wait_for_element_displayed([By.XPATH, "//button[text()='Найти']"])
        assert 'dzen.ru' in self.driver.current_url

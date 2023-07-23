from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.common_locators import HeaderLocators
from locators.main_page_locators import order_button


class CommonElements:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_displayed(self, element):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(element))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

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

    def close_all_tabs(self):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            self.driver.close()




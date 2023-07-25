from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_displayed(self, element):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(element))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def close_all_tabs(self):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            self.driver.close()

    def check_element_is_displayed(self, by, xpath):
        assert self.driver.find_element(by, xpath).is_displayed()

    def set_input_value(self, by, xpath, value):
        self.driver.find_element(by, xpath).send_keys(value)




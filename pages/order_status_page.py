from locators.order_status_locators import OrderStatusPageLocators
from pages.base_page import BasePage


class OrderStatusPage(BasePage):

    def check_order_is_exist(self, expected_order):
        actual_order = self.driver.find_element(*OrderStatusPageLocators.status_tracking_input_locator)\
            .get_attribute('value')
        assert expected_order == actual_order

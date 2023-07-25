from pages.main_page import MainPage
from pages.order_page import OrderPageClientDetails


class TestHeaderLinks:

    def test_yandex_link(self, driver):
        MainPage(driver).check_yandex_link()

    def test_home_link(self, driver):
        main = MainPage(driver)
        main.click_order_button()
        OrderPageClientDetails(driver).check_page_header()
        main.click_home_link()
        main.check_home_header_is_displayed()

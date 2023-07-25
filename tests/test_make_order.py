import pytest
from constants import USER_SET_1, USER_SET_2
from pages.order_page import OrderPageClientDetails, OrderPageOrderData, OrderPageSuccessModal, OrderPageConfirmModal
from pages.main_page import MainPage
from pages.order_status_page import OrderStatusPage


class TestOrder:

    @pytest.mark.parametrize("element,name,surname,address,station,phone,date,amount,color,comment",
                             [USER_SET_1, USER_SET_2])
    def test_create_order_is_successful(self, driver, element, name, surname, address, station, phone, date, amount,
                                        color,
                                        comment):
        client_data = OrderPageClientDetails(driver)
        order_data = OrderPageOrderData(driver)
        modal_confirm = OrderPageConfirmModal(driver)
        modal_success = OrderPageSuccessModal(driver)
        main = MainPage(driver)
        main.click_order_button(element)
        client_data.check_page_header()
        client_data.set_order_client_details(name, surname, address, station, phone)
        client_data.click_next_step_button()
        order_data.check_page_header()
        order_data.set_order_data(date, amount, color, comment)
        order_data.click_confirm_order_button()
        modal_confirm.check_modal_is_displayed()
        modal_confirm.click_modal_submit_button()
        modal_success.check_success_modal_is_displayed()
        order = modal_success.get_order_number()
        modal_success.click_order_status_button()
        OrderStatusPage(driver).check_order_is_exist(order)

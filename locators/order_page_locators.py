from selenium.webdriver.common.by import By


class OrderPageClientDataLocators:
    page_header_locator = By.XPATH, "//div[text()='Для кого самокат']"
    client_name_locator = By.XPATH, "//input[@placeholder='* Имя']"
    client_surname_locator = By.XPATH, "//input[@placeholder='* Фамилия']"
    client_address_locator = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    client_subway_station_locator = By.XPATH, "//input[@placeholder='* Станция метро']"
    client_subway_station_list_element_locator = By.XPATH, "//div[@class='select-search__select']//li"
    client_phone_number_locator = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    client_data_input_error_xpath = "//div[contains(@class, 'Error')][text()='{error_text}']"
    next_step_button_locator = By.XPATH, "//button[text()='Далее']"


class OrderPageDetailsLocators:
    page_header_locator = By.XPATH, "//div[text()='Про аренду']"
    date_locator = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    rent_duration_dropdown_root_locator = By.XPATH, "//div[@class='Dropdown-root']"
    rent_duration_dropdown_element_locator = By.XPATH, "//div[@class='Dropdown-menu']/div"
    order_color_label_locator = By.XPATH, "//div[text()='Цвет самоката']/..//label"
    order_comment_locator = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    previous_step_button_locator = By.XPATH, "//button[text()='Назад']"
    next_step_button_locator = By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']"


class OrderConfirmModalLocators:
    modal_header_locator = By.XPATH, "//div[text()='Хотите оформить заказ?']"
    modal_submit_button_locator = By.XPATH, "//button[text()='Да']"
    modal_back_button_locator = By.XPATH, "//button[text()='Нет']"


class OrderSuccessModalLocators:
    modal_message_container_locator = By.XPATH, "//div[contains(text(), 'Заказ оформлен')]"
    modal_message_locator = By.XPATH, "//div[contains(@class, 'Order_Text')]"
    modal_check_status_button_locator = By.XPATH, "//button[text()='Посмотреть статус']"

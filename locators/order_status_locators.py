from selenium.webdriver.common.by import By


class OrderStatusPageLocators:
    status_tracking_input_locator = By.XPATH, "//input[contains(@class, 'Track')]"
    status_check_button_locator = By.XPATH, "//button[text()='Посмотреть']"

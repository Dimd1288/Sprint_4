from selenium.webdriver.common.by import By


class HeaderLocators:
    order_button_locator = By.XPATH, "//div[contains(@class, 'Header')]//button[text()='Заказать']"
    status_button_locator = By.XPATH, "//div[contains(@class, 'Header')]//button[text()='Статус заказа']"
    home_link_locator = By.XPATH, "//div[contains(@class,'Header')]//a[@href='/']"
    yandex_link_locator = By.XPATH, "//div[contains(@class,'Header')]//a[@href='//yandex.ru']"

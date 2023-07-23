from selenium.webdriver.common.by import By

home_header = By.XPATH, "//div[contains(text(),'Самокат') and contains(@class, 'Home_Header')]"
questions_header = By.XPATH, "//div[text()='Вопросы о важном']"
question_xpath = "//div[@class='accordion__button'][text()='{question}']"
answer_xpath = question_xpath + "/../following-sibling::div//p"
order_button = By.XPATH, "//div[contains(@class, 'RoadMap')]//button[text()='Заказать']"

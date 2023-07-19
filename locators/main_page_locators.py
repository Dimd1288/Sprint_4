from selenium.webdriver.common.by import By

questions_header = By.XPATH, "//div[text()='Вопросы о важном']"
question_locator = "//div[@class='accordion__button'][text()='{question}']"
answer_locator = question_locator + "/../following-sibling::div//p"

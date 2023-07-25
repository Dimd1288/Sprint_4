import pytest
from selenium import webdriver
from constants import MAIN_URL


@pytest.fixture(scope="class")
def cls_driver(request):
    driver = webdriver.Firefox()
    request.cls.driver = driver
    driver.get(MAIN_URL)
    yield
    driver.quit()


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(MAIN_URL)
    yield driver
    driver.quit()

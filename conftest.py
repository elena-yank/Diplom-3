import pytest
from selenium import webdriver

from data import Credentials, Url
from locators.base_locators import BaseLocators
from pages.base_page import BasePage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(Url.MAIN_SITE)
    elif request.param == "firefox":
        browser = webdriver.Firefox()
        browser.maximize_window()
        browser.get(Url.MAIN_SITE)
    yield browser
    browser.quit()


@pytest.fixture
def authorize(driver):
    base_page = BasePage(driver)
    base_page.wait_for_element_hide(BaseLocators.OVERLAY)

    driver.find_element(*BaseLocators.BUTTON_ENTER_ACCOUNT).click()
    driver.find_element(*BaseLocators.INPUT_EMAIL).send_keys(Credentials.EMAIL)
    driver.find_element(*BaseLocators.INPUT_PASSWORD).send_keys(Credentials.PASSWORD)
    driver.find_element(*BaseLocators.BUTTON_LOGIN).click()
    return driver
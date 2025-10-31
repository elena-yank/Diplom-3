from selenium.webdriver.common.by import By


class AccountLocators:
    BUTTON_PERSONAL_ACCOUNT = [By.XPATH, "//p[text()='Личный Кабинет']"]
    LINK_ORDER_HISTORY = [By.XPATH, "//a[@href='/account/order-history' and text()='История заказов']"]
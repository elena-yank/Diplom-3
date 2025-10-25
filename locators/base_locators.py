from selenium.webdriver.common.by import By


class BaseLocators:
    INPUT_EMAIL = [By.XPATH, "//input[@name='name']"]
    INPUT_PASSWORD = [By.XPATH, "//input[@name='Пароль']"]
    BUTTON_LOGIN = [By.XPATH, "//button[text()='Войти']"]
    BUTTON_ENTER_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")
    BUTTON_PLACE_ORDER = [By.XPATH, "//button[text()='Оформить заказ']"]
    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
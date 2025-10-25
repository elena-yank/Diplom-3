from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_CONSTRUCTOR = [By.XPATH, "//p[text()='Конструктор']"]
    BUTTON_FEED = [By.XPATH, "//p[text()='Лента Заказов']"]
    INGREDIENT_BUN = [By.XPATH, "//img[@alt='Краторная булка N-200i']"]
    HEADER_DETAIL_INGREDIENT = [By.XPATH, "//h2[text()='Детали ингредиента']"]
    BUTTON_CLOSE = [By.XPATH,"//button[contains(@class, 'modal__close')]"]
    TAB_TOPPING = [By.XPATH, "//span[text()='Начинки']"]
    SECTION_BASKET = [By.XPATH,'//section[contains(@class, "BurgerConstructor_basket")]']
    COUNTER_BUN = [By.XPATH,'(//p[contains(@class, "counter_counter__num__3nue1")])[2]']
    BUTTON_ORDER = [By.XPATH,"//button[text()='Оформить заказ']"]
    HEADER_ID_ORDER = [By.XPATH,"//h2[contains(@class, 'Modal_modal__title')]"]
    ORDER_NUMBER = [By.XPATH, "//h2[contains(@class, 'Modal_modal__title') and contains(@class, 'text_type_digits-large')]"]
import allure

from locators.account_locators import AccountLocators
from locators.base_locators import BaseLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


@allure.step("Работа с главной страницей приложения")
class MainPage(BasePage):

    @allure.step("Открытие личного кабинета")
    def open_personal_account(self):
        locator = AccountLocators.BUTTON_PERSONAL_ACCOUNT
        self._wait_and_click(locator)

    @allure.step("Переход к конструктору")
    def go_to_constructor(self):
        locator = MainPageLocators.BUTTON_CONSTRUCTOR
        self._wait_and_click(locator)

    @allure.step("Переход к ленте заказов")
    def go_to_feed(self):
        locator = MainPageLocators.BUTTON_FEED
        self._wait_and_click(locator)

    @allure.step("Возврат к конструктору")
    def return_to_constructor(self):
        self.go_to_constructor()

    @allure.step("Клик по ингредиенту")
    def click_ingredient(self):
        locator = MainPageLocators.INGREDIENT_BUN
        self._wait_and_click(locator)

    @allure.step("Получение заголовка модального окна")
    def get_modal_title(self):
        return self.get_text_on_element(MainPageLocators.HEADER_DETAIL_INGREDIENT)

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        locator = MainPageLocators.BUTTON_CLOSE
        self._wait_and_click(locator)

    @allure.step("Получение текста активной вкладки")
    def get_active_tab_text(self):
        return self.get_text_on_element(MainPageLocators.TAB_TOPPING)

    @allure.step("Добавление ингредиента в заказ")
    def add_ingredient_to_order(self):
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        ingredient = self.wait_for_element(MainPageLocators.INGREDIENT_BUN)
        basket = self.wait_for_element(MainPageLocators.SECTION_BASKET)
        self.drag_and_drop_element(ingredient, basket)

    @allure.step("Получение значения счетчика ингредиента")
    def get_ingredient_counter(self):
        return self.get_text_on_element(MainPageLocators.COUNTER_BUN)

    @allure.step("Оформление заказа")
    def submit_order(self):
        locator = MainPageLocators.BUTTON_ORDER
        self._wait_and_click(locator)

    @allure.step("Закрытие модального окна заказа")
    def close_order_modal(self):
        self._wait_and_click(MainPageLocators.BUTTON_CLOSE)

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        # Ждем появления элемента с номером заказа
        self.wait_for_element_visibility_with_custom_timeout(MainPageLocators.ORDER_NUMBER)

        # Ждем, пока номер заказа обновится (пока не будет равен "9999")
        self.wait_for_text_to_be_present_in_element(MainPageLocators.ORDER_NUMBER, "9999")

        # Получаем текст элемента с номером заказа
        return self.get_text_on_element(MainPageLocators.ORDER_NUMBER)

    @allure.step("Проверка текущей страницы")
    def is_current_page(self, expected_url):
        return self.check_url(expected_url)

    def _wait_and_click(self, locator):
        """Вспомогательный метод для ожидания и клика по элементу"""
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        self.wait_for_element_to_be_clickable(locator)
        self.click_on_element(locator)

    @allure.step("Ожидание закрытия модального окна с номером заказа")
    def wait_for_order_modal_close(self):
        self.wait_until_element_invisible(MainPageLocators.ORDER_NUMBER)
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.order_feed_locators import OrderFeedLocators
from locators.account_locators import AccountLocators
from locators.base_locators import BaseLocators
from pages.base_page import BasePage


@allure.step("Работа со страницей ленты заказов")
class FeedPage(BasePage):

    @allure.step("Открытие ленты заказов")
    def open_feed(self):
        locator = OrderFeedLocators.BUTTON_FEED
        self._wait_and_click(locator)

    @allure.step("Получение текста модального окна")
    def get_modal_text(self):
        return self.get_text_on_element(OrderFeedLocators.HEADER_COMPOSITION)

    @allure.step("Проверка отображения модального окна")
    def is_modal_displayed(self):
        return self.wait_for_element_is_displayed(OrderFeedLocators.MODAL_ORDER_WINDOW)

    @allure.step("Переход в историю заказов")
    def go_to_order_history(self):
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(AccountLocators.BUTTON_PERSONAL_ACCOUNT))
        self.click_on_element(AccountLocators.BUTTON_PERSONAL_ACCOUNT)
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(AccountLocators.LINK_ORDER_HISTORY))
        self.click_on_element(AccountLocators.LINK_ORDER_HISTORY)

    @allure.step("Получение номера заказа из истории")
    def get_order_number_from_history(self):
        locator = OrderFeedLocators.ORDER_NUM_HISTORY
        self.wait_for_element(locator)
        return self.find_element(locator).text

    @allure.step("Получение номера заказа в ленте")
    def get_feed_order_number(self):
        locator = OrderFeedLocators.ORDER_NUMBER_FEED
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        return self.get_text_on_element(locator)

    @allure.step("Получение общего количества заказов")
    def get_total_orders_count(self):
        return self.get_text_on_element(OrderFeedLocators.COUNTER_ALL_ORDERS)

    @allure.step("Получение количества заказов за сегодня")
    def get_today_orders_count(self):
        return self.get_text_on_element(OrderFeedLocators.COUNTER_TODAY_ORDERS)

    @allure.step("Получение номера созданного заказа")
    def get_created_order_number(self):
        locator = OrderFeedLocators.HEADER_ORDER_CREATE_NUM
        self.get_order_number(OrderFeedLocators.MODAL_ORDER)
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        return self.get_text_on_element(locator)

    @allure.step("Получение списка заказов в работе")
    def get_orders_in_work(self):
        orders_text = self.get_text_on_element(OrderFeedLocators.ORDER_IN_WORK)
        # Убираем ведущие нули из номеров заказов
        return ''.join(orders_text).lstrip('0')

    def _wait_and_click(self, locator):
        """Вспомогательный метод для ожидания и клика по элементу"""
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.click_on_element(locator)

    @allure.step("Ожидание закрытия модального окна с номером заказа")
    def wait_for_order_modal_close(self):
        self.wait_until_element_invisible(OrderFeedLocators.MODAL_ORDER)
import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage


@allure.suite("Лента заказов")
@allure.feature("Статистика и отслеживание заказов")
class TestOrderFeed:

    @allure.title("Обновление счетчика 'Выполнено за всё время' при создании заказа")
    @allure.description("Проверяем, что счетчик 'Выполнено за всё время' увеличивается при создании нового заказа")
    def test_total_orders_counter_increases(self, authorize, driver):
        driver = authorize
        feed_page = FeedPage(driver)
        feed_page.open_feed()
        initial_count = feed_page.get_total_orders_count()
        main_page = MainPage(driver)
        main_page.return_to_constructor()
        main_page.add_ingredient_to_order()
        main_page.submit_order()
        main_page.close_order_modal()
        main_page.wait_for_order_modal_close()
        feed_page.open_feed()
        updated_count = feed_page.get_total_orders_count()
        assert updated_count >= initial_count

    @allure.title("Обновление счетчика 'Выполнено за сегодня' при создании заказа")
    @allure.description("Проверяем, что счетчик 'Выполнено за сегодня' увеличивается при создании нового заказа")
    def test_daily_orders_counter_increases(self, authorize, driver):
        driver = authorize
        feed_page = FeedPage(driver)
        feed_page.open_feed()
        initial_count = feed_page.get_today_orders_count()
        main_page = MainPage(driver)
        main_page.return_to_constructor()
        main_page.add_ingredient_to_order()
        main_page.submit_order()
        main_page.close_order_modal()
        main_page.wait_for_order_modal_close()
        feed_page.open_feed()
        updated_count = feed_page.get_today_orders_count()
        assert updated_count >= initial_count

    @allure.title("Отображение номера заказа в разделе 'В работе'")
    @allure.description("Проверяем, что номер созданного заказа отображается в разделе 'В работе'")
    def test_order_appears_in_work_section(self, authorize, driver):
        driver = authorize
        main_page = MainPage(driver)
        main_page.return_to_constructor()
        main_page.add_ingredient_to_order()
        main_page.submit_order()
        order_number = main_page.get_order_number()
        main_page.close_order_modal()
        main_page.wait_for_order_modal_close()
        feed_page = FeedPage(driver)
        feed_page.open_feed()
        orders_in_work = feed_page.get_orders_in_work()
        assert order_number in orders_in_work
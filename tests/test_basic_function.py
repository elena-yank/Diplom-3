import allure
from data import TextAssert, Url
from pages.main_page import MainPage

@allure.suite("Основной функционал приложения")
@allure.feature("Навигация и взаимодействие с элементами")
class TestMainFunctionality:

    @allure.title("Переход на страницу конструктора через навигацию")
    @allure.description("Проверяем, что при клике на 'Конструктор' осуществляется переход на главную страницу")
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_constructor()
        assert main_page.is_current_page(Url.MAIN_SITE)

    @allure.title("Переход к ленте заказов")
    @allure.description("Проверяем, что при клике на 'Лента заказов' осуществляется переход на страницу ленты заказов")
    def test_navigate_to_feed(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_feed()
        assert main_page.is_current_page(Url.FEED_URL)

    @allure.title("Открытие деталей ингредиента")
    @allure.description("Проверяем, что при клике на ингредиент открывается модальное окно с деталями")
    def test_open_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        modal_title = main_page.get_modal_title()
        assert TextAssert.TEXT_DETAIL_WINDOW in modal_title and Url.INGREDIENT_URL in driver.current_url

    @allure.title("Закрытие модального окна через кнопку закрытия")
    @allure.description("Проверяем, что модальное окно с деталями ингредиента закрывается при клике на крестик")
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.close_modal()
        tab_text = main_page.get_active_tab_text()
        assert TextAssert.TEXT_CLOSE_WINDOW in tab_text

    @allure.title("Увеличение счетчика ингредиента при добавлении в заказ")
    @allure.description("Проверяем, что счетчик ингредиента увеличивается при его добавлении в заказ")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.add_ingredient_to_order()
        counter_value = main_page.get_ingredient_counter()
        assert TextAssert.TEXT_COUNTER in counter_value
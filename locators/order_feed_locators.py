from selenium.webdriver.common.by import By


class OrderFeedLocators:
    BUTTON_FEED = [By.XPATH, "//p[text()='Лента Заказов']"]
    ORDER_IN_FEED = [By.XPATH, "// li[contains( @class , 'OrderHistory_listItem')][1]" ]
    HEADER_COMPOSITION = [By.XPATH, "//p [text() ='Cостав']"]
    MODAL_ORDER_WINDOW = [By.XPATH, ".//div[contains(@class, 'Modal_orderBox')]"]
    ORDER_NUMBER_FEED = [By.XPATH,"//p[@class= 'text text_type_digits-default'][1]"]
    ORDER_NUM_HISTORY = [By.XPATH, '//li[last()]//p[@class="text text_type_digits-default"]']
    COUNTER_ALL_ORDERS = [By.XPATH,'//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class, "OrderFeed_number")]']
    COUNTER_TODAY_ORDERS = [By.XPATH,'.//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class, "OrderFeed_number")]']
    HEADER_ORDER_CREATE_NUM = [By.XPATH,'//h2[contains(@class,"Modal_modal__title_shadow__3ikwq")]']
    ORDER_IN_WORK = [By.XPATH, '//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]//li[contains(@class,"text text_type_digits-default")]']
    MODAL_ORDER = [By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4"]
class Url:
    MAIN_SITE = 'https://stellarburgers.education-services.ru/'
    LOGIN_URL = f'{MAIN_SITE}login'
    ACCOUNT_URL = f'{MAIN_SITE}account/profile'
    FORGOT_PASS_URL = f'{MAIN_SITE}forgot-password'
    RESET_PASS_URL = f'{MAIN_SITE}reset-password'
    ORDER_HISTORY_URL = f'{MAIN_SITE}account/order-history'
    FEED_URL = f'{MAIN_SITE}feed'
    INGREDIENT_URL = f'{MAIN_SITE}ingredient/'

class Credentials:
    EMAIL='elena.yank@yahoo.com'
    PASSWORD='toeiti50ak'

class TextAssert:
    TEXT_DETAIL_WINDOW = "Детали ингредиента"
    TEXT_CLOSE_WINDOW = "Начинки"
    TEXT_COUNTER = "2"
    TEXT_ID_ORDER = "идентификатор заказа"
    TEXT_OPEN_WINDOW = "Cостав"
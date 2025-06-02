from selenium.webdriver.common.by import By

class Locators:
    # Регистрация

    # Главная страница
    LOGIN_MAIN_BUTTON = (By.XPATH, "//button[contains(@class,'button_button_type_primary') and text()='Войти в аккаунт']")
    PROFILE_BTN = (By.XPATH, "//p[text()='Личный Кабинет']")

    # Страница логина
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name' or @name='email' or @name='Email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")

    # Ссылка "Войти" на формах регистрации и восстановления
    LOGIN_LINK = (By.LINK_TEXT, "Войти")

    # Кнопка показать/скрыть пароль
    SHOW_PASSWORD = (By.XPATH, "//div[contains(@class,'input__icon-action')]")

    # Конструктор
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
    ACTIVE_TAB = (By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc")

    # Списки заказов
    ORDER_CARD = (By.XPATH, "//a[contains(@href, '/feed/')]")
    ORDER_HISTORY_CARD = (By.XPATH, "//div[contains(@class, 'OrderHistory_dataBox')]")
    IN_WORK_HEADER = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul/li")

    ORDER_ID_TEXT = (By.XPATH, "//p[contains(text(),'идентификатор заказа')]")

    # Счётчики
    TOTAL_DONE = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'text_type_digits-large')]")
    TODAY_DONE = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'text_type_digits-large')]")

    # Сообщение о готовности всех заказов
    ALL_READY_TEXT = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(text(), 'Все текущие заказы готовы')]")

    # Любой номер заказа
    ORDER_NUMBER_LI = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]/li[contains(@class,'text_type_digits-default')]")

    ORDER_MODAL = (By.XPATH, "//div[contains(@class,'Modal_orderBox__')]")

    # Кнопка закрытия модального окна
    MODAL_CLOSE_BTN = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    # Восстановление пароля
    #FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Войти")
    #FORGOT_PASSWORD_EMAIL_INPUT = (By.NAME, "name")
    #FORGOT_PASSWORD_SUBMIT = (By.XPATH, "//button[text()='Восстановить']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password' and contains(text(),'Восстановить пароль')]")
    FORGOT_PASSWORD_EMAIL_INPUT = (By.NAME, "name")
    FORGOT_PASSWORD_SUBMIT = (By.XPATH, "//button[text()='Восстановить']")


    CONSTRUCTOR_BTN = (By.XPATH, '//p[text()="Конструктор"]')
    FEED_BTN = (By.XPATH, '//a[@href="/feed"]')

    INGREDIENT = (By.XPATH, "//a[starts-with(@class, 'BurgerIngredient_ingredient')]")

    # Первый ингредиент (будет и булка, если она первая в списке)
    FIRST_INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')][1]")

    # Первая булка (по alt-атрибуту, надёжнее)
    FIRST_BUN = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]//img[contains(@alt, 'булка')]/ancestor::a")

    # Локатор для списка ингредиентов
    INGREDIENTS_LIST = (By.CLASS_NAME, "BurgerIngredients_ingredients__list__2A-mT")

    # Счётчик количества ингредиентов на иконке
    INGREDIENT_COUNTER = (By.CLASS_NAME, "counter_counter__num__3nue1")

    # Область конструктора для дропа ингредиента
    CONSTRUCTOR_DROPZONE = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_constructor__') or contains(@class,'BurgerConstructor_basket__')]")

    # Кнопка "Оформить заказ"
    PLACE_ORDER_BTN = (By.XPATH, "//button[contains(text(), 'Оформить заказ') and contains(@class, 'button_button_type_primary')]")

    # Модалка заказа - ищем по крупному номеру заказа
    ORDER_SUCCESS_MODAL = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title__2L34m')]")
    ORDER_SUCCESS_TEXT = (By.XPATH, "//p[contains(text(),'идентификатор заказа')]")

    # Модалка ингредиента
    INGREDIENT_MODAL = (By.XPATH, "//h2[text()='Детали ингредиента']/ancestor::div[contains(@class,'Modal_modal__contentBox')]")

    # Кнопка закрытия модалки
    MODAL_CLOSE_BTN = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")

    # Кнопка "Выход" в профиле
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    # Таб "История заказов" (вкладка в профиле)
    ORDER_HISTORY_TAB = (By.XPATH, "//a[contains(@href, '/account/order-history')]")

    # Локаторы страницы регистрации
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    ERROR_PASSWORD = (By.XPATH, "//p[contains(@class, 'input__error') and contains(text(), 'Некорректный пароль')]")

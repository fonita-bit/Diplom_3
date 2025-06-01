
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
import allure
from pages.main_page import MainPage

from utils.locators import Locators
from utils.urls import URLs


@allure.title("Переход по клику на 'Конструктор'")
def test_constructor_tab(driver):
    driver.get(URLs.MAIN_PAGE)
    page = MainPage(driver)
    page.click(Locators.CONSTRUCTOR_BTN)
    assert driver.current_url.endswith("/")

@allure.title("Переход по клику на 'Лента заказов'")
def test_feed_tab_click(driver):
    driver.get(URLs.MAIN_PAGE)
    # Ждём пока кнопка появится
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.FEED_BTN))
    driver.find_element(*Locators.FEED_BTN).click()
    WebDriverWait(driver, 10).until(EC.url_contains('/feed'))
    assert '/feed' in driver.current_url

@allure.title("Открытие и закрытие окна ингредиента")
def test_ingredient_modal_open_close(driver):
    driver.get(URLs.MAIN_PAGE)
    ingredient = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.FIRST_INGREDIENT)
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", ingredient)
    ActionChains(driver).move_to_element(ingredient).click().perform()

    # Ждём открытия модалки
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.INGREDIENT_MODAL)
    )
    assert driver.find_element(*Locators.INGREDIENT_MODAL).is_displayed()

    # Закрываем модалку
    close_btn = driver.find_element(*Locators.MODAL_CLOSE)
    close_btn.click()
    # Ждём, что модалка исчезла
    WebDriverWait(driver, 5).until(
        EC.invisibility_of_element_located(Locators.INGREDIENT_MODAL)
    )


@allure.title("Drag-and-drop ингредиента увеличивает его счетчик")
def test_drag_and_drop_ingredient_increases_counter(driver):
    driver.get(URLs.MAIN_PAGE)

    # Дожидаемся, пока список ингредиентов прогрузится
    ingredients_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.INGREDIENTS_LIST)
    )

    # Берём первый ингредиент (или нужный тебе)
    ingredient = driver.find_element(*Locators.FIRST_INGREDIENT)

    # Сохраняем текущее значение счетчика
    counter_elem = ingredient.find_element(*Locators.INGREDIENT_COUNTER)
    count_before = int(counter_elem.text)

    # Находим область конструктора (куда перетаскивать)
    constructor_area = driver.find_element(*Locators.CONSTRUCTOR_DROPZONE)

    # Drag and drop!
    actions = ActionChains(driver)
    actions.click_and_hold(ingredient).move_to_element(constructor_area).release().perform()

    # Явное ожидание обновления счетчика
    WebDriverWait(driver, 5).until(
        lambda d: int(d.find_element(*Locators.FIRST_INGREDIENT)
                      .find_element(*Locators.INGREDIENT_COUNTER).text) > count_before
    )

    # Проверяем, что счетчик увеличился
    count_after = int(driver.find_element(*Locators.FIRST_INGREDIENT)
                      .find_element(*Locators.INGREDIENT_COUNTER).text)
    assert count_after == count_before + 2 or count_after == count_before + 1

@allure.title("Залогиненный пользователь может оформить заказ")
def test_authorized_user_can_make_order(logged_in_user):
    driver = logged_in_user

    # Добавляем булку
    bun = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.FIRST_BUN)
    )
    dropzone = driver.find_element(*Locators.CONSTRUCTOR_DROPZONE)
    ActionChains(driver).drag_and_drop(bun, dropzone).perform()

    # Добавляем начинку (или соус)
    ingredient = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.FIRST_INGREDIENT)
    )
    ActionChains(driver).drag_and_drop(ingredient, dropzone).perform()

    # Кликаем "Оформить заказ"
    order_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.PLACE_ORDER_BTN)
    )
    order_btn.click()

    # Проверяем, что появилось модальное окно с номером заказа
    success_modal = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located(Locators.ORDER_SUCCESS_MODAL)
    )
    assert success_modal.is_displayed()
    order_text = driver.find_element(*Locators.ORDER_ID_TEXT)
    assert "идентификатор заказа" in order_text.text
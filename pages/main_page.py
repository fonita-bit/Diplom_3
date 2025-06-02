import allure

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.locators import Locators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_BTN)
        ).click()

    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_feed(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.FEED_BTN)
        ).click()

    @allure.step("Открытие модального окна ингредиента")
    def open_ingredient_modal(self):
        ingredient = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.FIRST_INGREDIENT)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ingredient)
        ActionChains(self.driver).move_to_element(ingredient).click().perform()

    @allure.step("Закрытие модального окна ингредиента")
    def close_ingredient_modal(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.MODAL_CLOSE_BTN)
        ).click()

    @allure.step("Модалка ингредиента отображается")
    def is_ingredient_modal_visible(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(Locators.INGREDIENT_MODAL)
            )
            return True
        except:
            return False

    @allure.step("Получение значения счётчика первого ингредиента")
    def get_first_ingredient_count(self):
        try:
            ingredient = self.driver.find_element(*Locators.FIRST_INGREDIENT)
            counter = ingredient.find_element(*Locators.INGREDIENT_COUNTER)
            return int(counter.text)
        except:
            return 0

    @allure.step("Перетаскивание первого ингредиента в конструктор")
    def drag_first_ingredient_to_constructor(self):
        ingredient = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Locators.FIRST_INGREDIENT)
        )
        constructor_area = self.driver.find_element(*Locators.CONSTRUCTOR_DROPZONE)
        ActionChains(self.driver).drag_and_drop(ingredient, constructor_area).perform()

    @allure.step("Перетаскивание булки в конструктор")
    def drag_bun_to_constructor(self):
        bun = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Locators.FIRST_BUN)
        )
        dropzone = self.driver.find_element(*Locators.CONSTRUCTOR_DROPZONE)
        ActionChains(self.driver).drag_and_drop(bun, dropzone).perform()

    @allure.step("Оформить заказ")
    def place_order(self):
        order_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.PLACE_ORDER_BTN)
        )
        order_btn.click()

    @allure.step("Успешное оформление заказа")
    def is_order_success_visible(self):
        modal = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(Locators.ORDER_SUCCESS_MODAL)
        )
        text = self.driver.find_element(*Locators.ORDER_ID_TEXT).text
        return modal.is_displayed() and "идентификатор заказа" in text

    @allure.step("Закрытие модального окна ингредиента")
    def close_ingredient_modal(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.MODAL_CLOSE_BTN)
        ).click()

        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(Locators.INGREDIENT_MODAL)
        )
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import Locators
from pages.base_page import BasePage

class MainPage(BasePage):
    def click_constructor(self):
        self.driver.find_element(*Locators.CONSTRUCTOR_LINK).click()
    def click_feed(self):
        self.driver.find_element(*Locators.FEED_LINK).click()
    def click(self, locator):
        self.driver.find_element(*locator).click()

    def open_ingredient_modal(self):
        # Ждем появления ингредиентов, берём первый и кликаем
        ingredient = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.INGREDIENT)
        )
        ingredient.click()

    def close_ingredient_modal(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(Locators.MODAL_CLOSE_BTN)
        ).click()

    def is_visible(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False

    def click(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
    def open_ingredient_modal(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.FIRST_INGREDIENT)
        )
        self.driver.find_element(*Locators.FIRST_INGREDIENT).click()

    def close_ingredient_modal(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.MODAL_CLOSE_BTN)
        )
        self.driver.find_element(*Locators.MODAL_CLOSE_BTN).click()

    def is_visible(self, locator):
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(locator)
            )
        except:
            return False

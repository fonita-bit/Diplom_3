import allure
from utils.locators import Locators
from pages.base_page import BasePage
from utils.urls import URLs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage(BasePage):

    @allure.step("Переход в профиль")
    def go_to_profile(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.PROFILE_BTN)
        ).click()

    @allure.step("Переход в историю заказов")
    def go_to_order_history(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.ORDER_HISTORY_TAB)
        ).click()

    @allure.step("Выход из профиля")
    def logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(URLs.LOGIN_PAGE)
        )
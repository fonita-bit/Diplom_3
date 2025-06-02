import allure

from utils.locators import Locators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.urls import URLs


class RegistrationPage(BasePage):

    @allure.step("Ввод имени: {name}")
    def set_name(self, name):
        self.driver.find_element(*Locators.NAME_INPUT).send_keys(name)

    @allure.step("Ввод email: {email}")
    def set_email(self, email):
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)

    @allure.step("Ввод пароля")
    def set_password(self, password):
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)

    @allure.step("Отправка формы регистрации")
    def submit(self):
        self.driver.find_element(*Locators.REGISTER_BUTTON).click()

    @allure.step("Проверка ошибки пароля")
    def is_password_error_visible(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(Locators.ERROR_PASSWORD)
        ).is_displayed()

    @allure.step("Редирект на страницу логина")
    def is_redirected_to_login(self):
        return WebDriverWait(self.driver, 10).until(
            EC.url_contains(URLs.LOGIN_PAGE)
        )

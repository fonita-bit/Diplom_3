import allure
from utils.locators import Locators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    @allure.step("Заполнение email: {email}")
    def set_email(self, email):
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)

    @allure.step("Заполнение пароля")
    def set_password(self, password):
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)

    @allure.step("Отправка формы логина")
    def submit(self):
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()

    @allure.step("Показать/скрыть пароль")
    def show_password(self):
        self.driver.find_element(*Locators.SHOW_PASSWORD).click()

    @allure.step("Получить элемент поля пароля")
    def get_password_input_element(self):
        return self.driver.find_element(*Locators.PASSWORD_INPUT)

    @allure.step("Переход и логин с главной страницы")
    def go_and_login_from_main(self, email, password):
        self.go("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(*Locators.LOGIN_MAIN_BUTTON).click()
        self.set_email(email)
        self.set_password(password)
        self.submit()
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

    @allure.step("Переход и логин через кнопку 'Личный кабинет'")
    def go_and_login_from_profile(self, email, password):
        self.go("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(*Locators.PROFILE_BTN).click()
        self.set_email(email)
        self.set_password(password)
        self.submit()
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

    @allure.step("Переход и логин через форму регистрации")
    def go_and_login_from_registration(self, email, password):
        self.go("https://stellarburgers.nomoreparties.site/register")
        self.driver.find_element(*Locators.LOGIN_LINK).click()
        self.set_email(email)
        self.set_password(password)
        self.submit()
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

    @allure.step("Переход и логин через форму восстановления пароля")
    def go_and_login_from_forgot_password(self, email, password):
        self.go("https://stellarburgers.nomoreparties.site/forgot-password")
        self.driver.find_element(*Locators.LOGIN_LINK).click()
        self.set_email(email)
        self.set_password(password)
        self.submit()
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

    @allure.step("Переход на форму восстановления пароля")
    def go_to_forgot_password_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.FORGOT_PASSWORD_LINK)
        ).click()
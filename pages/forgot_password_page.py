import allure
from utils.locators import Locators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ForgotPasswordPage(BasePage):

    @allure.step("Ввод email для восстановления: {email}")
    def set_email(self, email):
        self.driver.find_element(*Locators.FORGOT_PASSWORD_EMAIL_INPUT).send_keys(email)

    @allure.step("Нажатие на кнопку 'Восстановить'")
    def submit(self):
        self.driver.find_element(*Locators.FORGOT_PASSWORD_SUBMIT).click()

    @allure.step("Полный процесс восстановления пароля")
    def fill_and_submit(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.FORGOT_PASSWORD_EMAIL_INPUT)
        )
        self.set_email(email)
        self.submit()
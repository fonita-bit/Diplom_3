from utils.locators import Locators
from pages.base_page import BasePage

class ForgotPasswordPage(BasePage):
    def set_email(self, email):
        self.driver.find_element(*Locators.FORGOT_PASSWORD_EMAIL_INPUT).send_keys(email)
    def submit(self):
        self.driver.find_element(*Locators.FORGOT_PASSWORD_SUBMIT).click()

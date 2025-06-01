from utils.locators import Locators
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    def set_name(self, name):
        self.driver.find_element(*Locators.NAME_INPUT).send_keys(name)
    def set_email(self, email):
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    def set_password(self, password):
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    def submit(self):
        self.driver.find_element(*Locators.REGISTER_BUTTON).click()
    def error_message(self):
        return self.driver.find_element(*Locators.ERROR_PASSWORD)

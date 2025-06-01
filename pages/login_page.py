from utils.locators import Locators
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
    def set_email(self, email):
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    def set_password(self, password):
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    def submit(self):
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()
    def show_password(self):
        self.driver.find_element(*Locators.SHOW_PASSWORD).click()

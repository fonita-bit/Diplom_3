from utils.locators import Locators
from pages.base_page import BasePage

class ProfilePage(BasePage):
    def go_to_order_history(self):
        self.driver.find_element(*Locators.ORDER_HISTORY_TAB).click()
    def logout(self):
        self.driver.find_element(*Locators.LOGOUT_BUTTON).click()

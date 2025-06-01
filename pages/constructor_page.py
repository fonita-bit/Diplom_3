from utils.locators import Locators
from pages.base_page import BasePage

class ConstructorPage(BasePage):
    def switch_to_buns(self):
        self.driver.find_element(*Locators.BUNS_TAB).click()
    def switch_to_sauces(self):
        self.driver.find_element(*Locators.SAUCES_TAB).click()
    def switch_to_fillings(self):
        self.driver.find_element(*Locators.FILLINGS_TAB).click()
    def is_tab_active(self, name):
        tab = self.driver.find_element(*Locators.ACTIVE_TAB)
        return name in tab.text

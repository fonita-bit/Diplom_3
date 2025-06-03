import allure
from utils.locators import Locators
from pages.base_page import BasePage


class ConstructorPage(BasePage):

    @allure.step("Переключение на вкладку 'Булки'")
    def switch_to_buns(self):
        self.click(Locators.BUNS_TAB)

    @allure.step("Переключение на вкладку 'Соусы'")
    def switch_to_sauces(self):
        self.click(Locators.SAUCES_TAB)

    @allure.step("Переключение на вкладку 'Начинки'")
    def switch_to_fillings(self):
        self.click(Locators.FILLINGS_TAB)

    @allure.step("Проверка, что активная вкладка содержит '{name}'")
    def is_tab_active(self, name):
        tab = self.get_text(Locators.ACTIVE_TAB)
        return name in tab
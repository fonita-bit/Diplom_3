import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.locators import Locators
from pages.base_page import BasePage


class FeedPage(BasePage):

    @allure.step("Клик по первому заказу в ленте")
    def click_first_order(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.ORDER_CARD)
        )
        self.driver.find_element(*Locators.ORDER_CARD).click()

    @allure.step("Открыт модалка заказа")
    def order_modal_is_open(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.ORDER_MODAL)
        ).is_displayed()

    @allure.step("Есть заказы в ленте")
    def is_visible_order_card(self):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.ORDER_CARD)
            ).is_displayed()
        except:
            return False

    @allure.step("Счётчик 'Выполнено за все время'")
    def get_total_done_count(self):
        text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.TOTAL_DONE)
        ).text
        return int(text.replace(" ", ""))

    @allure.step("Счётчик 'Выполнено за сегодня'")
    def get_today_done_count(self):
        text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.TODAY_DONE)
        ).text
        return int(text.replace(" ", ""))

    @allure.step("Проверка, что заказ появился в разделе 'В работе'")
    def is_order_in_work(self):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.IN_WORK_HEADER)
            ).is_displayed()
        except:
            return False
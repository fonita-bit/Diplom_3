from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import Locators

class FeedPage(BasePage):
    def open_order_details(self):
        # Лучше: дождись, что элемент существует и кликабелен
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        order = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.ORDER_CARD)
        )
        order.click()
    def click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def open_order_modal(self):
        self.driver.find_element(*Locators.ORDER_CARD).click()

    def click_first_order(self):
        # Дождись, что первый заказ появился
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.ORDER_CARD)
        )
        self.driver.find_element(*Locators.ORDER_CARD).click()
    def order_modal_is_open(self):
        # Дождись, что модалка появилась
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.ORDER_MODAL)
        )
    def is_visible(self, locator):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            ).is_displayed()
        except:
            return False
    def get_text(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        ).text

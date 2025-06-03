import allure
import pytest

from pages.main_page import MainPage
from utils.urls import URLs


@allure.suite("Order Functionality")
class TestOrderFunctionality:

    @allure.title("Переход по клику на 'Конструктор'")
    def test_constructor_tab(self, driver):
        page = MainPage(driver)
        page.go(URLs.MAIN_PAGE)
        page.click_constructor()
        assert page.get_current_url().endswith("/")

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_feed_tab_click(self, driver):
        page = MainPage(driver)
        page.go(URLs.MAIN_PAGE)
        page.click_feed()
        assert "/feed" in page.get_current_url()

    @allure.title("Открытие и закрытие окна ингредиента")
    def test_ingredient_modal_open_close(self, driver):
        page = MainPage(driver)
        page.go(URLs.MAIN_PAGE)
        page.open_ingredient_modal()
        assert page.is_ingredient_modal_visible()
        page.close_ingredient_modal()
        assert not page.is_ingredient_modal_visible()

    @allure.title("Drag-and-drop ингредиента увеличивает его счетчик")
    def test_drag_and_drop_ingredient_increases_counter(self, driver):
        page = MainPage(driver)
        page.go(URLs.MAIN_PAGE)
        count_before = page.get_first_ingredient_count()
        page.drag_first_ingredient_to_constructor()
        count_after = page.get_first_ingredient_count()
        assert count_after > count_before

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_authorized_user_can_make_order(self, logged_in_user):
        page = MainPage(logged_in_user)
        page.go(URLs.MAIN_PAGE)
        page.drag_bun_to_constructor()
        page.drag_first_ingredient_to_constructor()
        page.place_order()
        assert page.is_order_success_visible()

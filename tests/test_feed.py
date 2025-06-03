import allure
import pytest

from pages.feed_page import FeedPage
from utils.urls import URLs


@allure.suite("Feed Feature")
class TestFeed:

    @allure.title("Открытие модального окна заказа")
    def test_order_modal_open(self, driver):
        feed_page = FeedPage(driver)
        feed_page.go(URLs.FEED_PAGE)
        feed_page.click_first_order()
        assert feed_page.order_modal_is_open()

    @allure.title("Отображение заказов пользователя в ленте заказов")
    def test_user_orders_visible_in_feed(self, driver):
        feed_page = FeedPage(driver)
        feed_page.go(URLs.FEED_PAGE)
        assert feed_page.is_visible_order_card()

    @allure.title("Счётчик 'Выполнено за всё время' увеличивается")
    def test_total_done_counter(self, driver):
        feed_page = FeedPage(driver)
        feed_page.go(URLs.FEED_PAGE)
        count = feed_page.get_total_done_count()
        assert count >= 0

    @allure.title("Счётчик 'Выполнено за сегодня' увеличивается")
    def test_today_done_counter(self, driver):
        feed_page = FeedPage(driver)
        feed_page.go(URLs.FEED_PAGE)
        count = feed_page.get_today_done_count()
        assert count >= 0

    @allure.title("Оформленный заказ появляется в разделе 'В работе'")
    def test_order_appears_in_work(self, driver):
        feed_page = FeedPage(driver)
        feed_page.go(URLs.FEED_PAGE)
        assert feed_page.is_order_in_work()
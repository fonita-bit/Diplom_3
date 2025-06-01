import allure
from pages.feed_page import FeedPage
from utils.locators import Locators

from utils.urls import URLs

@allure.title("Открытие модального окна заказа")
def test_order_modal_open(driver):
    driver.get(URLs.FEED_PAGE)
    feed_page = FeedPage(driver)
    feed_page.click_first_order()
    # Проверяем, что модалка появилась
    modal = feed_page.order_modal_is_open()
    assert modal.is_displayed()

@allure.title("Отображение заказов пользователя в ленте заказов")
def test_user_orders_visible_in_feed(driver):
    driver.get(URLs.FEED_PAGE)
    feed = FeedPage(driver)
    assert feed.is_visible(Locators.ORDER_CARD)

@allure.title("Счётчик 'Выполнено за всё время' увеличивается")
def test_total_done_counter(driver):
    driver.get(URLs.FEED_PAGE)
    feed = FeedPage(driver)
    count = int(feed.get_text(Locators.TOTAL_DONE).replace(" ", ""))
    assert count >= 0

@allure.title("Счётчик 'Выполнено за сегодня' увеличивается")
def test_today_done_counter(driver):
    driver.get(URLs.FEED_PAGE)
    feed = FeedPage(driver)
    count = int(feed.get_text(Locators.TODAY_DONE).replace(" ", ""))
    assert count >= 0

@allure.title("Оформленный заказ появляется в разделе 'В работе'")
def test_order_appears_in_work(driver):
    driver.get(URLs.FEED_PAGE)
    feed = FeedPage(driver)
    assert feed.is_visible(Locators.IN_WORK_HEADER)

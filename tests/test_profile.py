import allure
from utils.urls import URLs
from data.test_user import USER
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import Locators

@allure.title("Go to profile via profile button")
def test_navigate_to_profile(driver):
    page = LoginPage(driver)
    page.go(URLs.LOGIN_PAGE)
    page.set_email(USER["email"])
    page.set_password(USER["password"])
    page.submit()
    WebDriverWait(driver, 10).until(EC.url_to_be(URLs.MAIN_PAGE))
    driver.find_element(*Locators.PROFILE_BTN).click()
    assert "/account" in driver.current_url

@allure.title("Go to order history tab in profile")
def test_go_to_order_history(driver):
    page = LoginPage(driver)
    page.go(URLs.LOGIN_PAGE)
    page.set_email(USER["email"])
    page.set_password(USER["password"])
    page.submit()
    # Явно ждем появления кнопки Личный кабинет и кликаем по ней
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.PROFILE_BTN)).click()
    # Явно ждем появления ссылки "История заказов" и кликаем по ней
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.ORDER_HISTORY_TAB)).click()
    # Проверяем, что мы на странице истории заказов
    assert '/account/order-history' in driver.current_url

@allure.title("Logout from profile")
def test_logout(driver):
    page = LoginPage(driver)
    page.go(URLs.LOGIN_PAGE)
    page.set_email(USER["email"])
    page.set_password(USER["password"])
    page.submit()
    WebDriverWait(driver, 10).until(EC.url_to_be(URLs.MAIN_PAGE))
    driver.find_element(*Locators.PROFILE_BTN).click()
    prof = ProfilePage(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON))
    prof.logout()
    WebDriverWait(driver, 10).until(EC.url_to_be(URLs.LOGIN_PAGE))
    assert driver.current_url == URLs.LOGIN_PAGE

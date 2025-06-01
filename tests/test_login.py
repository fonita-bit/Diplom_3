import allure
from utils.urls import URLs
from data.test_user import USER
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import Locators
from selenium.webdriver.common.by import By

@allure.title("Login via main page button")
def test_login_via_main_button(driver):
    # Открываем главную, нажимаем «Войти в аккаунт» (можно реализовать через Page Object Header, если есть)
    driver.get(URLs.MAIN_PAGE)
    driver.find_element(*Locators.LOGIN_MAIN_BUTTON).click()
    page = LoginPage(driver)
    page.set_email(USER["email"])
    page.set_password(USER["password"])
    page.submit()
    WebDriverWait(driver, 10).until(EC.url_to_be(URLs.MAIN_PAGE))
    assert driver.current_url == URLs.MAIN_PAGE

@allure.title("Login via profile button")
def test_login_via_profile_button(driver):
    driver.get(URLs.MAIN_PAGE)
    driver.find_element(*Locators.PROFILE_BTN).click()
    page = LoginPage(driver)
    page.set_email(USER["email"])
    page.set_password(USER["password"])
    page.submit()
    WebDriverWait(driver, 10).until(EC.url_to_be(URLs.MAIN_PAGE))
    assert driver.current_url == URLs.MAIN_PAGE

@allure.title("Login via registration form link")
def test_login_via_registration_form(driver):
    driver.get(URLs.REGISTRATION_PAGE)
    # На странице регистрации ссылка «Войти» обычно находится снизу формы
    driver.find_element(By.LINK_TEXT, "Войти").click()
    page = LoginPage(driver)
    page.set_email(USER["email"])
    page.set_password(USER["password"])
    page.submit()
    WebDriverWait(driver, 10).until(EC.url_to_be(URLs.MAIN_PAGE))
    assert driver.current_url == URLs.MAIN_PAGE

@allure.title("Login via forgot password form link")
def test_login_via_forgot_password_form(driver):
    driver.get(URLs.FORGOT_PASSWORD_PAGE)
    # На странице восстановления пароля ссылка «Войти» также присутствует
    driver.find_element(By.LINK_TEXT, "Войти").click()
    page = LoginPage(driver)
    page.set_email(USER["email"])
    page.set_password(USER["password"])
    page.submit()
    WebDriverWait(driver, 10).until(EC.url_to_be(URLs.MAIN_PAGE))
    assert driver.current_url == URLs.MAIN_PAGE

@allure.title("Login shows/hides password field highlight")
def test_show_hide_password_highlight(driver):
    page = LoginPage(driver)
    page.go(URLs.LOGIN_PAGE)
    # Клик по иконке показать/скрыть пароль должен подсветить поле
    page.set_email(USER["email"])
    page.set_password(USER["password"])
    page.show_password()
    # Проверка, что поле подсвечено (например, по CSS классу или стилю)
    input_elem = driver.find_element(*Locators.PASSWORD_INPUT)
    assert "input_status_active" in input_elem.get_attribute("class") or input_elem == driver.switch_to.active_element


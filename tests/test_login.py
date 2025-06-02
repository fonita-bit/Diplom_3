import allure
import pytest

from data.user_data import USER
from pages.login_page import LoginPage
from utils.urls import URLs


@allure.suite("Login Feature")
class TestLogin:

    @allure.title("Login via main page button")
    def test_login_via_main_button(self, driver):
        page = LoginPage(driver)
        page.go_and_login_from_main(USER["email"], USER["password"])
        assert driver.current_url == URLs.MAIN_PAGE

    @allure.title("Login via profile button")
    def test_login_via_profile_button(self, driver):
        page = LoginPage(driver)
        page.go_and_login_from_profile(USER["email"], USER["password"])
        assert driver.current_url == URLs.MAIN_PAGE

    @allure.title("Login via registration form link")
    def test_login_via_registration_form(self, driver):
        page = LoginPage(driver)
        page.go_and_login_from_registration(USER["email"], USER["password"])
        assert driver.current_url == URLs.MAIN_PAGE

    @allure.title("Login via forgot password form link")
    def test_login_via_forgot_password_form(self, driver):
        page = LoginPage(driver)
        page.go_and_login_from_forgot_password(USER["email"], USER["password"])
        assert driver.current_url == URLs.MAIN_PAGE

    @allure.title("Login shows/hides password field highlight")
    def test_show_hide_password_highlight(self, driver):
        page = LoginPage(driver)
        page.go(URLs.LOGIN_PAGE)
        page.set_email(USER["email"])
        page.set_password(USER["password"])
        page.show_password()

        input_elem = page.get_password_input_element()
        assert "input_status_active" in input_elem.get_attribute("class") or input_elem == driver.switch_to.active_element

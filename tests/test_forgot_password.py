import allure
import pytest

from data.user_data import USER
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from utils.urls import URLs


@allure.suite("Forgot Password Feature")
class TestForgotPassword:

    @allure.title("Go to forgot password page from login")
    def test_go_to_forgot_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.go(URLs.LOGIN_PAGE)
        login_page.go_to_forgot_password_page()
        assert login_page.get_current_url() == URLs.FORGOT_PASSWORD_PAGE

    @allure.title("Restore password: enter email and submit")
    def test_restore_password_submit(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.go(URLs.FORGOT_PASSWORD_PAGE)
        forgot_page.fill_and_submit(USER["email"])
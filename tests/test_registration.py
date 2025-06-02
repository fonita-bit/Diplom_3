import allure
import pytest
import time

from data.user_data import USER
from pages.registration_page import RegistrationPage
from utils.urls import URLs


@allure.suite("Registration Feature")
class TestRegistration:

    @allure.title("Successful registration")
    def test_successful_registration(self, driver):
        page = RegistrationPage(driver)
        page.go(URLs.REGISTRATION_PAGE)
        page.set_name(USER["name"])

        def generate_unique_email():
            return f"autotest_{int(time.time())}@mail.com"

        email = generate_unique_email()
        page.set_email(email)
        page.set_password(USER["password"])
        page.submit()
        assert page.is_redirected_to_login()

    @allure.title("Registration with invalid password error")
    def test_invalid_password_registration(self, driver):
        page = RegistrationPage(driver)
        page.go(URLs.REGISTRATION_PAGE)
        page.set_name(USER["name"])
        page.set_email(USER["email"])
        page.set_password("123")
        page.submit()
        assert page.is_password_error_visible()
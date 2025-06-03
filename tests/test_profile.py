import allure
import pytest

from data.user_data import USER
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from utils.urls import URLs


@allure.suite("Profile Feature")
class TestProfile:

    @allure.title("Go to profile via profile button")
    def test_navigate_to_profile(self, driver):
        login_page = LoginPage(driver)
        login_page.go_and_login_from_profile(USER["email"], USER["password"])

        profile_page = ProfilePage(driver)
        profile_page.go_to_profile()

        assert "/account" in profile_page.get_current_url()

    @allure.title("Go to order history tab in profile")
    def test_go_to_order_history(self, driver):
        login_page = LoginPage(driver)
        login_page.go_and_login_from_profile(USER["email"], USER["password"])

        profile_page = ProfilePage(driver)
        profile_page.go_to_profile()
        profile_page.go_to_order_history()

        assert "/account/order-history" in profile_page.get_current_url()

    @allure.title("Logout from profile")
    def test_logout(self, driver):
        login_page = LoginPage(driver)
        login_page.go_and_login_from_profile(USER["email"], USER["password"])

        profile_page = ProfilePage(driver)
        profile_page.go_to_profile()
        profile_page.logout()

        assert profile_page.get_current_url() == URLs.LOGIN_PAGE
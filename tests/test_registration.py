import allure
import time
from utils.urls import URLs
from data.test_user import USER
from pages.registration_page import RegistrationPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import Locators

@allure.title("Successful registration")
def test_successful_registration(driver):
    page = RegistrationPage(driver)
    page.go(URLs.REGISTRATION_PAGE)
    page.set_name(USER["name"])

    def generate_unique_email():
        return f"autotest_{int(time.time())}@mail.com"
    email = generate_unique_email()
    page.set_email(email)
    page.set_password(USER["password"])
    page.submit()
    WebDriverWait(driver, 10).until(EC.url_contains(URLs.LOGIN_PAGE))
    assert driver.current_url.startswith(URLs.LOGIN_PAGE)

@allure.title("Registration with invalid password error")
def test_invalid_password_registration(driver):
    page = RegistrationPage(driver)
    page.go(URLs.REGISTRATION_PAGE)
    page.set_name(USER["name"])
    page.set_email(USER["email"])
    page.set_password("123")
    page.submit()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ERROR_PASSWORD))
    assert page.error_message().is_displayed()

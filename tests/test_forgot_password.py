import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.urls import URLs
from utils.locators import Locators
from data.test_user import USER
from pages.forgot_password_page import ForgotPasswordPage

@allure.title("Go to forgot password page from login")
def test_go_to_forgot_password_page(driver):
    driver.get(URLs.LOGIN_PAGE)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Восстановить пароль"))
    )
    driver.find_element(By.LINK_TEXT, "Восстановить пароль").click()
    assert driver.current_url == URLs.FORGOT_PASSWORD_PAGE

@allure.title("Restore password: enter email and submit")
def test_restore_password_submit(driver):
    page = ForgotPasswordPage(driver)
    page.go(URLs.FORGOT_PASSWORD_PAGE)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.FORGOT_PASSWORD_EMAIL_INPUT)
    )
    page.set_email(USER["email"])
    page.submit()

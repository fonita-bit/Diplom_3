import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.urls import URLs
from data.test_user import USER
from pages.login_page import LoginPage
from utils.locators import Locators

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")

def login_user(driver):
    driver.get(URLs.MAIN_PAGE)
    driver.find_element(*Locators.LOGIN_MAIN_BUTTON).click()
    page = LoginPage(driver)
    page.set_email(USER["email"])
    page.set_password(USER["password"])
    page.submit()
    # Ждем, пока окажемся на главной после логина
    WebDriverWait(driver, 10).until(EC.url_to_be(URLs.MAIN_PAGE))

@pytest.fixture
def logged_in_user(driver):
    login_user(driver)
    return driver

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "firefox":
        from selenium.webdriver.firefox.service import Service as FirefoxService
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:
        from selenium.webdriver.chrome.service import Service as ChromeService
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()




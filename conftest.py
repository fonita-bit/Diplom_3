import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from pages.login_page import LoginPage
from utils.urls import URLs
from data.user_data import USER


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "firefox":
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_user(driver):
    login_page = LoginPage(driver)
    login_page.go_and_login_from_main(USER["email"], USER["password"])
    return driver

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.driver.find_element(*locator).click()

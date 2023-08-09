from core.driver.driver_factory import DriverFactory
from core.driver.driver_properties import DriverProperties
from appium.webdriver.webdriver import WebDriver


class DriverManager:
    driver: WebDriver

    def __init__(self):
        self.driver = None

    def init_driver(self, properties: DriverProperties):
        driver_created = DriverFactory().init_driver(properties)
        if driver_created is not None:
            self.driver = driver_created

    def get_driver(self):
        return self.driver

    def quit_driver(self):
        self.driver.quit()

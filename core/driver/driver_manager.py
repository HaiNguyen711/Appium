import json
from driver_factory import DriverFactory
from driver_properties import DriverProperties
from appium.webdriver.webdriver import WebDriver


class DriverManager:
    driver: WebDriver

    def __init__(self):
        pass

    @staticmethod
    def init_driver(self, properties: DriverProperties):
        driver_created = DriverFactory.init_driver(properties)
        if driver_created is not None:
            self.driver = driver_created

    @staticmethod
    def get_driver(self):
        return self.driver

    def quit_driver(self):
        self.driver.quit()

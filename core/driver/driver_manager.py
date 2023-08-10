from core.driver.driver_factory import DriverFactory
from core.driver.driver_properties import DriverProperties
from appium.webdriver.webdriver import WebDriver


class DriverManager:
    __driver: WebDriver
    __wait_seconds = 10

    def __init__(self):
        self.__driver = None

    def init_driver(self, properties: DriverProperties):
        driver_created = DriverFactory().init_driver(properties)
        if driver_created is not None:
            self.__driver = driver_created

    def start_recording(self):
        self.__driver.start_recording_screen()

    def stop_recording(self):
        self.__driver.stop_recording_screen()

    def take_screen_shot(self):
        self.__driver.get_screenshot_as_base64()

    def get_driver(self):
        return self.__driver

    def quit_driver(self):
        self.__driver.quit()

    @staticmethod
    def get_timeout_sec() -> int:
        return 10

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from core.constant import constant
from driver_properties import DriverProperties

APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'


class DriverFactory:
    def __init__(self):
        pass

    def init_driver(self, properties: DriverProperties) -> WebDriver | None:
        try:
            match properties.platform_name.upper():
                case constant.IOS:
                    return self.__create_ios_driver(properties)
                case constant.ANDROID:
                    return self.__create_android_driver(properties)
        except:
            return None

    def __create_android_driver(self, properties: DriverProperties):
        options = UiAutomator2Options()
        options.platform_name = properties.platform_name
        options.platformVersion = properties.platform_version
        if properties.capabilities is not None:
            options.load_capabilities(properties.capabilities)
        return webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)

    def __create_ios_driver(self, properties: DriverProperties):
        options = XCUITestOptions()
        options.platform_name = properties.platform_name
        options.platformVersion = properties.platform_version
        if properties.capabilities is not None:
            options.load_capabilities(properties.capabilities)
        return webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)

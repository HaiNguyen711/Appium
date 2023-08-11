from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.webdriver import WebDriver

from core.util.logger import logger
from core.constant import constant
from core.driver.driver_properties import DriverProperties


class DriverFactory:
    def init_driver(self, properties: DriverProperties) -> WebDriver | None:
        logger.info("init_driver")
        logger.info(properties.platform_name.upper())
        try:
            match properties.platform_name.upper():
                case constant.IOS:
                    logger.info("Init ios driver")
                    return self.__create_ios_driver(properties)
                case constant.ANDROID:
                    logger.info("Init android driver")
                    return self.__create_android_driver(properties)
        except Exception as ex:
            logger.error(ex)
            return None

    def __create_android_driver(self, properties: DriverProperties):
        logger.info("__create_android_driver")
        options = UiAutomator2Options()
        options.device_name = properties.device_name
        options.platform_name = properties.platform_name
        options.platformVersion = properties.platform_version
        options.automation_name = properties.automation_name
        options.app_package = properties.app_package
        options.app_activity = properties.app_activity

        if properties.capabilities is not None:
            options.load_capabilities(properties.capabilities)
        logger.info("__create_android_driver")
        driver = webdriver.Remote(properties.remote_url, options=options)
        return driver

    def __create_ios_driver(self, properties: DriverProperties):
        options = XCUITestOptions()
        options.platform_name = properties.platform_name
        options.platformVersion = properties.platform_version
        if properties.capabilities is not None:
            options.load_capabilities(properties.capabilities)
        return webdriver.Remote(properties.remote_url, options=options)

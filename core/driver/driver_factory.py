from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from core.constant import constant
from core.driver.driver_properties import DriverProperties
import traceback
import sys

import logging

logger = logging.getLogger(__name__)

APPIUM_PORT = 8000
APPIUM_HOST = '127.0.0.1'


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
        except:
            logger.error("error")
            traceback.print_exception(*sys.exc_info())
            return None

    def __create_android_driver(self, properties: DriverProperties):
        logger.info("__create_android_driver")
        options = UiAutomator2Options()
        options.platform_name = properties.platform_name
        options.platformVersion = properties.platform_version
        if properties.capabilities is not None:
            options.load_capabilities(properties.capabilities)

        desired_caps = {
            'platformName': 'Android',
            'automationName': 'UiAutomator2',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.example.member_portal',
            'appActivity': 'com.example.member_portal.MainActivity',
            'language': 'en',
            'locale': 'US',
            'noReset': False,
            'sessionOverride': True,
            "newCommandTimeout": 100000,
            "adbExecTimeout": 2000000,
            "appWaitDuration": 1500000,
            "deviceReadyTimeout": 300,
            'videoRecordingEnabled': True,
            'videoRecordingDuration': 7200
        }
        logger.info("__create_android_driver")
        driver = webdriver.Remote('http://127.0.0.1:8000',
                                  options=UiAutomator2Options().load_capabilities(desired_caps))
        return driver

    def __create_ios_driver(self, properties: DriverProperties):
        options = XCUITestOptions()
        options.platform_name = properties.platform_name
        options.platformVersion = properties.platform_version
        if properties.capabilities is not None:
            options.load_capabilities(properties.capabilities)
        return webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)

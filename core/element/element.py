from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.locator.locator import Locator
from core.locator.locator_type import LocatorType
import base64
from core.driver import driver_manager
from core.util.logger import logger


class Element:
    __locator: Locator

    def __init__(self, locator: Locator):
        logger.info("============================xxxxxxxxxxxxxxxxx=============")
        logger.info(locator)
        self.__locator = locator

    def clear(self):
        self.wait_for_element_visible()
        el: WebElement = self.__get_element()
        el.clear()

    def enter(self, value: str) -> None:
        self.wait_for_element_visible()
        el: WebElement = self.__get_element()
        el.send_keys(value)

    def click(self):
        self.wait_for_element_clickable()
        el: WebElement = self.__get_element()
        el.click()

    def wait_for_element_visible(self):
        driver = driver_manager.get_driver()
        by = self.__locator.locator_type.value
        value = self.__locator.value
        return WebDriverWait(driver, driver_manager.get_timeout_sec()).until(
            EC.visibility_of_element_located((by, value)))

    def wait_for_element_clickable(self):
        driver = driver_manager.get_driver()
        by = self.__locator.locator_type.value
        value = self.__locator.value
        return WebDriverWait(driver, driver_manager.get_timeout_sec()).until(EC.element_to_be_clickable((by, value)))

    def __get_element(self) -> WebElement:
        __driver = driver_manager.get_driver()
        el = __driver.find_element(by=self.__locator.locator_type, value=self.__locator.value)
        return el

    def __find_image(self, image_path: str) -> WebElement:
        __driver = driver_manager.get_driver()
        if self.__locator.locator_type is LocatorType.IMAGE:
            with open(image_path, 'rb') as file:
                base64_data = base64.b64encode(file.read()).decode('UTF-8')
            el = __driver.find_element(by=AppiumBy.IMAGE, value=base64_data)
            return el
        else:
            return None

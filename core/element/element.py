from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.locator.locator import Locator
import base64
from core.driver import driver_manager
from core.util.logger import logger


class Element:
    __locator: Locator

    def __init__(self, locator: Locator):
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

    def check(self):
        self.wait_for_element_visible()
        if self.is_selected() is False:
            self.__get_element().click()

    def un_check(self):
        self.wait_for_element_visible()
        if self.is_selected() is True:
            self.__get_element().click()

    def is_displayed(self) -> bool:
        self.wait_for_element_visible()
        return self.__get_element().is_displayed()

    def get_text(self) -> str:
        self.wait_for_element_visible()
        return self.__get_element().text

    def get_attribute(self, attr) -> str:
        self.wait_for_element_visible()
        return self.__get_element().get_attribute(attr)

    def is_enabled(self) -> bool:
        return self.__get_element().is_enabled()

    def is_selected(self) -> bool:
        return self.__get_element().is_selected()

    def wait_for_element_visible(self):
        driver = driver_manager.get_driver()
        by: str = self.__locator.get_by_value()
        value: str = self.__locator.get_value()
        WebDriverWait(driver, driver_manager.get_timeout_sec()).until(EC.visibility_of_element_located((by, value)))

    def wait_for_element_clickable(self):
        driver = driver_manager.get_driver()
        by: str = self.__locator.get_by_value()
        value: str = self.__locator.get_value()
        WebDriverWait(driver, driver_manager.get_timeout_sec()).until(EC.element_to_be_clickable((by, value)))

    def __get_element(self) -> WebElement:
        try:
            __driver = driver_manager.get_driver()
            el = __driver.find_element(by=self.__locator.get_by(), value=self.__locator.get_value())
            return el
        except Exception as ex:
            logger.error(ex)

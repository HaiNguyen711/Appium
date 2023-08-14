import base64

from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy

from core.driver import driver_manager
from core.locator.locator import Locator


class Image:
    # __path: str
    __locator: Locator

    def __init__(self, path: str):
        self.__locator = Locator.image(path)

    # def __init__(self, locator: Locator):
    #     self.__locator = locator.image()

    def click(self):
        # self.wait_for_element_clickable()
        el: WebElement = self.__find_by_image(self.__locator.get_value())
        el.click()

    def __find_by_image(self, image_path: str) -> WebElement:
        driver = driver_manager.get_driver()
        if self.__locator.get_by() is AppiumBy.IMAGE:
            with open(image_path, 'rb') as file:
                base64_data = base64.b64encode(file.read()).decode('UTF-8')
            el = driver.find_element(by=AppiumBy.IMAGE, value=base64_data)
            return el
        else:
            return None

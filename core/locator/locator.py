from appium.webdriver.common.appiumby import AppiumBy

from core.util.logger import logger


class Locator:
    __by: AppiumBy
    __value: str

    def __init__(self, by: AppiumBy, value: str):
        self.__by = by
        self.__value = value

    @staticmethod
    def xpath(value: str):
        locator: Locator = Locator(AppiumBy.XPATH, value)
        return locator

    @staticmethod
    def id(value: str):
        locator: Locator = Locator(AppiumBy.ID, value)
        return locator

    @staticmethod
    def image(value: str):
        locator: Locator = Locator(AppiumBy.IMAGE, value)
        return locator

    @staticmethod
    def link_text(value: str):
        locator: Locator = Locator(AppiumBy.LINK_TEXT, value)
        return locator

    @staticmethod
    def partial_link_text(value: str):
        locator: Locator = Locator(AppiumBy.PARTIAL_LINK_TEXT, value)
        return locator

    @staticmethod
    def name(value: str):
        locator: Locator = Locator(AppiumBy.NAME, value)
        return locator

    @staticmethod
    def tag_name(value: str):
        locator: Locator = Locator(AppiumBy.TAG_NAME, value)
        return locator

    @staticmethod
    def class_name(value: str):
        locator: Locator = Locator(AppiumBy.CLASS_NAME, value)
        return locator

    @staticmethod
    def css_selector(value: str):
        locator: Locator = Locator(AppiumBy.CSS_SELECTOR, value)
        return locator

    @staticmethod
    def accessibility_id(value: str):
        locator: Locator = Locator(AppiumBy.ACCESSIBILITY_ID, value)
        return locator

    def get_by(self) -> AppiumBy:
        return self.__by

    def get_value(self) -> str:
        return self.__value

    def get_by_value(self) -> str:
        match self.__by:
            case AppiumBy.XPATH:
                return AppiumBy.XPATH

            case AppiumBy.ID:
                return AppiumBy.ID

            case AppiumBy.IMAGE:
                return AppiumBy.IMAGE

            case AppiumBy.LINK_TEXT:
                return AppiumBy.LINK_TEXT

            case AppiumBy.PARTIAL_LINK_TEXT:
                return AppiumBy.PARTIAL_LINK_TEXT

            case AppiumBy.NAME:
                return AppiumBy.NAME

            case AppiumBy.TAG_NAME:
                return AppiumBy.TAG_NAME

            case AppiumBy.CLASS_NAME:
                return AppiumBy.CLASS_NAME

            case AppiumBy.CSS_SELECTOR:
                return AppiumBy.CSS_SELECTOR

            case AppiumBy.ACCESSIBILITY_ID:
                return AppiumBy.ACCESSIBILITY_ID

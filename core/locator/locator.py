from core.locator.locator_type import LocatorType
from core.util.logger import logger


class Locator:
    locator_type: LocatorType
    value: str

    def __init__(self, locator_type: LocatorType, value: str):
        self.locator_type = locator_type
        self.value = value

    @staticmethod
    def xpath(value: str):
        locator: Locator = Locator(LocatorType.XPATH, value)
        return locator

    @staticmethod
    def id(value: str):
        locator: Locator = Locator(LocatorType.ID, value)
        return locator

    @staticmethod
    def image(value: str):
        locator: Locator = Locator(LocatorType.IMAGE, value)
        return locator

    @staticmethod
    def link_text(value: str):
        locator: Locator = Locator(LocatorType.LINK_TEXT, value)
        return locator

    @staticmethod
    def partial_link_text(value: str):
        locator: Locator = Locator(LocatorType.PARTIAL_LINK_TEXT, value)
        return locator

    @staticmethod
    def name(value: str):
        locator: Locator = Locator(LocatorType.NAME, value)
        return locator

    @staticmethod
    def tag_name(value: str):
        locator: Locator = Locator(LocatorType.TAG_NAME, value)
        return locator

    @staticmethod
    def class_name(value: str):
        locator: Locator = Locator(LocatorType.CLASS_NAME, value)
        return locator

    @staticmethod
    def css_selector(value: str):
        locator: Locator = Locator(LocatorType.CSS_SELECTOR, value)
        return locator

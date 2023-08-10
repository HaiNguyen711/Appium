from core.locator.locator_type import LocatorType
from core.util.logger import logger


class Locator:
    locator_type: LocatorType
    value: str

    def __init__(self):
        logger.info("locator init data")
        self.locator_type = None
        self.value = None

    @staticmethod
    def xpath(value: str):
        logger.info("xpath_xpath_xpath")
        locator: Locator = Locator()
        locator.locator_type = LocatorType.XPATH
        locator.value = value
        return locator

    @staticmethod
    def id(self, value: str):
        self.locator_type = LocatorType.ID
        self.value = value

    @staticmethod
    def image(self, value: str):
        self.locator_type = LocatorType.IMAGE
        self.value = value

    @staticmethod
    def link_text(self, value: str):
        self.locator_type = LocatorType.LINK_TEXT
        self.value = value

    @staticmethod
    def partial_link_text(self, value: str):
        self.locator_type = LocatorType.PARTIAL_LINK_TEXT
        self.value = value

    @staticmethod
    def name(self, value: str):
        self.locator_type = LocatorType.NAME
        self.value = value

    @staticmethod
    def tag_name(self, value: str):
        self.locator_type = LocatorType.TAG_NAME
        self.value = value

    @staticmethod
    def class_name(self, value: str):
        self.locator_type = LocatorType.CLASS_NAME
        self.value = value

    @staticmethod
    def css_selector(self, value: str):
        self.locator_type = LocatorType.CSS_SELECTOR
        self.value = value

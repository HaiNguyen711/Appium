from enum import Enum
from appium.webdriver.common.appiumby import AppiumBy


class LocatorType(Enum):
    XPATH = AppiumBy.XPATH,
    ID = AppiumBy.ID,
    IMAGE = AppiumBy.IMAGE,
    LINK_TEXT = AppiumBy.LINK_TEXT
    PARTIAL_LINK_TEXT = AppiumBy.PARTIAL_LINK_TEXT
    NAME = AppiumBy.NAME
    TAG_NAME = AppiumBy.TAG_NAME
    CLASS_NAME = AppiumBy.CLASS_NAME
    CSS_SELECTOR = AppiumBy.CSS_SELECTOR

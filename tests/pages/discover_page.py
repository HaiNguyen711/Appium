from core.element.element import Element
from core.locator.locator import Locator
from tests.pages.general_page import GeneralPage


class DiscoverPage(GeneralPage):
    ele_voucher_paradise_title: Element = Element(Locator.accessibility_id("Voucher Paradise"))

    def is_displayed_title(self) -> bool:
        return self.ele_voucher_paradise_title.is_displayed()

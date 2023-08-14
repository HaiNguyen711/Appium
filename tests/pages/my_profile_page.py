from core.element.element import Element
from core.locator.locator import Locator
from tests.pages.general_page import GeneralPage


class MyProfilePage(GeneralPage):
    ele_my_profile_title: Element

    def is_displayed_page_title(self, title) -> bool:
        self.ele_my_profile_title: Element = Element(Locator.accessibility_id(title))
        return self.ele_my_profile_title.is_displayed()

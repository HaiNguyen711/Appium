from core.element.element import Element
from core.element.image import Image
from core.locator.locator import Locator
from tests.constant.image_path import ImagePath



class GeneralPage:
    ele_tab_discover: Element = Element(Locator.accessibility_id('Discover Tab 1 of 3'))
    ele_tab_my_profile: Image = Image(ImagePath.TAB_MY_PROFILE)
    ele_tab_setting: Element = Element(Locator.accessibility_id('Settings Tab 3 of 3'))

    def navigate_to_tab_my_profile(self):
        self.ele_tab_my_profile.click()
        from tests.pages.my_profile_page import MyProfilePage
        return MyProfilePage()

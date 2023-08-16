from core.element.element import Element
from core.locator.locator import Locator
from tests.pages.general_page import GeneralPage


class MyProfilePage(GeneralPage):
    ele_my_profile_title: Element
    btn_setting: Element = Element(Locator.xpath("//android.widget.ImageView/following-sibling::android.widget.Button"))
    ele_username: Element = Element(Locator.xpath("//android.widget.ImageView/following-sibling::android.view.View[2]"))

    def is_displayed_page_title(self, title) -> bool:
        self.ele_my_profile_title: Element = Element(Locator.accessibility_id(title))
        return self.ele_my_profile_title.is_displayed()

    def get_username(self):
        return self.ele_username.get_attribute('content-desc')

    def click_setting_button(self):
        self.btn_setting.click()

from core.element.element import Element
from core.locator.locator import Locator
from core.util.logger import logger
from tests.pages.discover_page import DiscoverPage
from core.element.image import Image
from tests.data_objects.user import User


class LoginPage:
    txt_username: Element = Element(Locator.xpath("//android.widget.EditText[contains(@hint,'Username')]"))
    txt_password: Element = Element(Locator.xpath("//android.widget.EditText[contains(@hint,'Password')]"))
    # txt_username: Element = Element(Locator.xpath("//android.widget.EditText[1]"))
    # txt_password: Element = Element(Locator.xpath("//android.widget.EditText[@hint='Password']"))
    btn_sign_in: Element = Element(Locator.xpath("//android.widget.Button[@content-desc='Sign in']"))
    ele_error_message: Element = Element(
        Locator.xpath("//android.view.View[@content-desc='Invalid username or password']"))

    # img_login: Image = Image('path')
    # img_test: Image = Image(Locator.image('path'))

    def __init__(self):
        logger.info("login page init data")

    def login(self, user: User):
        return self.__login(user.get_username(), user.get_password())

    def __login(self, username: str, password: str):
        self.txt_username.enter(username)
        self.txt_password.click()
        self.txt_password.enter(password)
        self.btn_sign_in.click()
        return DiscoverPage()

    def login_fail(self, username: str, password: str):
        self.txt_username.enter(username)
        self.txt_password.click()
        self.txt_password.enter(password)
        self.btn_sign_in.click()
        return self

    def is_displayed_error_message(self) -> bool:
        return self.ele_error_message.is_displayed()

    def get_error_message(self) -> str:
        return self.ele_error_message.get_attribute('content-desc')

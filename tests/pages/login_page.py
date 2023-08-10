from core.element.element import Element
from core.locator.locator import Locator
from core.util.logger import logger


class LoginPage:
    txt_username: Element = Element(Locator.xpath("//android.widget.EditText[2]"))
    txt_password: Element = Element(Locator.xpath("//android.widget.EditText[@hint='Password']"))
    btn_sign_in: Element = Element(Locator.xpath("//android.widget.Button[@content-desc='Sign in']"))

    def __init__(self):
        logger.info("login page init data")

    def login(self, username: str, password: str):
        self.txt_username.enter(username)
        self.txt_password.click()
        self.txt_password.enter(password)
        self.btn_sign_in.enter()

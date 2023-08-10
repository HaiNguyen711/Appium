from tests.test_cases.test_base import TestBase

from tests.pages.login_page import LoginPage

from core.util.logger import logger


class TestLogin(TestBase):
    login_page: LoginPage = LoginPage()

    def test_login(self):
        logger.info('input username')
        self.login_page.login("ma@vp.com", "password")

        logger.info("done")

    # def test_login2(self):
    #     print('test_login2')
    #     sleep(15)
    #     logger.info("done")

    # def test_login3(self):
    #     print('test_login3')
    #
    # def test_login4(self):
    #     sleep(5)
    #     print('test_login4')

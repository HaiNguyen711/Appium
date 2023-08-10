from tests.test_cases.test_base import TestBase

from tests.pages.login_page import LoginPage

from core.util.logger import logger
from time import sleep


class TestLogin(TestBase):
    login_page: LoginPage = LoginPage()

    def test_login(self):
        logger.info('input username')
        self.login_page.login("ma@vp.com", "password")
        logger.info("test_login_1_1")
        sleep(1)
        logger.info("test_login_1_2")
        logger.info("test_login_1_3")
        sleep(3)
        logger.info("test_login_1_4")
        logger.info("test_login_1_5")
        sleep(1)
        logger.info("test_login_1_6")
        logger.info("test_login_1_7")
        logger.info("test_login_1_8")
        logger.info("done")

    # def test_login2(self):
    #     print('test_login2_1')
    #     print('test_login2_2')
    #     print('test_login2_3')
    #     sleep(1)
    #     print('test_login2_4')
    #     print('test_login2_5')
    #     print('test_login2_6')
    #     sleep(4)
    #     print('test_login2_7')
    #     print('test_login2_8')
    #     logger.info("done")
    #
    # def test_login3(self):
    #     sleep(1)
    #     print('test_login3_1')
    #     print('test_login3_2')
    #     sleep(2)
    #     print('test_login3_3')
    #     sleep(1)
    #     print('test_login3_4')
    #     print('test_login3_5')
    #     sleep(1)
    #     print('test_login3_6')
    #     print('test_login3_7')
    #     print('test_login3_8')
    #     sleep(1)
    #     print('test_login3_9')
    #
    # def test_login4(self):
    #     print('test_login4_1')
    #     print('test_login4_2')
    #     sleep(1)
    #     print('test_login4_3')
    #     sleep(1)
    #     print('test_login4_4')
    #     sleep(4)
    #     print('test_login4_5')
    #     print('test_login4_6')
    #     print('test_login4_7')
    #     sleep(1)
    #     print('test_login4_8')

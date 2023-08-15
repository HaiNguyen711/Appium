from tests.test_cases.test_base import TestBase
import allure
from tests.pages.login_page import LoginPage
from tests.pages.discover_page import DiscoverPage

# from core.util.logger import logger
# from core.util.logger import step
# from time import sleep


class TestLogin(TestBase):
    login_page: LoginPage = LoginPage()
    discover_page: DiscoverPage

    def test_login(self):
        # logger.info('input username')

        # allure.step("Input username and password")
        # step('Input username and password')
        with allure.step("Input username and password"):
            self.discover_page = self.login_page.login("ma@vp.com", "password")

        with allure.step("Verify page title 'voucher paradise' displayed"):
            assert self.discover_page.is_displayed_title() is True, "Doesn't displayed voucher paradise title"

    # def test_login2(self):
    #     logger.info('input username')
    #     self.login_page.login_fail("ma@vp.com", "password_error")
    #
    #     logger.info("verify error message displayed")
    #     assert self.login_page.is_displayed_error_message() is True, "Doesn't displayed error message"
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

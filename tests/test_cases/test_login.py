import allure
import pytest

from tests.helper.assert_helper import AssertHelper
from tests.pages.discover_page import DiscoverPage
from tests.pages.login_page import LoginPage
from tests.test_cases.test_base import TestBase
from tests.constant.constant import Constant


class TestLogin(TestBase):
    login_page: LoginPage = LoginPage()
    discover_page: DiscoverPage

    @pytest.mark.C001
    def test_login(self):
        with allure.step('Input username and password'):
            self.discover_page = self.login_page.login(Constant.USER)

        with allure.step("Verify page title 'voucher paradise' displayed"):
            AssertHelper.assert_true(self.discover_page.is_displayed_title(),
                                     "Doesn't displayed voucher paradise title")

    @pytest.mark.C002
    def test_login2(self):
        with allure.step('input username'):
            self.login_page.login_fail("ma@vp.com", "password_error")

        with allure.step("verify error message displayed"):
            AssertHelper.assert_true(self.login_page.is_displayed_error_message(), "Doesn't displayed error message")

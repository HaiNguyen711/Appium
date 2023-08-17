import allure
import pytest

from tests.pages.login_page import LoginPage
from tests.pages.my_profile_page import MyProfilePage
from tests.test_cases.test_base import TestBase
from tests.helper.assert_helper import AssertHelper
from tests.constant.constant import Constant


class TestMyProfile(TestBase):
    login_page: LoginPage = LoginPage()
    my_profile_page: MyProfilePage

    @pytest.mark.C003
    def test_verify_my_profile_displayed(self):
        with allure.step('input username'):
            self.discover_page = self.login_page.login(Constant.USER)

        with allure.step("Verify discover page displayed"):
            AssertHelper.assert_true(self.discover_page.is_displayed_title(),
                                     "Doesn't displayed voucher paradise title")

        with allure.step("Navigate to my profile page"):
            self.my_profile_page = self.discover_page.navigate_to_tab_my_profile()

        with allure.step("Verify my profile page displayed"):
            AssertHelper.assert_true(self.my_profile_page.is_displayed_page_title('My Profile'),
                                     'Display my profile page')

    @pytest.mark.C004
    def test_verify_username(self):
        username_expected = 'Linda Ngo'
        with allure.step('input username'):
            self.discover_page = self.login_page.login(Constant.USER)

        with allure.step('Verify username displayed successful'):
            self.my_profile_page = self.discover_page.navigate_to_tab_my_profile()
            username = self.my_profile_page.get_username()
            AssertHelper.assert_equals(username, username_expected, "Doesn't displayed username {}".format(username))

        with allure.step("Update user info"):
            self.my_profile_page.click_setting_button()

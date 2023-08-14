from core.util.logger import logger
from tests.pages.login_page import LoginPage
from tests.pages.my_profile_page import MyProfilePage
from tests.test_cases.test_base import TestBase


class TestMyProfile(TestBase):
    login_page: LoginPage = LoginPage()
    my_profile_page: MyProfilePage

    def test_verify_my_profile_displayed(self):
        logger.info('input username')
        self.discover_page = self.login_page.login("ma@vp.com", "password")

        logger.info("Verify discover page displayed")
        assert self.discover_page.is_displayed_title() is True, "Doesn't displayed voucher paradise title"

        logger.info("Navigate to my profile page")
        self.my_profile_page = self.discover_page.navigate_to_tab_my_profile()

        logger.info("Verify my profile page displayed")
        assert self.my_profile_page.is_displayed_page_title('My Profile')

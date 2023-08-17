import allure
import pytest
from allure_commons.types import AttachmentType

from core.driver import driver_manager


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def take_screen_shot(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        allure.attach(driver_manager.take_screen_shot(), name='asdfasdfasdf', attachment_type=AttachmentType.PNG)

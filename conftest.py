import allure
import pytest
from allure_commons.types import AttachmentType

from core.driver import driver_manager


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    print(item.funcargs)
    print(item.parent.obj)
    print(rep)
    if rep.when == 'call' and rep.failed:
        print('faileddddddddddddddddddddddddddddd')
        file_name = 'test_failed'
        capture_path = (f"./screenshots/{file_name}.png")
        screen_shot = driver_manager.take_screen_shot()
        allure.attach(driver_manager.get_driver().get_screenshot_as_png(), name='asdfasdfasdf', attachment_type=AttachmentType.PNG)
    # else:
        # print('Fail to take screen-shotxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        # return

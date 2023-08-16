import base64
import os
from pathlib import Path
from typing import Optional

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from allure_commons.types import AttachmentType

from core.driver import driver_manager
from core.driver.driver_properties import DriverProperties
from core.util.file_util import load_driver_properties
from core.util.logger import logger

DRIVER_CONFIG_FILE = 'driver_config.json'
CONFIG_FOLDER = 'config'


class TestBase:

    # @pytest.fixture(scope='module')
    def setup_method(self) -> None:
        logger.info("setup_method")
        plat_form = 'android'
        config_file_path = Path(__file__).parent.parent.joinpath(CONFIG_FOLDER).joinpath(DRIVER_CONFIG_FILE)
        logger.info(config_file_path)

        properties: DriverProperties = load_driver_properties(config_file_path, plat_form)
        print(properties)
        if properties is not None:
            logger.info('init_driver')
            driver_manager.init_driver(properties)
            driver = driver_manager.get_driver()
            driver.start_recording_screen()

    # @pytest.fixture(scope='module')
    def teardown_method(self, method) -> None:
        logger.info("teardown_method")
        if driver_manager.get_driver() is not None:
            payload = driver_manager.get_driver().stop_recording_screen()
            video_path = os.path.join(os.getcwd(), method.__name__ + '.mp4')
            with open(video_path, 'wb') as fd:
                fd.write(base64.b64decode(payload))
            driver_manager.quit_driver()

    @pytest.fixture()
    def pytest_runtest_makereport(item, request: FixtureRequest):
        logger.info("asdfffffffffff")
        # logger.info(request.node.re)
        item = request.node
        if item.rep_call.failed:
            allure.attach(driver_manager.get_driver().get_screenshot_as_png(), name='testfailed',
                          attachment_type=AttachmentType.PNG)
    # @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    # def pytest_runtest_makereport(item, call):
    #     logger.info("pytest_runtest_makereport")
    #     global test, status_tag, line, duration, exception
    #     report = yield
    #     result = report.get_result()
    #
    #     if result.when == 'call':
    #         (filename, line, name) = item.location
    #         test = item.nodeid
    #         status_tag = result.outcome
    #         line = line
    #         duration = call.duration
    #         exception = call.excinfo

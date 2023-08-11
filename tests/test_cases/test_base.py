from pathlib import Path
from typing import Optional
from core.driver import driver_manager
from core.driver.driver_properties import DriverProperties
from core.util.file_util import load_driver_properties
from core.util.logger import logger

DRIVER_CONFIG_FILE = 'driver_config.json'
CONFIG_FOLDER = 'config'


class TestBase:
    def setup_method(self) -> None:
        logger.info("setup_method")
        plat_form = 'android'
        config_file_path = Path.cwd().parent.joinpath(CONFIG_FOLDER).joinpath(DRIVER_CONFIG_FILE)

        properties: DriverProperties = load_driver_properties(config_file_path, plat_form)
        print(properties)
        if properties is not None:
            logger.info('init_driver')
            driver_manager.init_driver(properties)

    def teardown_method(self) -> None:
        logger.info("teardown_method")
        if driver_manager.get_driver() is not None:
            driver_manager.quit_driver()

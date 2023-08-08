from core.driver.driver_manager import DriverManager
from core.util.file_util import load_driver_properties
from core.driver.driver_properties import DriverProperties
from pathlib import Path

DRIVER_CONFIG_FILE = 'driver_config.json'
CONFIG_FOLDER = 'config'


class BaseTest:

    def setup_method(self) -> None:
        config_file_path = Path.joinpath(CONFIG_FOLDER).join(DRIVER_CONFIG_FILE)
        properties: DriverProperties = load_driver_properties(config_file_path)
        DriverManager.init_driver(properties)

    def teardown_method(self, method) -> None:
        self.driver.quit()

from pathlib import Path

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
        config_file_path = Path(__file__).parent.parent.joinpath(CONFIG_FOLDER).joinpath(DRIVER_CONFIG_FILE)
        logger.info(config_file_path)

        properties: DriverProperties = load_driver_properties(config_file_path, plat_form)
        print(properties)
        if properties is not None:
            logger.info('init_driver')
            driver_manager.init_driver(properties)
            # driver_manager.start_recording()

    # @pytest.fixture(scope='module')
    def teardown_method(self, method) -> None:
        print('teardown_method')
        logger.info("teardown_method")
        if driver_manager.get_driver() is not None:
            # payload = driver_manager.get_driver().stop_recording_screen()
            # video_path = os.path.join(os.getcwd(), method.__name__ + '.mp4')
            # with open(video_path, 'wb') as fd:
            #     fd.write(base64.b64decode(payload))
            driver_manager.quit_driver()

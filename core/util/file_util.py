from core.driver.driver_properties import DriverProperties
from core.util.logger import logger
import json


def load_driver_properties(file_path: str, plat_form: str) -> DriverProperties:
    try:

        with open(file_path) as json_file:
            json_data = json.load(json_file)
            plat_form_data = json_data[plat_form]
            device_name = plat_form_data['deviceName']
            platform_name = plat_form_data['platformName']
            platform_version = plat_form_data['platformVersion']
            automation_name = plat_form_data['automationName']
            app_package = plat_form_data['appPackage']
            app_activity = plat_form_data['appActivity']
            capabilities = plat_form_data['capabilities']
            remote_url = plat_form_data['remote_url']
            properties = DriverProperties(platform_name,
                                          platform_version,
                                          device_name,
                                          automation_name,
                                          app_package,
                                          app_activity,
                                          capabilities,
                                          remote_url)
            return properties
    except Exception as ex:
        logger.error(ex)
        logger.error("load driver property error")
        return None

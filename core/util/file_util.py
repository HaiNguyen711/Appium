from core.driver.driver_properties import DriverProperties
import json


def load_driver_properties(self, file_path: str) -> DriverProperties:
    try:
        properties: DriverProperties
        with open(file_path) as json_file:
            json_data = json.load(json_file)
            properties.platform_name = json_data['']


        return properties
    except:
        return None

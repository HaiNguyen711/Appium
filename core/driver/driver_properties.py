from typing import Dict


class DriverProperties:
    platform_name: str
    platform_version: str
    device_name: str
    automation_name: str
    app_package: str
    app_activity: str
    capabilities: Dict

    def __init__(self, platform_name: str,
                 platform_version: str,
                 device_name: str,
                 automation_name: str,
                 app_package: str,
                 app_activity: str,
                 capabilities: Dict):
        self.platform_name = platform_name
        self.platform_version = platform_version
        self.device_name = device_name
        self.automation_name = automation_name
        self.app_package = app_package
        self.app_activity = app_activity
        self.capabilities = capabilities

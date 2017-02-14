from AndroidConf import AndroidConf
from iOSConf import iOSConf
from Modules.setup import SetupTestCase


class CommonLocators(SetupTestCase, AndroidConf, iOSConf):

    def __init__(self):
        super().__init__()

        platform_name = self.driver.capabilities["platformName"]
        print(platform_name)
        platform_version = self.driver.capabilities["platformVersion"]
        print(platform_version)

        if platform_name == "Android" and platform_version == "6.0.1":
            self.common_login_button = self.LOGIN_BUTTON_android
        elif platform_name == "iOS" and platform_version == "9.3":
            #return iOSConf.LOGIN_BUTTON
            self.common_login_button = self.LOGIN_BUTTON_ios
        else:
            self.fail("error in locators")

        # if platform == Android:
        #     self.common_button_ok = self.button_ok_android
        # else:
        #     self.common_button_ok = self.button_ok_ios



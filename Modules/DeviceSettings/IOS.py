""" Methods for IOS device settings """

from Modules.DeviceSettings.DevicesSettings import DeviceSettings
from appium import webdriver
from configuration import PORT
import logging
from time import sleep


class IOS(DeviceSettings):

    def turn_off_auto_correction_in_settings(self):

        logging.info("turn off auto correction in settings for iOS emulator")

        desired_capabilities = {  # this should be in separate file
            "platformName": "iOS",
            "platformVersion": "10.3",
            "deviceName": "iPhone 7",
            "app": "settings",
            "noReset": False,
            "autoAcceptAlerts": True,
            "newCommandTimeout": 60,
            "launchTimeout": 200000,  # iOS only
        }

        self.driver = webdriver.Remote("http://localhost:" + str(PORT) + "/wd/hub", desired_capabilities)

        sleep(4)

        logging.warning("wd started on iOS 10")

        sleep(2)

        self.driver.quit()

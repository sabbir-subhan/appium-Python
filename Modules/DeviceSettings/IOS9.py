""" Methods for IOS 9 device settings """

from Modules.DeviceSettings.IOS import IOS
from appium import webdriver
from configuration import PORT
import logging
from time import sleep


class IOS9(IOS):

    def turn_off_auto_correction_in_settings(self):

        logging.info("turn off auto correction in settings - iOS 9 emulator")

        desired_capabilities = {
            "platformName": "iOS",
            "platformVersion": "9.3",
            "deviceName": "iPhone 5s",
            "app": "settings",
            "noReset": True,
            "autoAcceptAlerts": True,
            "newCommandTimeout": 60,
            "launchTimeout": 200000,  # iOS only
        }

        self.driver = webdriver.Remote("http://localhost:" + str(PORT) + "/wd/hub", desired_capabilities)

        sleep(4)

        logging.warning("wd started on iOS 9")

        sleep(2)

        self.driver.quit()

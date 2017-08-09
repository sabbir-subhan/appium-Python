""" Methods for IOS 9 device settings """

from Modules.DeviceSettings.IOS import IOS
from appium import webdriver
from configuration import PORT
import logging
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from Conf.desired_capabilities import DesiredCapabilities


class IOS9(IOS):

    def turn_off_auto_correction_in_settings(self):

        logging.warning("Turn off auto correction in device settings for iOS 9")

        desired_capabilities = DesiredCapabilities.get_desired_capabilities()  # create local object

        # print("capabilities before update = " + str(desired_capabilities))

        desired_capabilities.get('app') and desired_capabilities.update({'app': 'settings'})
        desired_capabilities.get('bundleId') and desired_capabilities.pop('bundleId', None)

        # print("capabilities after update = " + str(desired_capabilities))

        logging.warning("starting additional appium driver")

        self.driver = webdriver.Remote("http://localhost:" + str(PORT) + "/wd/hub", desired_capabilities)

        sleep(2)

        # general = self.driver.find_element(*self.configuration.DeviceSettings.GENERAL)
        general = self.driver.find_element_by_xpath('//UIATableCell[@name="General"]')
        self.assertIsNotNone(general, "General tab not found")
        logging.info("click on General tab")
        general.click()

        # keyboard = self.driver.find_element(*self.configuration.DeviceSettings.KEYBOARD)
        keyboard = self.driver.find_element_by_xpath('//UIATableCell[@name="Keyboard"]')
        self.assertIsNotNone(keyboard, "Keyboard tab not found")
        logging.info("click on Keyboard tab")
        keyboard.click()
        try:
            # auto_correction = self.driver.find_element(*self.configuration.DeviceSettings.AUTO_CORRECTION)
            auto_correction = self.driver.find_element_by_xpath('//UIATableCell[@name="Auto-Correction"][@value="1"]')
            self.assertIsNotNone(auto_correction, "Auto-Correction tab not found")
            logging.info("disable Auto-Correction")
            auto_correction.click()
        except NoSuchElementException:
            logging.info("Auto-Correction is already disabled")

        sleep(1)

        logging.info("Quit additional driver session")

        self.driver.quit()

        sleep(1)



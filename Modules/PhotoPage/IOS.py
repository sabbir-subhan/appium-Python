""" Methods for IOS to handle Photo Page """

from Modules.PhotoPage.PhotoPage import PhotoPage
from time import sleep
from configuration import platform
import logging
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from Modules.load_class import LoadClass


class IOS(PhotoPage):

    def click_send_button_camera(self):

        sleep(1)

        logging.info("Appium is running on: " + str(platform))

        if "emulator" in str(platform):
            logging.info("Appium is running on emulator = skip taking photo because emulators don't "
                         "support that functionality")
            pass
        else:
            self.switch_context_to_webview()

            logging.info("click 'Send' button")
            send_button = self.driver.find_element(*self.configuration.PhotoScreen.SEND_BUTTON)
            self.assertIsNotNone(send_button, "Send button not found")
            send_button.click()
            sleep(2)

            self.switch_context_to_native()

            logging.info("sending file")
            WebDriverWait(self.driver, 720).until(
                expected_conditions.presence_of_element_located(self.configuration.MainMenuScreen.INBOX_BUTTON),
                "Failed to send file")
            logging.info("File was sent")

    def click_back_arrow_if_running_on_emulator(self):

        logging.info("click back arrow if running on emulator")

        logging.info("Appium is running on: " + str(platform))

        if "emulator" in str(platform):
            logging.info("Appium is running on emulator = click back arrow")
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.back_arrow()
        else:
            pass




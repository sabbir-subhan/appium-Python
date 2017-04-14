"""A class for methods to handle Sound Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass
import logging
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from configuration import platform


class SoundPage(BasePage):

    def check_if_sound_page_was_opened(self):

        video_page_header = self.driver.find_element(*self.configuration.SoundScreen.SOUND_PAGE_HEADER)
        self.assertIsNotNone(video_page_header, "Sound page header was not found")
        logging.info("Sound page was opened")

    def type_description(self, description):

        self.switch_context_to_webview()

        WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_element_located(self.configuration.SoundScreen.DESCRIPTION_FIELD),
            "Failed to locate description field")
        logging.info("type text into description field")
        description_field = self.driver.find_element(*self.configuration.SoundScreen.DESCRIPTION_FIELD)
        self.assertIsNotNone(description_field, "Description field not found")

        description_field.click()
        description_field.send_keys(description)

        self.switch_context_to_native()

    def click_send_button(self):

        logging.info("Appium is running on: " + str(platform))

        if "emulator" in str(platform):
            logging.info("Appium is running on emulator = skip recording sound because emulators don't "
                         "support that functionality")
            pass
        else:
            sleep(1)

            self.switch_context_to_webview()

            logging.info("click 'Send' button")
            send_button = self.driver.find_element(*self.configuration.SoundScreen.SEND_BUTTON)
            self.assertIsNotNone(send_button, "Send button not found")
            send_button.click()
            sleep(2)

            self.switch_context_to_native()

            logging.info("sending file")
            WebDriverWait(self.driver, 600).until(
                expected_conditions.presence_of_element_located(self.configuration.MainMenuScreen.INBOX_BUTTON),
                "Failed to send file")
            logging.info("File was sent")

    def click_record_sound_icon(self):

        logging.info("Appium is running on: " + str(platform))

        if "emulator" in str(platform):
            logging.info("Appium is running on emulator = skip recording sound because emulators don't "
                         "support that functionality")
            pass
        else:
            self.switch_context_to_webview()

            logging.info("clicking in 'Record Sound' icon")
            record_sound_button = self.driver.find_element(*self.configuration.SoundScreen.RECORD_SOUND_BUTTON)
            self.assertIsNotNone(record_sound_button, "record sound button not found")
            record_sound_button.click()

            self.switch_context_to_native()

    def click_back_arrow_if_running_on_emulator(self):

        logging.info("Appium is running on emulator = click back arrow")
        video_page = LoadClass.load_page('VideoPage')
        video_page.setDriver(self.driver)
        video_page.click_back_arrow_if_running_on_emulator()


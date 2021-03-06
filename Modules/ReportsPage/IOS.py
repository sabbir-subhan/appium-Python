""" Methods for IOS to handle Reports Page """

from Modules.ReportsPage.ReportsPage import ReportsPage
from Modules.load_class import LoadClass
import logging
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from configuration import platform


class IOS(ReportsPage):

    def type_text_into_search_field(self, text):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.type_text_into_search_field(text)

    def click_on_lodging_agency_picker(self):

        sleep(4)
        logging.info("click on 'Lodging Agency' picker")
        # lodging_agency_picker = self.driver.find_element(*self.configuration.ReportsScreen.LODGING_AGENCY_PICKER)
        lodging_agency_picker = self.driver.find_element(*self.configuration.ReportsScreen.LODGING_AGENCY_PICKER_FIELD)
        self.assertIsNotNone(lodging_agency_picker, "Lodging Agency picker was not found")
        action = TouchAction(self.driver)
        sleep(1)
        action.tap(element=lodging_agency_picker, count=1).perform()
        sleep(1)

    # def click_on_lodging_agency_picker(self):
    #
    #     sleep(4)
    #     logging.info("click on 'Lodging Agency' picker")
    #     lodging_agency_picker = self.driver.find_element(*self.configuration.ReportsScreen.LODGING_AGENCY_PICKER)
    #     self.assertIsNotNone(lodging_agency_picker, "Lodging Agency picker was not found")
    #     action = TouchAction(self.driver)
    #     sleep(1)
    #     action.tap(element=lodging_agency_picker, count=1).perform()
    #     sleep(1)

    def scroll_down_to_assets_chooser_field(self):

        logging.info("scroll down to assets chooser field")
        var = 10
        while var > 0:
            logging.info("check if assets chooser field is visible")
            assets_chooser_field = self.driver.find_element(*self.configuration.ReportsScreen.ASSETS_CHOOSER_FIELD)
            if assets_chooser_field.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                var = var - 1

    def scroll_down_to_publish_button(self):

        logging.info("scroll down to Publish button")
        scroll = 20
        while scroll > 0:
            logging.info("check if Publish button is visible")
            publish_button = self.driver.find_element(*self.configuration.ReportsScreen.PUBLISH_BUTTON)
            if publish_button.is_displayed():
                break
            else:
                logging.info("scroll down to Publish button")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                scroll = scroll - 1

    def choose_lodging_agency(self):

        logging.info("choose Lodging Agency")
        try:
            choose_lodging_agency = self.driver.find_element(*self.configuration.ReportsScreen.LODGING_AGENCY)
            self.assertIsNotNone(choose_lodging_agency, "Lodging Agency inside picker was not found")
            choose_lodging_agency.click()
        except NoSuchElementException:
            picker_wheel = self.driver.find_element(*self.configuration.CommonScreen.PICKER_WHEEL)
            picker_wheel.send_keys("contact_group_for_tests")
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.done_button()

    def scroll_down_to_on_load_field(self):

        logging.info("scroll down to on load field")
        var = 10
        while var > 0:
            logging.info("check if on load field is visible")
            on_load_field = self.driver.find_element(*self.configuration.ReportsScreen.ON_LOAD_FIELD)
            if on_load_field.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                var = var - 1

    def scroll_down_media_release_field(self):

        logging.info("scroll down to media release field")
        var = 10
        while var > 0:
            logging.info("check if media release field is visible")
            media_release_field = self.driver.find_element(*self.configuration.ReportsScreen.MEDIA_RELEASE_FIELD)
            if media_release_field.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                var = var - 1

    def scroll_down_to_option_list(self):

        logging.info("scroll down to option list")
        var = 10
        while var > 0:
            logging.info("check if option list is visible")
            option_list = self.driver.find_element(*self.configuration.ReportsScreen.NEW_OPTION_LIST)
            if option_list.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                var = var - 1

    def type_title_offline(self, text):

        self.switch_context_to_webview()

        logging.info("type title")

        if "emulator" in platform:  # there is no automatic way to disable networking on iOS emulators
            title = self.driver.find_element(*self.configuration.ReportsScreen.TITLE_EDITED)
            self.assertIsNotNone(title, "Title input field was not found")
            title.click()
            title.send_keys(text)
        else:
            title = self.driver.find_element(*self.configuration.ReportsScreen.TITLE)
            self.assertIsNotNone(title, "Title input field was not found")
            title.click()
            title.send_keys(text)

        self.switch_context_to_native()

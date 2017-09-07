""" Methods for IOS to handle Logs Page """

from Modules.LogsPage.LogsPage import LogsPage
import logging
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from Modules.load_class import LoadClass
from selenium.common.exceptions import NoSuchElementException


class IOS(LogsPage):

    def type_text_into_search_field(self, text):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.type_text_into_search_field(text)

    def click_on_lodging_agency_picker(self):

        logging.info("click on 'Lodging Agency' picker")
        lodging_agency_picker = self.driver.find_element(*self.configuration.LogsScreen.LODGING_AGENCY_PICKER)
        self.assertIsNotNone(lodging_agency_picker, "Lodging Agency picker was not found")
        action = TouchAction(self.driver)
        sleep(1)
        action.tap(element=lodging_agency_picker, count=1).perform()
        sleep(1)

    def scroll_down_to_entry_field(self):

        # if "Pad" in platform:
        #     pass
        # else:
        logging.info("scroll down with loop")
        var = 20
        while var > 0:
            logging.info("check if entry field is visible")
            try:
                entry_field = self.driver.find_element(*self.configuration.LogsScreen.ENTRY_FIELD)
            except NoSuchElementException:
                entry_field = self.driver.find_element(*self.configuration.LogsScreen.ENTRY_FIELD_BY_XPATH)
            if entry_field.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                var = var - 1

    # def type_text_into_entry_field(self, text):
    #
    #     logging.info("type text into 'Entry' field")
    #     entry_field = self.driver.find_element(*self.configuration.LogsScreen.ENTRY_FIELD)
    #     entry_field.click()
    #     sleep(1)
    #     entry_field.send_keys(text)

    def scroll_down_to_save_button(self):
        """Method to scroll down to bottom of the screen - to 'Save' button"""

        logging.info("scroll down to Save button")
        scroll = 20
        while scroll > 0:
            logging.info("check if save button is visible")
            save_button = self.driver.find_element(*self.configuration.CommonScreen.SAVE_BUTTON)
            if save_button.is_displayed():
                break
            else:
                logging.info("scroll down to save button")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                scroll = scroll - 1

    def scroll_down_to_option_list(self):

        reports_page = LoadClass.load_page('ReportsPage')
        reports_page.setDriver(self.driver)
        reports_page.scroll_down_to_option_list()



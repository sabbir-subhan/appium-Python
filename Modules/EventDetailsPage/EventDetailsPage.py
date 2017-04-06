"""A class for methods to handle Event Details Page """

from Modules.BasePage.BasePage import BasePage
from time import sleep
import logging
from selenium.common.exceptions import *


class EventDetailsPage(BasePage):

    # def event_details_More_button(self):
    #
    #     self.switch_context_to_webview()
    #
    #     logging.info("click 'More' button")
    #     more_button = self.driver.find_element(*self.configuration.EventDetailsScreen.MORE_BUTTON)
    #     self.assertIsNotNone(more_button, "More button was not found")
    #     more_button.click()
    #     sleep(0.5)
    #
    #     self.switch_context_to_native()

    def click_edit_button(self):

        logging.info("edit previously created event")

        try:
            self.driver.find_element(*self.configuration.EventDetailsScreen.EVENT_INFO_BUTTON).click()
        except NoSuchElementException:
            pass

        self.switch_context_to_webview()

        sleep(1)
        edit_button = self.driver.find_element(*self.configuration.EventDetailsScreen.EDIT_BUTTON)
        self.assertIsNotNone(edit_button, "edit button not found")
        edit_button.click()
        sleep(2)

        self.switch_context_to_native()

        sleep(2)

    def set_as_primary_event(self):

        self.switch_context_to_webview()

        logging.info("clicking in 'Set as primary' button")
        set_as_primary_button = self.driver.find_element(*self.configuration.EventDetailsScreen.
                                                         SET_AS_PRIMARY_BUTTON)
        self.assertIsNotNone(set_as_primary_button, "Set as primary button not found")
        set_as_primary_button.click()
        sleep(2)

        self.switch_context_to_native()

    def click_Delete_button(self):

        self.switch_context_to_webview()

        logging.info("clicking in 'Delete event' button")
        delete_event_button = self.driver.find_element(*self.configuration.EventDetailsScreen.DELETE_EVENT_BUTTON)
        self.assertIsNotNone(delete_event_button, "delete event button not found")
        delete_event_button.click()

        self.switch_context_to_native()

    def alert_confirm_delete(self):

        logging.info("confirm delete")
        delete_confirm_button = self.driver.find_element(*self.configuration.EventDetailsScreen.DELETE_CONFIRM_BUTTON)
        self.assertIsNotNone(delete_confirm_button, "confirm delete button not found")
        delete_confirm_button.click()
        sleep(7)

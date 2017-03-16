"""A class for methods to handle Event Details Page """

from Modules.BasePage.BasePage import BasePage
from time import sleep
import logging


class EventDetailsPage(BasePage):

    def click_edit_button(self):

        logging.info("edit previously created event")
        edit_button = self.driver.find_element(*self.configuration.EventDetailsScreen.EDIT_BUTTON)
        self.assertIsNotNone(edit_button, "edit button not found")
        edit_button.click()
        sleep(2)

    def click_Delete_button(self):

        logging.info("clicking in 'Delete event' button")
        delete_event_button = self.driver.find_element(*self.configuration.EventDetailsScreen.DELETE_EVENT_BUTTON)
        self.assertIsNotNone(delete_event_button, "delete event button not found")
        delete_event_button.click()

    def alert_confirm_delete(self):

        logging.info("confirm delete")
        delete_confirm_button = self.driver.find_element(*self.configuration.EventDetailsScreen.DELETE_CONFIRM_BUTTON)
        self.assertIsNotNone(delete_confirm_button, "confirm delete button not found")
        delete_confirm_button.click()
        sleep(7)

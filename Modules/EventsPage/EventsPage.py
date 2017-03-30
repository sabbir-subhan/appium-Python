"""A class for methods to handle Events Page """

from Modules.BasePage.BasePage import BasePage
from time import sleep
import logging


class EventsPage(BasePage):

    def filter_events_by_Search_field(self):

        self.switch_context_to_webview()

        logging.info("search field - search event named: 'search'")
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).click()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).send_keys("search")

        self.switch_context_to_native()

    def clear_Search_field(self):

        self.switch_context_to_webview()

        logging.info("clear search field")
        search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        search_field.clear()

        self.switch_context_to_native()

    def filter_events_to_find_previous_event(self):

        self.switch_context_to_webview()

        logging.info("search field - search event named: 'app'")
        sleep(2)
        search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        search_field.click()
        search_field.send_keys("app")

        self.switch_context_to_native()

    def click_More_button(self):

        self.switch_context_to_webview()

        # sleep(1)
        # logging.info("click 'More' button")
        # more_button = self.driver.find_element(*self.configuration.CommonScreen.SPINNER_ON_THE_RIGHT)
        # self.assertIsNotNone(more_button, "More button was not found")
        # more_button.click()
        # sleep(0.5)
        sleep(1)
        logging.info("click 'More' button")
        more_button = self.driver.find_element(*self.configuration.EventsScreen.MORE_BUTTON)
        self.assertIsNotNone(more_button, "More button was not found")
        more_button.click()
        sleep(0.5)

        self.switch_context_to_native()

    def check_if_EVENTS_were_opened(self):

        sleep(2)
        logging.info("check if Events were opened")
        events_header = self.driver.find_element(*self.configuration.EventsScreen.EVENTS_HEADER)
        self.assertIsNotNone(events_header)

    def filter_events_by_Type(self):

        sleep(1)
        logging.info("filtering events by Type")
        self.driver.find_element(*self.configuration.EventsScreen.ANY_TYPE_EXPAND).click()
        self.driver.find_element(*self.configuration.EventsScreen.CHOOSE_TYPE_INCIDENT).click()
        sleep(1)
        self.driver.find_element(*self.configuration.EventsScreen.INCIDENT_TYPE_EXPAND).click()
        self.driver.find_element(*self.configuration.EventsScreen.CHOOSE_TYPE_ANY).click()
        sleep(1)

    def filter_events_by_Status(self):

        sleep(1)
        logging.info("filtering events by Status")
        self.driver.find_element(*self.configuration.EventsScreen.ANY_STATUS_EXPAND).click()
        self.driver.find_element(*self.configuration.EventsScreen.CHOOSE_ACTIVE_STATUS).click()
        sleep(1)
        self.driver.find_element(*self.configuration.EventsScreen.ACTIVE_STATUS_EXPAND).click()
        self.driver.find_element(*self.configuration.EventsScreen.CHOOSE_INACTIVE_STATUS).click()
        sleep(1)
        self.driver.find_element(*self.configuration.EventsScreen.INACTIVE_STATUS_EXPAND).click()
        self.driver.find_element(*self.configuration.EventsScreen.CHOOSE_DRAFT_STATUS).click()
        sleep(1)
        self.driver.find_element(*self.configuration.EventsScreen.DRAFT_STATUS_EXPAND).click()
        self.driver.find_element(*self.configuration.EventsScreen.CHOOSE_ANY_STATUS).click()
        sleep(1)

    def click_New_event_button(self):

        self.switch_context_to_webview()

        sleep(1)
        logging.info("clicking in New event button")
        new_event_button = self.driver.find_element(*self.configuration.EventsScreen.NEW_EVENT_BUTTON)
        self.assertIsNotNone(new_event_button, "New Event button not found")
        new_event_button.click()
        sleep(0.5)

        self.switch_context_to_native()

    def click_New_sub_event(self):

        logging.info("clicking in 'New sub event' button")
        new_sub_event = self.driver.find_element(*self.configuration.EventDetailsScreen.NEW_SUB_EVENT)
        self.assertIsNotNone(new_sub_event, "New sub event button is not present")
        new_sub_event.click()
        sleep(3)

    def set_as_primary_event(self):

        logging.info("clicking in 'Set as primary' button")
        set_as_primary_button = self.driver.find_element(*self.configuration.EventDetailsScreen.
                                                         SET_AS_PRIMARY_BUTTON)
        self.assertIsNotNone(set_as_primary_button, "Set as primary button not found")
        set_as_primary_button.click()
        sleep(2)

    def open_previously_created_event(self):

        sleep(2)
        logging.info("open created event")
        created_event = self.driver.find_elements(*self.configuration.EventsScreen.PREVIOUSLY_CREATED_EVENT)
        created_event[0].click()
        sleep(5)
        # sleep(2)
        # logging.info("open created event")
        # created_event = self.driver.find_element(*self.configuration.EventsScreen.PREVIOUSLY_CREATED_EVENT)
        # self.assertIsNotNone(created_event, "Previously created event not found")
        # created_event.click()
        # sleep(5)

    # def open_previously_created_event2(self):
    #
    #     logging.info("open previously created Event, Edit and Create mapping data")
    #     created_event2 = self.driver.find_element(*self.configuration.EventsScreen.CREATED_EVENT_2)
    #     self.assertIsNotNone(created_event2, "Created event 2 not found")
    #     created_event2.click()
    #     sleep(5)

    # def open_previously_created_event3(self):
    #
    #     logging.info("open previously created Event, Edit and Create mapping data")
    #     created_event3 = self.driver.find_element(*self.configuration.EventsScreen.CREATED_EVENT_3)
    #     self.assertIsNotNone(created_event3, "Created event 3 not found")
    #     created_event3.click()
    #     sleep(5)

    # only for events list, opened from chooser fields inside other event
    # def click_on_previously_created_event_for_chooser_field(self):
    #
    #     sleep(5)
    #     logging.info("click_on_previously_created_event_for_chooser_field")
    #     event_for_chooser_field = self.driver.find_element(*self.configuration.EventEditScreen.
    #                                                        PREVIOUSLY_CREATED_EVENT_FOR_CHOOSER)
    #     self.assertIsNotNone(event_for_chooser_field, "event_for_chooser_field not found")
    #     event_for_chooser_field.click()
    #     sleep(5)
    #
    # def click_on_previously_created_event_for_subform_chooser(self):
    #
    #     sleep(10)
    #     logging.info("click_on_previously_created_event_for_subform_chooser")
    #     event_for_subform = self.driver.find_element(*self.configuration.EventEditScreen.
    #                                                  PREVIOUSLY_CREATED_EVENT_FOR_CHOOSER)
    #     self.assertIsNotNone(event_for_subform, "event_for_subform not found")
    #     event_for_subform.click()
    #     sleep(5)



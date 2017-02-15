"""A class for methods to handle Events Types Page """

from Modules.BasePage.BasePage import BasePage
from time import sleep
import logging


class EventsTypesPage(BasePage):

    def choose_Incident_type_of_event(self):

        event_type_incident = self.driver.find_element(*self.configuration.TypesOfEventsScreen.INCIDENT_TYPE_OF_EVENT)
        self.assertIsNotNone(event_type_incident, "event type Incident not found")
        logging.info("choosing Incident type of new event")
        event_type_incident.click()

    def choose_Event_for_on_load_save_type_of_event(self):

        event_type_onload = self.driver.find_element(*self.configuration.TypesOfEventsScreen.EVENT_FOR_ON_LOAD_SAVE)
        self.assertIsNotNone(event_type_onload, "event type onload not found")
        logging.info("choose type of event = event_for_on_load/save_test")
        event_type_onload.click()

    def choose_Event_for_chooser_fields_type_of_event(self):

        event_type_chooser = self.driver.find_element(*self.configuration.TypesOfEventsScreen.EVENT_FOR_CHOOSER_FIELDS)
        self.assertIsNotNone(event_type_chooser, "event type chooser not found")
        logging.info("choose type of event = event for chooser fields")
        event_type_chooser.click()
        sleep(5)


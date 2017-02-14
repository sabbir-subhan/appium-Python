"""A class for methods to handle Main Page """

import logging
from time import sleep
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Modules.BasePage.BasePage import BasePage


class MainPage(BasePage):

    def dismiss_notifications(self):

        logging.info("dismiss notifications")
        try:
            notification_msg_on = self.driver.find_element(*self.configuration.LoginScreen.
                                                           NOTIFICATION_ABOUT_SENDING_MESSAGES)
            if notification_msg_on.is_displayed():
                logging.info("click 'No' for sending notifications")
                notification_msg_on = self.driver.find_element(
                    *self.configuration.LoginScreen.NOTIFICATION_ABOUT_SENDING_MESSAGES)
                self.assertIsNotNone(notification_msg_on, "Notification msg not found")
                self.driver.find_element(*self.configuration.LoginScreen.NO_FOR_SENDING_NOTIFICATIONS_ON).click()
            else:
                pass
        except NoSuchElementException:
            logging.info("notifications alert not present")

    def logout_if_already_logged_in(self):

        sleep(5)
        logging.info("logout if already logged in")
        try:
            logout_button = self.driver.find_element(*self.configuration.MainMenuScreen.LOGOUT_BUTTON)
            self.assertIsNotNone(logout_button, "Logout button not found")
            logging.info("Your are already logged in - logging out")
            logout_button.click()
            submit_button = self.driver.find_element(*self.configuration.LoginScreen.SUBMIT_BUTTON)
            self.assertIsNotNone(submit_button, "Submit button not found")
            submit_button.click()
            sleep(7)
        except NoSuchElementException:
            logging.info("Your are already logged out")

    def alert_expiring_password(self):

        logging.info("check if Notice alert, about expiring password, is present")
        try:
            self.driver.find_element(*self.configuration.LoginScreen.ALERT_MSG_WILL_EXPIRE)
            self.assertIsNotNone(*self.configuration.LoginScreen.ALERT_MSG_WILL_EXPIRE)
            logging.info("Notice alert is present")
            self.driver.find_element(*self.configuration.LoginScreen.OK_BUTTON).click()
        except NoSuchElementException:
            logging.info("Notice alert is not present")
            pass

    def check_presence_of_events_button(self):

        try:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located(self.configuration.MainMenuScreen.EVENTS_BUTTON),
                "Events button in Main Menu is not present")
            logging.info("Events button in Main Menu is present")
        except NoSuchElementException:
            logging.info("Events button in Main Menu is not present")
            self.fail("Events button in Main Menu is not present")

    def click_ACTIVATE_BUTTON_on_alert(self):

        logging.info("clicking in ACTIVATE button on alert")
        alert_activate_button = self.driver.find_element(*self.configuration.MainMenuScreen.ALERT_ACTIVATE_BUTTON)
        self.assertIsNotNone(alert_activate_button, "ACTIVATE button on alert not found")
        alert_activate_button.click()
        sleep(2)

    def check_if_alert_WORKFLOW_ACTIVATED_is_present(self):

        logging.info("check if alert 'Workflow activated' is present and click 'Ok'")
        alert_workflow_activated = self.driver.find_element(*self.configuration.MainMenuScreen.ALERT_WORKFLOW_ACTIVATED)
        self.assertIsNotNone(alert_workflow_activated, "alert WORKFLOW ACTIVATED is not present")
        self.driver.find_element(*self.configuration.LoginScreen.OK_BUTTON).click()

    def click_ACTIVATE_WORKFLOW(self):

        logging.info("clicking in ACTIVATE WORKFLOW button")
        activate_workflow_button = self.driver.find_element(*self.configuration.MainMenuScreen.ACTIVATE_WORKFLOW_BUTTON)
        self.assertIsNotNone(activate_workflow_button, "ACTIVATE WORKFLOW button not found")
        activate_workflow_button.click()

    def open_CREATE_CONTACT(self):

        logging.info("clicking in CREATE CONTACT button")
        create_contact_button = self.driver.find_element(*self.configuration.MainMenuScreen.CREATE_CONTACT_BUTTON)
        self.assertIsNotNone(create_contact_button, "CREATE CONTACT button not found")
        create_contact_button.click()

    def open_CREATE_TASK(self):

        logging.info("clicking in CREATE TASK button")
        create_task_button = self.driver.find_element(*self.configuration.MainMenuScreen.CREATE_TASK_BUTTON)
        self.assertIsNotNone(create_task_button, "CREATE TASK button not found")
        create_task_button.click()

    def open_CREATE_REPORT(self):

        logging.info("clicking in CREATE REPORT button")
        create_report_button = self.driver.find_element(*self.configuration.MainMenuScreen.CREATE_REPORT_BUTTON)
        self.assertIsNotNone(create_report_button, "CREATE REPORT button not found")
        create_report_button.click()

    def open_WEBSITE_LINK(self):

        logging.info("clicking in WEBSITE LINK button")
        website_link_button = self.driver.find_element(*self.configuration.MainMenuScreen.WEBSITE_LINK_BUTTON)
        self.assertIsNotNone(website_link_button, "WEBSITE LINK button not found")
        website_link_button.click()

    def open_INCIDENT(self):

        logging.info("clicking in INCIDENT button")
        incident_button = self.driver.find_element(*self.configuration.MainMenuScreen.INCIDENT_BUTTON)
        self.assertIsNotNone(incident_button, "INCIDENT button not found")
        incident_button.click()

    def open_CREATE_ASSETS(self):

        logging.info("clicking in CREATE ASSETS button")
        create_assets_button = self.driver.find_element(*self.configuration.MainMenuScreen.CREATE_ASSETS_BUTTON)
        self.assertIsNotNone(create_assets_button, "CREATE ASSETS button not found")
        create_assets_button.click()

    def open_CREATE_LOG(self):

        logging.info("clicking in CREATE LOG button")
        create_log_button = self.driver.find_element(*self.configuration.MainMenuScreen.CREATE_LOG_BUTTON)
        self.assertIsNotNone(create_log_button, "CREATE LOG button not found")
        create_log_button.click()

    def open_RISKS(self):

        logging.info("clicking in RISKS button")
        risks_button = self.driver.find_element(*self.configuration.MainMenuScreen.RISKS_BUTTON)
        self.assertIsNotNone(risks_button, "RISKS button not found")
        risks_button.click()

    def open_EVENTS(self):

        logging.info("clicking in Events button")
        events_button = self.driver.find_element(*self.configuration.MainMenuScreen.EVENTS_BUTTON)
        self.assertIsNotNone(events_button, "EVENTS button not found")
        events_button.click()
        logging.info("check if Events were opened")
        events_header = self.driver.find_element(*self.configuration.EventsScreen.EVENTS_HEADER)
        self.assertIsNotNone(events_header)

    def open_LOGS(self):

        logging.info("clicking in LOGS button")
        logs_button = self.driver.find_element(*self.configuration.MainMenuScreen.LOGS_BUTTON)
        self.assertIsNotNone(logs_button, "LOGS button not found")
        logs_button.click()

    def open_REPORTS(self):

        logging.info("clicking in REPORTS button")
        reports_button = self.driver.find_element(*self.configuration.MainMenuScreen.REPORTS_BUTTON)
        self.assertIsNotNone(reports_button, "REPORTS button not found")
        reports_button.click()

    def open_MAP(self):

        logging.info("clicking in Map button")
        map_button = self.driver.find_element(*self.configuration.MainMenuScreen.MAP_BUTTON)
        self.assertIsNotNone(map_button, "MAP button not found")
        map_button.click()

    def open_LOCATION(self):

        logging.info("clicking in Location button")
        location_button = self.driver.find_element(*self.configuration.MainMenuScreen.LOCATION_BUTTON)
        self.assertIsNotNone(location_button, "Location button not found")
        location_button.click()

    def open_ASSETS(self):

        logging.info("clicking in ASSETS button")
        assets_button = self.driver.find_element(*self.configuration.MainMenuScreen.ASSETS_BUTTON)
        self.assertIsNotNone(assets_button, "ASSETS button not found")
        assets_button.click()

    def open_MY_MESSAGES(self):
        logging.info("clicking in MY MESSAGES button")
        my_messages_button = self.driver.find_element(*self.configuration.MainMenuScreen.MY_MESSAGES_BUTTON)
        self.assertIsNotNone(my_messages_button, "MY MESSAGES button not found")
        my_messages_button.click()

    def open_INBOX(self):
        logging.info("clicking in INBOX button")
        inbox_button = self.driver.find_element(*self.configuration.MainMenuScreen.INBOX_BUTTON)
        self.assertIsNotNone(inbox_button, "INBOX button not found")
        inbox_button.click()

    def open_COMPOSE(self):
        logging.info("clicking in COMPOSE button")
        compose_button = self.driver.find_element(*self.configuration.MainMenuScreen.COMPOSE_BUTTON)
        self.assertIsNotNone(compose_button, "COMPOSE button not found")
        compose_button.click()

    def open_SENT(self):
        logging.info("clicking in SENT button")
        sent_button = self.driver.find_element(*self.configuration.MainMenuScreen.SENT_BUTTON)
        self.assertIsNotNone(sent_button, "SENT button not found")
        sent_button.click()

    def open_PHOTO(self):

        logging.info("clicking in Photo button")
        photo_button = self.driver.find_element(*self.configuration.MainMenuScreen.PHOTO_BUTTON)
        self.assertIsNotNone(photo_button, "PHOTO button not found")
        photo_button.click()

    def open_VIDEO(self):

        logging.info("clicking in Video button")
        video_button = self.driver.find_element(*self.configuration.MainMenuScreen.VIDEO_BUTTON)
        self.assertIsNotNone(video_button, "VIDEO button not found")
        video_button.click()

    def open_SOUND(self):

        logging.info("clicking in Sound button")
        sound_button = self.driver.find_element(*self.configuration.MainMenuScreen.SOUND_BUTTON)
        self.assertIsNotNone(sound_button, "Sound button not found")
        sound_button.click()

    def open_TASKS(self):

        logging.info("clicking in TASKS button")
        tasks_button = self.driver.find_element(*self.configuration.MainMenuScreen.TASKS_BUTTON)
        self.assertIsNotNone(tasks_button, "TASKS button not found")
        tasks_button.click()

    def open_DOCUMENTS(self):

        logging.info("clicking in DOCUMENTS button")
        documents_button = self.driver.find_element(*self.configuration.MainMenuScreen.DOCUMENTS_BUTTON)
        self.assertIsNotNone(documents_button, "DOCUMENTS button not found")
        documents_button.click()

    def open_CONTACTS(self):

        logging.info("clicking in CONTACTS button")
        contacts_button = self.driver.find_element(*self.configuration.MainMenuScreen.CONTACTS_BUTTON)
        self.assertIsNotNone(contacts_button, "CONTACTS button not found")
        contacts_button.click()

    def open_ALLOCATE(self):

        logging.info("clicking in ALLOCATE button")
        allocate_button = self.driver.find_element(*self.configuration.MainMenuScreen.ALLOCATE_BUTTON)
        self.assertIsNotNone(allocate_button, "ALLOCATE button not found")
        allocate_button.click()

    def open_SETTINGS(self):
        logging.info("clicking in SETTINGS button")
        settings_button = self.driver.find_element(*self.configuration.MainMenuScreen.SETTINGS_BUTTON)
        self.assertIsNotNone(settings_button, "SETTINGS button not found")
        settings_button.click()

    def open_ACTIVATE(self):
        logging.info("clicking in ACTIVATE button")
        activate_button = self.driver.find_element(*self.configuration.MainMenuScreen.ACTIVATE_BUTTON)
        self.assertIsNotNone(activate_button, "ACTIVATE button not found")
        activate_button.click()

    def open_OFFLINE_SYNC(self):
        logging.info("clicking in OFFLINE SYNC button")
        offline_sync_button = self.driver.find_element(*self.configuration.MainMenuScreen.OFFLINE_SYNC_BUTTON)
        self.assertIsNotNone(offline_sync_button, "OFFLINE SYNC button not found")
        offline_sync_button.click()

    def open_ABOUT(self):
        logging.info("clicking in ABOUT button")
        about_button = self.driver.find_element(*self.configuration.MainMenuScreen.ABOUT_BUTTON)
        self.assertIsNotNone(about_button, "ABOUT button not found")
        about_button.click()
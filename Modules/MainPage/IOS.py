""" Methods for IOS to handle Main Page"""

from Modules.MainPage.MainPage import MainPage
import logging
from time import sleep


class IOS(MainPage):

    def scroll_down_to_sent_button(self):

        logging.info("scroll down with loop")
        var = 4
        while var > 0:
            logging.info("check if sent button is visible")
            sent_button = self.driver.find_element(*self.configuration.MainMenuScreen.SENT_BUTTON)
            if sent_button.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                var = var - 1

    def scroll_down_to_photo_button(self):

        logging.info("scroll down with loop")
        var = 4
        while var > 0:
            logging.info("check if photo button is visible")
            photo_button = self.driver.find_element(*self.configuration.WelcomeScreen.PHOTO_BUTTON)
            if photo_button.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                var = var - 1

    def scroll_down_to_video_button(self):

        logging.info("scroll down with loop")
        var = 4
        while var > 0:
            logging.info("check if video button is visible")
            video_button = self.driver.find_element(*self.configuration.WelcomeScreen.VIDEO_BUTTON)
            if video_button.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                var = var - 1

    def scroll_down_to_sound_button(self):

        logging.info("scroll down with loop")
        var = 4
        while var > 0:
            logging.info("check if sound button is visible")
            sound_button = self.driver.find_element(*self.configuration.WelcomeScreen.SOUND_BUTTON)
            if sound_button.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                var = var - 1

    def scroll_down_to_tasks_button(self):

        logging.info("scroll down with loop")
        var = 4
        while var > 0:
            logging.info("check if tasks button is visible")
            tasks_button = self.driver.find_element(*self.configuration.MainMenuScreen.TASKS_BUTTON)
            if tasks_button.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                var = var - 1

    def scroll_down_to_documents_button(self):

        logging.info("scroll down with loop")
        var = 4
        while var > 0:
            logging.info("check if documents button is visible")
            documents_button = self.driver.find_element(*self.configuration.MainMenuScreen.DOCUMENTS_BUTTON)
            if documents_button.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                var = var - 1

    def scroll_down_to_contacts_button(self):

        logging.info("scroll down with loop")
        var = 4
        while var > 0:
            logging.info("check if contacts button is visible")
            contacts_button = self.driver.find_element(*self.configuration.MainMenuScreen.CONTACTS_BUTTON)
            if contacts_button.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                var = var - 1

    def scroll_down_to_allocate_button(self):

        logging.info("scroll down with loop")
        var = 4
        while var > 0:
            logging.info("check if allocate button is visible")
            allocate_button = self.driver.find_element(*self.configuration.MainMenuScreen.ALLOCATE_BUTTON)
            if allocate_button.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                var = var - 1

    def scroll_down_to_settings_button(self):

        logging.info("scroll down with loop")
        var = 4
        while var > 0:
            logging.info("check if settings button is visible")
            settings_button = self.driver.find_element(*self.configuration.WelcomeScreen.SETTINGS_BUTTON)
            if settings_button.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                var = var - 1

    def scroll_down_to_active_button(self):

        logging.info("scroll down with loop")
        var = 4
        while var > 0:
            logging.info("check if active button is visible")
            active_button = self.driver.find_element(*self.configuration.MainMenuScreen.ACTIVE_BUTTON)
            if active_button.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                var = var - 1

    def scroll_down_to_offline_sync_button(self):

        logging.info("scroll down with loop")
        var = 4
        while var > 0:
            logging.info("check if offline sync button is visible")
            offline_sync_button = self.driver.find_element(*self.configuration.MainMenuScreen.OFFLINE_SYNC_BUTTON)
            if offline_sync_button.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                var = var - 1

    def scroll_down_to_about_button(self):

        logging.info("scroll down with loop")
        var = 4
        while var > 0:
            logging.info("check if about button is visible")
            about_button = self.driver.find_element(*self.configuration.WelcomeScreen.ABOUT_BUTTON)
            if about_button.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                var = var - 1

    def scroll_down_to_logout_button(self):

        logging.info("scroll down with loop")
        var = 4
        while var > 0:
            logging.info("check if logout button is visible")
            logout_button = self.driver.find_element(*self.configuration.MainMenuScreen.LOGOUT_BUTTON)
            if logout_button.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                var = var - 1

    def scroll_up_to_reports_button(self):

        logging.info("scroll up with loop")
        var = 4
        while var > 0:
            logging.info("check if reports button is visible")
            reports_button = self.driver.find_element(*self.configuration.MainMenuScreen.REPORTS_BUTTON)
            if reports_button.is_displayed():
                break
            else:
                logging.info("scroll up")
                self.driver.execute_script("mobile: scroll", {"direction": "up"})
                var = var - 1

    def scroll_up_to_events_button(self):

        logging.info("scroll up")
        sleep(1)
        var = 4
        while var > 0:
            logging.info("check if events button is visible")
            events_button = self.driver.find_element(*self.configuration.MainMenuScreen.EVENTS_BUTTON)
            if events_button.is_displayed():
                break
            else:
                logging.info("scroll up")
                self.driver.execute_script("mobile: scroll", {"direction": "up"})
                var = var - 1







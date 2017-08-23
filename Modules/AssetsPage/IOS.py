""" Methods for IOS to handle Assets Page """

from Modules.AssetsPage.AssetsPage import AssetsPage
import logging
from selenium.common.exceptions import NoSuchElementException


class IOS(AssetsPage):

    def scroll_down_to_save_button(self):
        """Method to scroll down to bottom of the screen - to 'Save' button"""

        logging.info("scroll down to Save button")
        scroll = 20
        while scroll > 0:
            logging.info("check if save button is visible")
            try:
                save_button = self.driver.find_element(*self.configuration.CommonScreen.SAVE_BUTTON)
                if save_button.is_displayed():
                    logging.info("save button is visible")
                    break
                else:
                    logging.info("scroll down to save button")
                    self.driver.execute_script("mobile: scroll", {"direction": "down"})
                    scroll = scroll - 1
            except NoSuchElementException:
                logging.info("scroll down to save button")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                scroll = scroll - 1

    # def scroll_down_to_save_button(self):
    #     """Method to scroll down to bottom of the screen - to 'Save' button"""
    #
    #     logging.info("scroll down to Save button")
    #     scroll = 20
    #     while scroll > 0:
    #         logging.info("check if save button is visible")
    #         save_button = self.driver.find_element(*self.configuration.CommonScreen.SAVE_BUTTON)
    #         if save_button.is_displayed():
    #             logging.info("save button is visible")
    #             break
    #         else:
    #             logging.info("scroll down to save button")
    #             self.driver.execute_script("mobile: scroll", {"direction": "down"})
    #             scroll = scroll - 1

    def scroll_down_to_add_media_button(self):
        """Method to scroll down to 'Add Media' button"""

        logging.info("scroll down to Add Media button")
        scroll = 10
        while scroll > 0:
            logging.info("check if Add Media button is visible")
            add_media_button = self.driver.find_element(*self.configuration.CommonScreen.ADD_MEDIA)
            if add_media_button.is_displayed():
                break
            else:
                logging.info("scroll down to Add Media button")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                scroll = scroll - 1

    def scroll_up_to_name_field(self):
        """Method to scroll up to 'Name' input field"""

        logging.info("scroll down to Name input field")
        self.switch_context_to_native()
        scroll = 10
        while scroll > 0:
            logging.info("check if Name input field is visible")
            try:
                name_input_field = self.driver.find_element(*self.configuration.CommonScreen.FIRST_INPUT_FIELD)
                if name_input_field.is_displayed():
                    break
                else:
                    logging.info("scroll up to Name input field")
                    self.driver.execute_script("mobile: scroll", {"direction": "up"})
                    scroll = scroll - 1
            except NoSuchElementException:
                logging.warning("first input field not found")
                pass

    # def scroll_up_to_name_field(self):
    #     """Method to scroll up to 'Name' input field"""
    #
    #     logging.info("scroll down to Name input field")
    #     scroll = 10
    #     while scroll > 0:
    #         logging.info("check if Name input field is visible")
    #         name_input_field = self.driver.find_element(*self.configuration.CommonScreen.FIRST_INPUT_FIELD)
    #         # name_input_field = self.driver.find_elements(*self.configuration.CommonScreen.FIRST_INPUT_FIELD)
    #         # if name_input_field[0].is_displayed():
    #         if name_input_field.is_displayed():
    #             break
    #         else:
    #             logging.info("scroll up to Name input field")
    #             self.driver.execute_script("mobile: scroll", {"direction": "up"})
    #             scroll = scroll - 1

    def scroll_down(self):

        logging.info("scroll down")
        self.driver.execute_script("mobile: scroll", {"direction": "down"})
        self.driver.execute_script("mobile: scroll", {"direction": "down"})
        self.driver.execute_script("mobile: scroll", {"direction": "down"})
        
    def scroll_up(self):

        logging.info("scroll up")
        self.driver.execute_script("mobile: scroll", {"direction": "up"})
        self.driver.execute_script("mobile: scroll", {"direction": "up"})
        self.driver.execute_script("mobile: scroll", {"direction": "up"})

    # def read_only_option_list(self):
    #
    #     logging.info("click option list - Is Read Only ?")
    #
    #     sleep(1)
    #     option_list = self.driver.find_element(*self.configuration.AssetsScreen.OPTION_LIST_READ_ONLY_IOS)
    #     self.assertIsNot(option_list, "option list - Is Read Only ?, not found")
    #     action = TouchAction(self.driver)
    #     action.tap(element=option_list, count=1).perform()
    #     sleep(1)

    def scroll_down_to_second_set_of_fields(self):

        logging.info("scrolling down to second set of fields")

        scroll = 7
        while scroll > 0:
            logging.info("check if field is visible")
            field = self.driver.find_element(*self.configuration.AssetsScreen.NEW_PHONE_NUMBER2)
            if field.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                scroll = scroll - 1



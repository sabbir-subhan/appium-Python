""" Methods for IOS to handle Events Page """

from Modules.EventsPage.EventsPage import EventsPage
import logging
from time import sleep
from Modules.load_class import LoadClass
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from configuration import platform


class IOS(EventsPage):

    def type_text_into_search_field(self, text):

        logging.info("type text into search field")

        search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        self.assertIsNotNone(search_field, "Search field not found")
        search_field.click()
        sleep(1)
        search_field.send_keys(text)
        sleep(1)

    def click_severity_lvl_picker_for_edit_event(self):

        sleep(1)
        logging.info("click on severity level picker")
        severity_picker = self.driver.find_element(*self.configuration.EventEditScreen.SEVERITY_LEVEL_SELECTOR)
        self.assertIsNotNone(severity_picker, "Lodging Agency picker was not found")
        action = TouchAction(self.driver)
        sleep(1)
        action.tap(element=severity_picker, count=1).perform()
        sleep(1)

    def click_severity_lvl_picker(self):

        IOS.click_severity_lvl_picker_for_edit_event(self)
        # sleep(1)
        # logging.info("click on severity level picker")
        # severity_picker = self.driver.find_element(*self.configuration.EventEditScreen.SEVERITY_LEVEL_SELECTOR)
        # self.assertIsNotNone(severity_picker, "Lodging Agency picker was not found")
        # action = TouchAction(self.driver)
        # sleep(1)
        # action.tap(element=severity_picker, count=1).perform()
        # sleep(1)

    # def filter_events_by_Search_field(self):
    #
    #     logging.info("search field - search event named: 'search'")
    #     self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).click()
    #     self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
    #     self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).send_keys("search")
    #
    # def filter_events_to_find_previous_event(self):
    #
    #     logging.info("search field - search event named: 'app'")
    #     self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).click()
    #     self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
    #     self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).send_keys("app")

    # def clear_Search_field(self):
    #
    #     logging.info("clear search field")
    #     self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).click()
    #     self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
    #     sleep(1)

    # def click_More_button(self):
    #
    #     sleep(1)
    #     logging.info("clicking in More button")
    #     more_button = self.driver.find_element(*self.configuration.EventsScreen.MORE_BUTTON)
    #     self.assertIsNotNone(more_button, "More button not found")
    #     more_button.click()

        # location = more_button.location
        # print(location)
        # x = location["x"]
        # y = location["y"]
        # print(x)
        # print(y)
        # positions = [(x, y)]
        # self.driver.tap(positions)

    # def clear_primary_event(self):
    #
    #     logging.info("clicking in 'Clear primary event' button")
    #     clear_primary_event_button = self.driver.find_element(*self.configuration.EventsScreen.
    #                                                           CLEAR_PRIMARY_EVENT_BUTTON)
    #     self.assertIsNotNone(clear_primary_event_button, "Clear primary event button not found")
    #     clear_primary_event_button.click()
    #     try:
    #         logging.info("checking notification - 'Primary event cleared'")
    #         sleep(1)
    #         notification = self.driver.find_element(*self.configuration.EventsScreen.NOTIFICATION_PRIMARY_EVENT_CLEARED)
    #         self.assertIsNotNone(notification)
    #     except NoSuchElementException:
    #         logging.info("notification not found")

    def type_text_into_description_field(self):

        # self.switch_context_to_webview()  # webview is not working on iOS10

        sleep(2)
        logging.info("type some text into description field")
        description_field = self.driver.find_element(*self.configuration.EventEditScreen.DESCRIPTION_FIELD)
        description_field.click()
        description_field.send_keys("test appium")

    def scroll_down_to_write_access_level(self):
        """Method to scroll down to write access level"""

        logging.info("scroll down to write access level")
        scroll = 20
        while scroll > 0:
            logging.info("check if write access level is visible")
            write_access_level = self.driver.find_element(*self.configuration.CommonScreen.WRITE_ACCESS_LEVEL)
            if write_access_level.is_displayed():
                break
            else:
                logging.info("scroll down to write access level")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                scroll = scroll - 1

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
        sleep(1)
        # else:
        #     pass

    # def fill_Name_input_field(self, text):
    #
    #     logging.info("fill Name input field")
    #     try:
    #         name_field = self.driver.find_element(*self.configuration.EventEditScreen.NAME_FIELD)
    #         if name_field.is_displayed():
    #             name_field.click()
    #             name_field.send_keys(text)
    #     except NoSuchElementException:
    #         name_field_by_index = self.driver.find_element(*self.configuration.EventEditScreen.NAME_FIELD_by_index)
    #         if name_field_by_index.is_displayed():
    #             name_field_by_index.click()
    #             name_field_by_index.send_keys(text)

    # def click_severity_lvl_picker(self):  # not working for iOS 10
    #
    #     sleep(1)
    #
    #     logging.info("click on severity level field")
    #     self.driver.find_element(*self.configuration.EventEditScreen.SEVERITY_LEVEL_SELECTOR).click()
    #
    # click_severity_lvl_picker_for_edit_event = click_severity_lvl_picker

    def choose_severity_level_1(self):

        logging.info("choose severity level 1")
        try:
            choose_severity_lvl1 = self.driver.find_element(*self.configuration.EventEditScreen.
                                                            CHOOSE_SEVERITY_LVL1_iPad)
            self.assertIsNotNone(choose_severity_lvl1, "severity level 1 not found")
            choose_severity_lvl1.click()
        except NoSuchElementException:
            picker_wheel = self.driver.find_element(*self.configuration.CommonScreen.PICKER_WHEEL)
            picker_wheel.send_keys('Severity 1')
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.done_button()

    def choose_severity_level_2(self):

        logging.info("choose severity level 2")
        try:
            choose_severity_lvl2 = self.driver.find_element(*self.configuration.EventEditScreen.
                                                            CHOOSE_SEVERITY_LVL2_iPad)
            self.assertIsNotNone(choose_severity_lvl2, "severity level 2 not found")
            choose_severity_lvl2.click()
        except NoSuchElementException:
            picker_wheel = self.driver.find_element(*self.configuration.CommonScreen.PICKER_WHEEL)
            picker_wheel.send_keys('Severity 2')
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.done_button()

    def choose_severity_level_3(self):

        logging.info("choose severity level 3")
        try:
            choose_severity_lvl3 = self.driver.find_element(*self.configuration.EventEditScreen.
                                                            CHOOSE_SEVERITY_LVL3_iPad)
            self.assertIsNotNone(choose_severity_lvl3, "severity level 3 not found")
            choose_severity_lvl3.click()
        except NoSuchElementException:
            picker_wheel = self.driver.find_element(*self.configuration.CommonScreen.PICKER_WHEEL)
            picker_wheel.send_keys('Severity 3')
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.done_button()

    def choose_severity_level_4(self):

        logging.info("choose severity level 4")
        try:
            choose_severity_lvl4 = self.driver.find_element(*self.configuration.EventEditScreen.
                                                            CHOOSE_SEVERITY_LVL4_iPad)
            self.assertIsNotNone(choose_severity_lvl4, "severity level 4 not found")
            choose_severity_lvl4.click()
        except NoSuchElementException:
            picker_wheel = self.driver.find_element(*self.configuration.CommonScreen.PICKER_WHEEL)
            picker_wheel.send_keys('Severity 4')
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.done_button()

    def choose_severity_level_5(self):

        logging.info("choose severity level 5")
        try:
            choose_severity_lvl = self.driver.find_element(*self.configuration.EventEditScreen.CHOOSE_SEVERITY_LVL5_iPad)
            self.assertIsNotNone(choose_severity_lvl, "severity level 5 not found")
            choose_severity_lvl.click()
        except NoSuchElementException:
            picker_wheel = self.driver.find_element(*self.configuration.CommonScreen.PICKER_WHEEL)
            picker_wheel.send_keys("Severity 5")
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.done_button()

    def scroll_down_to_description_field(self):

        logging.info("scroll down to description field")
        var = 20
        while var > 0:
            logging.info("check if description field is visible")
            description_field = self.driver.find_element(*self.configuration.EventEditScreen.DESCRIPTION_FIELD)
            if description_field.is_displayed():
                break
            else:
                logging.info("scroll down to description field")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                var = var - 1

    # def type_text_into_description_field(self):
    #
    #     try:
    #         logging.info("type some text into description field")
    #         self.driver.find_element(*self.configuration.EventEditScreen.DESCRIPTION_FIELD).click()
    #         self.driver.find_element(*self.configuration.EventEditScreen.DESCRIPTION_FIELD).send_keys("test ios")
    #     except NoSuchElementException:
    #         logging.info("text field couldn't be selected")
    #         pass

    def scroll_down_to_option_list(self):

        logging.info("scroll down to option_list")
        var = 20
        while var > 0:
            logging.info("check if option list is visible")
            option_list = self.driver.find_element(*self.configuration.EventEditScreen.NEW_OPTION_LIST_HEADER)
            if option_list.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                var = var - 1

    def click_on_option_list(self):

        logging.info("click on option list")
        new_option_list = self.driver.find_element(*self.configuration.EventEditScreen.NEW_OPTION_LIST_HEADER)
        self.assertIsNotNone(new_option_list)
        new_option_list.click()

    def scroll_down_to_add_row_button(self):

        sleep(2)
        logging.info("scroll down with loop")
        var = 20
        while var > 0:
            logging.info("check if add row button is visible")
            subform_field = self.driver.find_element(*self.configuration.EventEditScreen.SUBFORM_FIELD_ADD_ROW)
            if subform_field.is_displayed():
                break
            else:
                logging.info("scroll down to add row button")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                var = var - 1

    # # only for event type: "event_for_on_load/save_test"
    # def click_button_add_row(self):
    #
    #     logging.info("click button Add row")
    #     add_row = self.driver.find_element(*self.configuration.EventEditScreen.SUBFORM_FIELD_ADD_ROW)
    #     self.assertIsNotNone(add_row, "add_row button not found")
    #     add_row.click()

    def scroll_down_to_event_chooser_field(self):

        logging.info("scroll down with loop")
        var = 20
        while var > 0:
            logging.info("check if event_chooser_field is visible")
            save_button = self.driver.find_element(*self.configuration.EventEditScreen.CHOOSER_FIELD)
            if save_button.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                var = var - 1

    # def delete_chosen_event_inside_subform(self):
    #
    #     logging.info("delete chosen event inside sub form")
    #     try:
    #         delete_x = self.driver.find_element(*self.configuration.EventEditScreen.DELETE_SUB_EVENT_FROM_CHOOSER)
    #         if delete_x.is_displayed():
    #             delete_x.click()
    #         else:
    #             location = delete_x.location
    #             print(location)
    #             x = location["x"]
    #             y = location["y"]
    #             print(x)
    #             print(y)
    #             positions = [(x, y)]
    #             self.driver.tap(positions)
    #     except NoSuchElementException:
    #         pass

    def click_on_option_1(self):

        logging.info("choose '1' in option list")
        try:
            option_1 = self.driver.find_element(*self.configuration.EventEditScreen.OPTION_LIST_VALUE_1)
        except NoSuchElementException:
            option_1 = self.driver.find_element(*self.configuration.EventEditScreen.OPTION_LIST_VALUE_1_iPad)
        self.assertIsNotNone(option_1, "option list - option '1' not found")
        # option_1.click()
        action = TouchAction(self.driver)
        action.tap(element=option_1, count=1).perform()

    def click_on_option_2(self):

        logging.info("choose '2' in option list")
        try:
            option_2 = self.driver.find_element(*self.configuration.EventEditScreen.OPTION_LIST_VALUE_2)
        except NoSuchElementException:
            option_2 = self.driver.find_element(*self.configuration.EventEditScreen.OPTION_LIST_VALUE_2_iPad)
        self.assertIsNotNone(option_2, "option list - option '2' not found")
        # option_2.click()
        action = TouchAction(self.driver)
        action.tap(element=option_2, count=1).perform()

    def click_on_option_3(self):

        logging.info("choose '3' in option list")
        try:
            option_3 = self.driver.find_element(*self.configuration.EventEditScreen.OPTION_LIST_VALUE_3)
        except NoSuchElementException:
            option_3 = self.driver.find_element(*self.configuration.EventEditScreen.OPTION_LIST_VALUE_3_iPad)
        self.assertIsNotNone(option_3, "option list - option '3' not found")
        # option_3.click()
        action = TouchAction(self.driver)
        action.tap(element=option_3, count=1).perform()

    def click_save_offline_event(self):

        logging.info("click Save button")

        if "emulator" in platform:  # there is no automatic way to disable networking on iOS emulators
            save_button_native = self.driver.find_element(*self.configuration.EventEditScreen.SAVE_BUTTON)
            self.assertIsNotNone(save_button_native, "Save button not found")
            save_button_native.click()
            try:
                self.switch_context_to_webview()
                save_button = self.driver.find_element(*self.configuration.EventEditScreen.SAVE_BUTTON_EDIT_EVENT)
                self.assertIsNotNone(save_button, "Save button not found")
                save_button.click()
                self.switch_context_to_native()
            except NoSuchElementException:
                pass
        else:
            try:
                save_button_native = self.driver.find_element(*self.configuration.EventEditScreen.SAVE_BUTTON)
                self.assertIsNotNone(save_button_native, "Save button not found")
                save_button_native.click()
            except NoSuchElementException:
                self.switch_context_to_webview()
                save_button = self.driver.find_element(*self.configuration.EventEditScreen.SAVE_BUTTON_NEW_EVENT)
                self.assertIsNotNone(save_button, "Save button not found")
                save_button.click()
                self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

    def open_first_pending_event(self):  # pending event in offline mode

        logging.info("open first pending event on the list")

        if "emulator" in platform:  # there is no automatic way to disable networking on iOS emulators
            contacts_page = LoadClass.load_page('EventsPage')
            contacts_page.setDriver(self.driver)
            contacts_page.clear_Search_field()
            contacts_page.type_text_into_search_field("Offline Object - Event")
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.click_Return_button_on_keyboard()
            common_page.hide_keyboard()
            contacts_page.open_previously_created_event()
        else:
            self.switch_context_to_webview()
            first_pending_event = self.driver.find_element(*self.configuration.EventsScreen.FIRST_PENDING_EVENT)
            self.assertIsNotNone(first_pending_event, "first pending event not found")
            first_pending_event.click()
            self.switch_context_to_native()

    # def click_on_lodging_agency_picker(self):
    #
    #     logging.info("click on 'Lodging Agency' picker")
    #     lodging_agency_picker = self.driver.find_element(*self.configuration.EventEditScreen.LODGING_AGENCY_PICKER)
    #     self.assertIsNotNone(lodging_agency_picker, "Lodging Agency picker was not found")
    #     action = TouchAction(self.driver)
    #     sleep(1)
    #     action.tap(element=lodging_agency_picker, count=1).perform()
    #     sleep(1)





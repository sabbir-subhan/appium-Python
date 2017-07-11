""" Methods for IOS 9 to handle Events Page"""

from Modules.EventsPage.IOS import IOS
import logging
from time import sleep


class IOS9(IOS):

    def click_severity_lvl_picker_for_edit_event(self):

        sleep(1)

        self.switch_context_to_webview()

        logging.info("click on severity level field")
        severity_picker = self.driver.find_element(*self.configuration.EventEditScreen.
                                                   SEVERITY_LEVEL_SELECTOR_EDIT_EVENT)
        self.assertIsNotNone(severity_picker, "severity picker for edited event not found")
        severity_picker.click()

        self.switch_context_to_native()

    def scroll_down_to_save_button(self):

        pass

    def scroll_down_to_event_chooser_field(self):

        pass

    def scroll_down_to_add_row_button(self):

        pass

    def scroll_down_to_option_list(self):

        pass

    def scroll_down_to_description_field(self):

        pass


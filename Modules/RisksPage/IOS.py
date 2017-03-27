"""A class for methods to handle Risks Page on iOS"""

from Modules.RisksPage.RisksPage import RisksPage
from Modules.load_class import LoadClass
import logging


class IOS(RisksPage):

    def scroll_down_to_save_button(self):

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.scroll_down_to_save_button()

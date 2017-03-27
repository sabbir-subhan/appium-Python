"""A class for methods to handle Risks Page """

from Modules.RisksPage.RisksPage import RisksPage
from Modules.load_class import LoadClass
import logging


class Android(RisksPage):

    def scroll_down_to_save_button(self):

        event_edit_page = LoadClass.load_page('CommonPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.scroll_down_one_view()

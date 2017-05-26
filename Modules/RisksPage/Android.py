"""A class for methods to handle Risks Page """

from Modules.RisksPage.RisksPage import RisksPage
from Modules.load_class import LoadClass
import logging
from time import sleep


class Android(RisksPage):

    def scroll_down_to_save_button(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()
        common_page.scroll_down_one_view()

    def choose_status_implemented(self):

        logging.info("choose status implemented")
        choose_status_implemented = self.driver.find_element(*self.configuration.RisksScreen.CHOOSE_STATUS_IMPLEMENTED)
        choose_status_implemented.click()
        sleep(1)

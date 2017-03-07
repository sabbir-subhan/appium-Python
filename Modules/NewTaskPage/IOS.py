""" Methods for IOS to handle New Task Page """

from Modules.NewTaskPage.NewTaskPage import NewTaskPage
from Modules.load_class import LoadClass
import logging


class IOS(NewTaskPage):

    def choose_current_date(self):

        logging.info('choose current date')
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.done_button()


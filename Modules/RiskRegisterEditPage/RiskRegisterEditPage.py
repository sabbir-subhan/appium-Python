"""A class for methods to handle Risk Register Edit Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass


class RiskRegisterEditPage(BasePage):

    def fill_Name_input_field(self, text):

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.fill_Name_input_field(text)



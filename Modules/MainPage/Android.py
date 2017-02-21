""" Methods for IOS to handle Main Page"""

from Modules.MainPage.MainPage import MainPage
from Modules.load_class import LoadClass


class Android(MainPage, LoadClass):

    def scroll_down_to_sound_button(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

""" Methods for IOS to handle Main Page"""

from Modules.MainPage.MainPage import MainPage
from Modules.load_class import LoadClass


class Android(MainPage):

    def scroll_down_to_sent_button(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

    def scroll_down_to_photo_button(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

    def scroll_down_to_video_button(self):
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

    def scroll_down_to_sound_button(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

    def scroll_down_to_tasks_button(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

    def scroll_down_to_documents_button(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

    def scroll_down_to_contacts_button(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

    def scroll_down_to_allocate_button(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

    def scroll_down_to_settings_button(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

    def scroll_down_to_active_button(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

    def scroll_down_to_offline_sync_button(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

    def scroll_down_to_about_button(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

    def scroll_down_to_logout_button(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()
        common_page.scroll_down_one_view()

    def scroll_up_to_reports_button(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_up_one_view()

    def scroll_up_to_events_button(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_up_one_view()






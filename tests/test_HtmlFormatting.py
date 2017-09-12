# Test Case - HTML Formatting on OCA app -- OCAMOB-63


# before running this test create in OCA web page:
# - new event type, with rich text containing image, table and link, name for new event type: "event_with_rich_text",
#  (add some text into first line of rich text field and add few empty lines bellow it/above image - at least 5 lines)
# inside OCA designer add image, table and link into rich text field, image name = "cats.jpg"
# - create new event named: "event_with_image" - use event type created above
#
# - new report type, with rich text containing image, table and link, name for new report type: "report_with_rich_text",
#  (add some text into first line of rich text field and add few empty lines bellow it/above image - at least 5 lines)
# inside OCA designer add image, table and link into rich text field, image name = "everest.jpg"
# - create new report named: "report_with_image" - use report type created above
#
# - new log type, with rich text containing image, table and link
#  (add some text into first line of rich text field and add few empty lines bellow it/above image - at least 5 lines)
#  name for new log type: "log_with_rich_text",
# inside OCA designer add image, table and link into rich text field, image name = "panda.jpg"
# - create new log named: "log_with_image" - use log type created above


# open OCA app
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss notifications
# check if button "EVENTS" is present

# load event created in OCA web page - check presence of image in rich text field
# create new event - choose new type containing rich text field with image, table and link
# open event created in mobile app and check presence of image in rich text field
# switch to landscape view and check presence of image inside rich text field

# repeat steps for report and log


import unittest
import logging
from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
from configuration import PROJECT_ROOT


class TestHtmlFormatting(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        self.driver.save_screenshot(PROJECT_ROOT + "/screenshots/test_HtmlFormatting.png")

        self.driver.quit()

    def test_HtmlFormatting(self):

        logging.info("starting Test Case: HTML Formatting on OCA app")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        welcome_page = LoadClass.load_page('WelcomePage')
        welcome_page.setDriver(self.driver)
        welcome_page.click_login_button()
        login_page = LoadClass.load_page('LoginPage')
        login_page.setDriver(self.driver)
        login_page.type_domain_address('QA')
        common_page.hide_keyboard()
        login_page.click_submit_button()
        login_page.type_username('QA')
        login_page.type_password('QA')
        common_page.hide_keyboard()
        login_page.click_submit_button()
        login_page.accept_terms()
        common_page.wait_for_app_loading()
        main_page = LoadClass.load_page('MainPage')
        main_page.setDriver(self.driver)
        main_page.alert_expiring_password()
        main_page.dismiss_notifications()
        main_page.check_presence_of_events_button()

        # Events
        main_page.open_EVENTS()
        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.clear_Search_field()
        events_page.type_text_into_search_field('event_with_image')
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        events_page.open_previously_created_event()
        common_page.wait_for_app_loading()
        events_page.check_presence_of_image_inside_rich_text_field()
        common_page.take_screenshot('event_rich_text_with_image')
        common_page.rotate_to_landscape_view()
        events_page.check_presence_of_image_inside_rich_text_field()
        common_page.rotate_to_portrait_view()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_EVENTS()
        events_page.click_more_button_in_events_list()
        events_page.click_New_event_button()
        events_page.choose_event_type_with_rich_text()
        events_page.fill_Name_input_field('html_formatting_test')
        events_page.scroll_down_to_save_button()
        events_page.click_save_new_event()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_EVENTS()
        events_page.clear_Search_field()
        events_page.type_text_into_search_field('html_formatting_test')
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        events_page.open_previously_created_event()
        common_page.wait_for_app_loading()
        events_page.check_presence_of_image_inside_rich_text_field()
        common_page.rotate_to_landscape_view()
        events_page.check_presence_of_image_inside_rich_text_field()
        common_page.rotate_to_portrait_view()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Reports
        main_page.open_REPORTS()
        reports_page = LoadClass.load_page('ReportsPage')
        reports_page.setDriver(self.driver)
        reports_page.clear_Search_field()
        reports_page.type_text_into_search_field("report_with_image")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        reports_page.open_existing_report()
        common_page.wait_for_app_loading()
        reports_page.check_presence_of_image_inside_rich_text_field()
        common_page.take_screenshot('report_rich_text_with_image')
        common_page.rotate_to_landscape_view()
        reports_page.check_presence_of_image_inside_rich_text_field()
        common_page.rotate_to_portrait_view()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_REPORTS()
        reports_page.click_create_report_button()
        reports_page.choose_report_type_with_rich_text()
        reports_page.type_title("html_formatting_test")
        reports_page.click_on_lodging_agency_picker()
        reports_page.choose_lodging_agency()
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_new_report()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_REPORTS()
        reports_page.clear_Search_field()
        reports_page.type_text_into_search_field("html_formatting_test")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        reports_page.open_existing_report()
        common_page.wait_for_app_loading()
        reports_page.check_presence_of_image_inside_rich_text_field()
        common_page.rotate_to_landscape_view()
        reports_page.check_presence_of_image_inside_rich_text_field()
        common_page.rotate_to_portrait_view()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Logs
        main_page.open_LOGS()
        logs_page = LoadClass.load_page('LogsPage')
        logs_page.setDriver(self.driver)
        logs_page.clear_Search_field()
        logs_page.type_text_into_search_field("log_with_image")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        logs_page.open_first_log_on_the_list()
        common_page.wait_for_app_loading()
        logs_page.check_presence_of_image_inside_rich_text_field()
        common_page.take_screenshot('log_rich_text_with_image')
        common_page.rotate_to_landscape_view()
        logs_page.check_presence_of_image_inside_rich_text_field()
        common_page.rotate_to_portrait_view()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_LOGS()
        logs_page.create_new_log()
        logs_page.choose_log_type_with_rich_text()
        logs_page.click_on_lodging_agency_picker()
        logs_page.choose_lodging_agency()
        logs_page.type_text_into_entry_field_for_html_formatting("htmlformatting")
        common_page.hide_keyboard()
        logs_page.scroll_down_to_save_button()
        logs_page.click_save_new_log()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_LOGS()
        logs_page.clear_Search_field()
        logs_page.type_text_into_search_field("htmlformatting")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        logs_page.open_first_log_on_the_list()
        common_page.wait_for_app_loading()
        logs_page.check_presence_of_image_inside_rich_text_field()
        common_page.rotate_to_landscape_view()
        logs_page.check_presence_of_image_inside_rich_text_field()
        common_page.rotate_to_portrait_view()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHtmlFormatting)
    unittest.TextTestRunner(verbosity=2).run(suite)

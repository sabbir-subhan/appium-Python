# Test Case - Rich Text Fields in all Objects -- OCAMOB-69

# before running this test create in OCA web page:
# create a new Asset type that has a rich text field and a subform with a rich text field
# - new object type, with rich text containing image, table and link, name for new object type: "asset_with_rich_text",
#  (add some text into first line of rich text field and add few empty lines bellow it/above image - at least 5 lines)
# inside OCA designer add image, table and link into rich text field, image name = "cats.jpg" and add the same
# elements into rich text field inside sub form - image name: "everest.jpg"
# - create new asset named: "asset_with_image" - use asset type created above
# - create new object type for Event just like Asset, first image use: "cats.jpg" and for sub form: "everest.jpg"
# - create new object type for Report just like Asset, but for the first image use: "everest.jpg" and for sub form: "panda.jpg"
# - create new object type for Log just like Asset, but for the first image use: "panda.jpg" (Log can't have sub form)
# - create new object type for Contact Group just like Asset, but for the first image use: "cats.jpg" (Contact Group can't have sub form)
# - create new object type for Contact just like Asset, but for the first image use: "panda.jpg" (Contact can't have sub form)
# (remember to create each one of new objects types on OCA web page)

# open OCA app
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss notifications
# check if button "EVENTS" is present


# Login to the OCA mobile app and click on Assets. Open the asset created above.
# View the rich text fields of the asset.
# Create new asset using type created in OCA.

# Repeat steps for an event.
# Repeat steps for a report.
# Repeat steps for a log.
# Repeat steps for a contact group.
# Repeat steps for a contact.


import unittest
import logging
from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
from configuration import PROJECT_ROOT


class TestRichTextFields(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        self.driver.save_screenshot(PROJECT_ROOT + "/screenshots/test_RichTextFields.png")

        self.driver.quit()

    def test_RichTextFields(self):

        logging.info("starting Test Case: Rich Text Fields")
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

        # Login to the OCA mobile app and click on Assets. Open the asset created above.
        # View the rich text fields of the asset.
        main_page.open_ASSETS()
        assets_page = LoadClass.load_page('AssetsPage')
        assets_page.setDriver(self.driver)
        assets_page.clear_Search_field()
        assets_page.type_text_into_search_field("asset_with_image")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        assets_page.open_existing_asset()
        assets_page.check_presence_of_image_inside_rich_text_field()
        assets_page.check_presence_of_image_inside_rich_text_field_in_subform()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Create new asset using type created in OCA.
        main_page.open_ASSETS()
        assets_page.click_new_button()
        assets_page.click_new_asset()
        assets_page.choose_asset_type_with_rich_text()
        assets_page.fill_Name_input_field("asset_rich_text")
        assets_page.add_subform_row()
        assets_page.scroll_down_to_save_button()
        assets_page.click_save_button()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_ASSETS()
        assets_page.clear_Search_field()
        assets_page.type_text_into_search_field("asset_rich_text")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        assets_page.open_existing_asset()
        assets_page.check_presence_of_image_inside_rich_text_field()
        assets_page.check_presence_of_image_inside_rich_text_field_in_subform()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Repeat steps for an event.
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
        events_page.check_presence_of_image_inside_rich_text_field_in_subform()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_EVENTS()
        events_page.click_more_button_in_events_list()
        events_page.click_New_event_button()
        events_page.choose_event_type_with_rich_text()
        events_page.fill_Name_input_field('event_rich_text')
        # events_page.scroll_down_to_save_button()
        common_page.scroll_down_to_subform_add_row_button()
        events_page.add_subform_row()
        events_page.scroll_down_to_save_button()
        events_page.click_save_new_event()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_EVENTS()
        events_page.clear_Search_field()
        events_page.type_text_into_search_field('event_rich_text')
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        events_page.open_previously_created_event()
        common_page.wait_for_app_loading()
        events_page.check_presence_of_image_inside_rich_text_field()
        events_page.check_presence_of_image_inside_rich_text_field_in_subform()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Repeat steps for a report.
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
        reports_page.check_presence_of_image_inside_rich_text_field_in_subform()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_REPORTS()
        reports_page.click_create_report_button()
        reports_page.choose_report_type_with_rich_text()
        reports_page.type_title("report_rich_text")
        reports_page.click_on_lodging_agency_picker()
        reports_page.choose_lodging_agency()
        common_page.scroll_down_to_subform_add_row_button()
        reports_page.add_subform_row()
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_new_report()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_REPORTS()
        reports_page.clear_Search_field()
        reports_page.type_text_into_search_field("report_rich_text")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        reports_page.open_existing_report()
        common_page.wait_for_app_loading()
        reports_page.check_presence_of_image_inside_rich_text_field()
        reports_page.check_presence_of_image_inside_rich_text_field_in_subform()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Repeat steps for a log.
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
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_LOGS()
        logs_page.create_new_log()
        logs_page.choose_log_type_with_rich_text()
        logs_page.click_on_lodging_agency_picker()
        logs_page.choose_lodging_agency()
        logs_page.type_text_into_entry_field_for_rich_text("logrichtext")
        common_page.hide_keyboard()
        logs_page.scroll_down_to_save_button()
        logs_page.click_save_new_log()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_LOGS()
        logs_page.clear_Search_field()
        logs_page.type_text_into_search_field("logrichtext")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        logs_page.open_first_log_on_the_list()
        common_page.wait_for_app_loading()
        logs_page.check_presence_of_image_inside_rich_text_field()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Repeat steps for a contact group.
        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page = LoadClass.load_page('ContactsPage')
        contacts_page.setDriver(self.driver)
        contacts_page.clear_Search_field()
        contacts_page.type_text_into_search_field("contact_group_with_image")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        contacts_page.open_first_contact_group()
        contacts_page.click_group_info_button()
        common_page.wait_for_app_loading()
        contacts_page.check_presence_of_image_inside_rich_text_field_for_contact_group()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.click_new_button()
        contacts_page.add_new_contact_group()
        contacts_page.choose_group_with_rich_text_type()  # contact_group_with_rich_text
        contacts_page.type_name_for_new_contact_group("contact_group_rich_text")
        contacts_page.scroll_down_to_save_button()
        contacts_page.save_new_contact_group()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.clear_Search_field()
        contacts_page.type_text_into_search_field("contact_group_rich_text")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        contacts_page.open_first_contact_group()
        contacts_page.click_group_info_button()
        common_page.wait_for_app_loading()
        contacts_page.check_presence_of_image_inside_rich_text_field_for_contact_group()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        # Repeat steps for a contact.
        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.clear_Search_field()
        contacts_page.type_text_into_search_field("contact_with_image")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        contacts_page.click_first_contact_on_the_list()
        contacts_page.check_presence_of_image_inside_rich_text_field_for_contact()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.clear_Search_field()
        contacts_page.open_contacts_group()  # Contacts
        contacts_page.click_new_button()
        contacts_page.add_new_contact_into_group()
        contacts_page.choose_contact_type_contact_with_rich_text()
        contacts_page.type_first_name_for_new_contact("contact_rich_text")
        contacts_page.scroll_down_to_save_button()
        contacts_page.save_new_contact()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.clear_Search_field()
        contacts_page.type_text_into_search_field("contact_rich_text")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        contacts_page.click_first_contact_on_the_list()
        contacts_page.check_presence_of_image_inside_rich_text_field_for_contact()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRichTextFields)
    unittest.TextTestRunner(verbosity=2).run(suite)

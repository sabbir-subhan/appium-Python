# Test Case - Read Only Properties -- OCAMOB-33

# before running test case:

# Go to setting > OCA designer > Create object types: Asset, Reports, Event, Risk
# for each new type add the following:
#   - option list: name = Is Read only ?, Options = Yes A, Yes B, No,
#  Maximum selected options = Height of field = 3, Default value = (None)
#   - *Options may come from a central list or a user-defined list

# Add the 2 sets of the following fields
# - phone number ("New phone number" input field should be visible on top of the form - on the first screen after creating new object)
# - option list
# - single-line text
# - multi-line text
# - rich text
# - fax number
# - cell number
# - email address
# - website address
# - location
# - date
# - date & time
# - date & optional time
# - number
# - sub form
# - single-line text inside the sub form

# Make the 1st set of fields Read only if Is Read only ? = Yes A.
# Make the 2nd set of fields visible only if Is Read only ? = Yes B.
# Set up default values for all fields in both sets.


# TEST CASE STEPS:

# open OCA app
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss notifications
# check if button "EVENTS" is present

# create new Asset -> Do not select any options for is read only Y/N ->
# Verify that the second set of fields is hidden
# Set is Read only = Yes A and Yes B
# Check that the 2 sets of fields in step 2 are still Read only while set to their default values.
# Change the value of each field in the 2 sets of fields in step 2 then save the Asset

#  Edit the details of created Asset and Check that the 2 sets of fields in step 4 are still Read only while set to their default values.
#  Change the value of each field in the 2 sets of fields in step 4. Set Is Read only ? != Yes A or Yes B then save the Asset

# 1. Edit the details of #49135 Asset Set Is Read only ? = Yes A and Yes B.

# . Check that the 2 sets of fields in step 2 are still Read only  while set to their values in step 8 (not step 11).

# Repeat the steps for Report
# Repeat the steps for Event
# Repeat the steps for Risk

import unittest
import logging
from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import os
from configuration import PROJECT_ROOT


class TestReadOnlyProperties(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        path = PROJECT_ROOT + "/screenshots"
        os.chdir(path)
        self.driver.save_screenshot("test_ReadOnlyProperties" + ".png")
        os.chdir("..")

        self.driver.quit()

    def test_ReadOnlyProperties(self):

        logging.info("starting Test Case: Read Only Properties")
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

        # create new Asset -> Do not select any options for is read only Y/N
        main_page.open_ASSETS()
        assets_page = LoadClass.load_page('AssetsPage')
        assets_page.setDriver(self.driver)
        assets_page.click_new_button()
        assets_page.click_new_asset()
        assets_page.choose_asset_type_with_option_list()
        assets_page.fill_Name_input_field("Asset for Read Only test")

        # Verify that the second set of fields is hidden
        assets_page.scroll_down_to_add_media_button()
        assets_page.check_invisibility_of_second_set_of_fields_in_asset_with_option_list()
        assets_page.scroll_up_to_name_field()

        # Set is Read only = Yes A and Yes B
        assets_page.read_only_option_list()
        assets_page.option_list_option_yes_a()
        assets_page.option_list_option_yes_b()
        assets_page.save_option_list()

        # Check that the 2 sets of fields in step 2 are still Read only while set to their default values.
        assets_page.check_if_first_set_of_fields_in_asset_with_option_list_is_disabled()  # locator is not working
        # Change the value of each field in the 2 sets of fields in step 2 then save the Asset

        assets_page.scroll_down_to_save_button()
        assets_page.click_save_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReadOnlyProperties)
    unittest.TextTestRunner(verbosity=2).run(suite)

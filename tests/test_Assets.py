# Test Case - Assets -- OCAMOB-50

# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present
# From the main menu click on Assets

# Assets > New > New Asset > Select Type > Create and save
# Asset > open asset > Click on Edit > Update and save
# Asset > Select asset > More > Delete this asset
# Create a Child Asset Asset > Select asset > More > New Child asset > select type > Create asset
# Edit child asset Asset > Select parent > Child is displayed >Select Child > Edit
# Delete child asset Asset > Select parent > Child is displayed >Select Child > More > Delete this asset
# Create an Asset from Map Maps > Layers > Select layers > Tools > Plot a point, line, circle or polygon > Create > Asset > Type > Save
# Click on Assets>Search Assets

# Login to OCA server >Create a new Asset type >Login to OCA mobile app >Click on Assets>New>Select the new asset type created above  -- can't be done using Appium

# Scroll down/Up the Asset list view
# Load an assets with max number of fields
# Click on Asset>Create Asset>New>Select a type>Click on Create mapping data>Add point/line/Circle/Polygon> Click on Add media >Add all files (audio,Video,Document)
# Create an asset that has option lists and fields with visibility rules that clears hidden fields and restores default values.


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest


class TestAssets(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_manage_risks(self):

        logging.info("starting Test Case: Assets")
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

        # Assets > New > New Asset > Select Type > Create and save
        main_page.open_ASSETS()
        assets_page = LoadClass.load_page('AssetsPage')
        assets_page.setDriver(self.driver)
        assets_page.click_new_button()
        assets_page.click_new_asset()
        assets_page.choose_asset_type()
        assets_page.fill_Name_input_field("Asset test")
        # common_page.hide_keyboard()
        assets_page.scroll_down_to_save_button()
        assets_page.click_save_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Asset > open asset > Click on Edit > Update and save
        main_page.open_ASSETS()
        assets_page.open_existing_asset()
        assets_page.click_edit_button()
        assets_page.type_cost_per_unit("2")
        assets_page.scroll_down_to_save_button()
        assets_page.save_edited_asset()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Asset > Select asset > More > Delete this asset
        main_page.open_ASSETS()
        assets_page.open_existing_asset()
        assets_page.click_more_button()
        assets_page.click_delete_this_asset()
        assets_page.alert_accept_delete()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Create a Child Asset Asset > Select asset > More > New Child asset > select type > Create asset
        main_page.open_ASSETS()
        assets_page.open_existing_asset()
        assets_page.click_more_button()  # problem because if asset already have a child there is no MORE button
        assets_page.click_new_child_asset()
        assets_page.choose_asset_type()
        assets_page.fill_Name_input_field("Asset test 2")
        # common_page.hide_keyboard()
        assets_page.scroll_down_to_save_button()
        assets_page.click_save_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Edit child asset Asset > Select parent > Child is displayed >Select Child > Edit
        main_page.open_ASSETS()
        assets_page.open_existing_asset()
        assets_page.open_existing_child_asset()
        assets_page.click_edit_button()
        assets_page.type_cost_per_unit("4")
        assets_page.scroll_down_to_save_button()
        assets_page.save_edited_asset()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()


        # Delete child asset Asset > Select parent > Child is displayed >Select Child > More > Delete this asset
        # Create an Asset from Map Maps > Layers > Select layers > Tools > Plot a point, line, circle or polygon > Create > Asset > Type > Save
        # Click on Assets>Search Assets

        # Login to OCA server >Create a new Asset type >Login to OCA mobile app >Click on Assets>New>Select the new asset type created above  -- can't be done using Appium

        # Scroll down/Up the Asset list view
        # Load an assets with max number of fields
        # Click on Asset>Create Asset>New>Select a type>Click on Create mapping data>Add point/line/Circle/Polygon> Click on Add media >Add all files (audio,Video,Document)
        # Create an asset that has option lists and fields with visibility rules that clears hidden fields and restores default values.


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAssets)
    unittest.TextTestRunner(verbosity=2).run(suite)

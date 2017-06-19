# Test Case - Sort Assets in Alphabetical order  -- OCAMOB-323


# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present
# From the main menu click on Assets

# open Assets
# create new assets with names: #Assets, Assets, Ballarat
# check if assets are sorted alphabetically


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest


class TestSortAssets(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_sort_assets(self):

        logging.info("starting Test Case: Sort Assets in Alphabetical order")
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
        assets_page.fill_Name_input_field("#Asset")
        assets_page.scroll_down_to_save_button()
        assets_page.click_save_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_ASSETS()
        assets_page.click_new_button()
        assets_page.click_new_asset()
        assets_page.choose_asset_type()
        assets_page.fill_Name_input_field("Assets")
        assets_page.scroll_down_to_save_button()
        assets_page.click_save_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_ASSETS()
        assets_page.click_new_button()
        assets_page.click_new_asset()
        assets_page.choose_asset_type()
        assets_page.fill_Name_input_field("Ballarat")
        assets_page.scroll_down_to_save_button()
        assets_page.click_save_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_ASSETS()
        assets_page.click_new_button()
        assets_page.click_new_asset()
        assets_page.choose_asset_type()
        assets_page.fill_Name_input_field("$Asset")
        assets_page.scroll_down_to_save_button()
        assets_page.click_save_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_ASSETS()
        assets_page.click_new_button()
        assets_page.click_new_asset()
        assets_page.choose_asset_type()
        assets_page.fill_Name_input_field("%Asset")
        assets_page.scroll_down_to_save_button()
        assets_page.click_save_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_ASSETS()
        assets_page.click_new_button()
        assets_page.click_new_asset()
        assets_page.choose_asset_type()
        assets_page.fill_Name_input_field("CCC_Asset")
        assets_page.scroll_down_to_save_button()
        assets_page.click_save_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Click on Assets > Search Assets
        main_page.open_ASSETS()
        assets_page.type_text_into_search_field("Ballarat")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        assets_page.check_result_for_asset_with_name_containing_ballart()
        assets_page.clear_Search_field()
        # common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_ASSETS()
        common_page.take_screenshot("Assets_sort_order")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSortAssets)
    unittest.TextTestRunner(verbosity=2).run(suite)

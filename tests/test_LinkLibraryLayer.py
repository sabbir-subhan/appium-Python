# Test Case - Ability to access link library feature layer from mobile app -- OCAMOB-62

# before running this test create in OCA web page:
# create new event with name containing: "map layer" and with point added to map
# create new map with multiple drawing and event - save the map, name: "map_layer_for_appium"
# - Login to oca server > Click on mapping > Draw geometry > Save map as "FOR MOBILE"


# open OCA app
# Login to OCA app
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss notifications
# check if button "EVENTS" is present

# Click on map > Layers > Saved map > Choose the saved map with event


# !!!!!!!!!! can't add below layers: (instead add the layer from TC: test_Maps)
# Login to OCA server - Click on Mapping > Add apple store, DEPI layers, Save map
# Login to OCA app > Click on Map > Click on Layers > Saved map > Select the saved map created above
# Repeat steps for Add Fire layer
# https://maptest.environment.nsw.gov.au/arcgis/rest/services/Elements/MapData_H/MapServer/2


import unittest
import logging
from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
from configuration import PROJECT_ROOT


class TestLinkLibraryLayer(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        self.driver.save_screenshot(PROJECT_ROOT + "/screenshots/test_LinkLibraryLayer.png")

        self.driver.quit()

    def test_LinkLibraryLayer(self):

        logging.info("starting Test Case: Link Library Layer")
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

        # Click on map > Layers > Saved map > Choose the saved map with event: "map_layer_for_appium"
        main_page.open_MAP()
        common_page.alert_popup_allow()
        map_page = LoadClass.load_page("MapPage")
        map_page.setDriver(self.driver)
        map_page.wait_for_map_to_load()
        map_page.click_layers_button()
        map_page.click_saved_maps_button()
        map_page.choose_map_layer_for_appium()
        map_page.check_presents_of_added_layer()
        map_page.click_clear_button()
        map_page.check_absence_of_added_layer()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_MAP()
        map_page.wait_for_map_to_load()
        map_page.click_layers_button()
        map_page.click_saved_maps_button()
        map_page.choose_map_for_mobile()
        map_page.check_presents_of_added_layer()
        map_page.click_clear_button()
        map_page.check_absence_of_added_layer()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_MAP()
        map_page.wait_for_map_to_load()
        map_page.click_layers_button()
        map_page.choose_first_layer_from_the_list()
        map_page.click_done_button()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_MAP()
        map_page.wait_for_map_to_load()
        map_page.click_layers_button()
        map_page.choose_second_layer_from_the_list()
        map_page.click_done_button()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLinkLibraryLayer)
    unittest.TextTestRunner(verbosity=2).run(suite)

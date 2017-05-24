# Test Case - Maps -- OCAMOB-55

# before running this test create:

# - Login to the OCA server > Click on OCA designer > Symbology and Colour Coding > Add more symbology - new point symbol name: "point2"
# - Login to oca server > Click on mapping > Draw geometry > Save map as "FOR MOBILE"


# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present

# From the main menu press Maps.
# Click on Map > Click on Layers > Select a layer = "ARCGIS polygon Layer" --> Layer added to the map on oca mobile
# Click on the map --> OCA mobile Map should show  the user's location by default
# Click on Circle icon on the map --> Map should refresh
# Click on Search Icon on the map > Location Search > Enter the address >
# Go = "Enter the Address as = 580 George street Sydney 2121" -->
# List of suggested address should be displayed . Choose the address > Point is marked on the selected address
# Click on +/- on the map --> Map should Zoom in and out
# Click on map > Point > Select point/Line/Circle/Polygon --> All shapes are plotted on the map

# login to the OCA server > Click on OCA designer > Symbology and Colour Coding > Add more symbology

# Login to oca server > Click on mapping > Draw geometry > Save map as "FOR MOBILE"
# Load Saved maps to the mapping layer
# Login to the app Click on Map > Click on Layers > Saved maps > Select a saved map created above
# Clear saved maps Click on map > Click on layers > Saved maps>select a map > Clear --> Saved map is cleared.

# Support Proxied layer feeds QLD LGA layer has been configured for testing
# Login to App -> Click on mapping -> Click on layer -> Select QLD LGA -> Issue # 40773 for details
# --> Proxied layers are rendered properly on the oca App

from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest
from time import sleep


class TestMaps(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_maps(self):

        logging.info("starting Test Case: Maps")
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

        main_page.open_MAP()
        common_page.alert_popup_allow()
        map_page = LoadClass.load_page("MapPage")
        map_page.setDriver(self.driver)
        map_page.click_layers_button()
        map_page.choose_first_layer_from_the_list()
        map_page.click_done_button()

        map_page.click_locate_button()
        sleep(2)  # wait for localization
        map_page.click_locate_button()
        map_page.click_search_button_on_the_map()
        map_page.type_address_into_search_field("580 George street Sydney 2121")
        common_page.hide_keyboard()
        map_page.click_search_button()
        map_page.click_first_address_on_the_list()
        map_page.click_zoom_in_button()
        map_page.click_zoom_out_button()

        map_page.click_plot_button()
        map_page.click_tool_button()
        map_page.click_point_button()
        map_page.click_default_button()
        map_page.click_in_map_area_1()
        map_page.click_tool_button()
        map_page.click_line_button()
        map_page.click_default_button()
        map_page.click_in_map_area_2()
        map_page.double_click_in_map_area_3()
        map_page.click_tool_button()
        map_page.click_circle_button()
        map_page.click_default_button()
        map_page.click_in_map_area_2()
        map_page.click_tool_button()
        map_page.click_polygon_button()
        map_page.click_default_button()
        map_page.click_in_map_area_1()
        map_page.click_in_map_area_2()
        map_page.double_click_in_map_area_3()
        map_page.save_map()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_MAP()
        map_page.click_plot_button()
        map_page.click_tool_button()
        map_page.click_point_button()
        map_page.click_point_2_button()
        map_page.click_in_map_area_2()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_MAP()
        map_page.click_layers_button()
        map_page.click_saved_maps_button()
        map_page.choose_map_for_mobile()
        map_page.check_presents_of_added_layer()
        map_page.click_clear_button()
        map_page.check_absence_of_added_layer()

        # step nr 10 - adding QLD LGA layer ?


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMaps)
    unittest.TextTestRunner(verbosity=2).run(suite)

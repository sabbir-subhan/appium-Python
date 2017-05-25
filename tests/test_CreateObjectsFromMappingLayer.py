# Test Case - Create objects from Mapping layer -- OCAMOB-53

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
# Maps > Layers > Select layers > Tools > Plot a point, line, circle or polygon > Create > Event > Type > Save
# Maps > Layers > Select layers > Tools > Plot a point, line, circle or polygon > Create > Asset > Type > Save
# Maps > Layers > Select layers > Tools > Plot a point, line, circle or polygon > Create > Report > Type > Save
# Maps > Layers > Select layers > Tools > Plot a point, line, circle or polygon > Create > Task > Type > Save

# Navigate to Events > Check the type of Event created above
# Navigate to Reports > Check the type of Report created above
# Navigate to Assets > Check the type of created above

# View attributes on Map Geometry - Click on Event > Create a new event > Click on Create mapping data >
# Click on Tool > Add Geometry>Save - Edit event > Click on mapping data > Click on Geometry > View attributes

# Click on Map > Click on layers > Click on Saved map > Click on geometry > Click on View attributes

# Click on map > Click on Layers > Click on saved map > Add map > Click on Geometry > Click on View Event

# Click on map > Click on layers > Click on saved map > saved map > Select an asset map > click on view Asset

# Click on map > Click on layers > Click on saved map > saved map > Select an Contact map > click on view Contact

# Click on map > Click on layers > Click on saved map > saved map > Select an Task map > click on view Task

# Duplicate Geometry Click on map >Add geometry>Click on Duplicate>select the type>Click on the geometry again and drag


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest
from time import sleep


class TestCreateObjectsFromMappingLayer(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_create_objects_from_mapping_layer(self):

        logging.info("starting Test Case: Create objects from Mapping layer")
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

        map_page.click_plot_button()
        map_page.click_tool_button()
        map_page.click_point_button()
        map_page.click_default_button()
        map_page.click_in_map_area_1()
        map_page.save_map()
        #event

        main_page.open_MAP()
        map_page.click_layers_button()
        map_page.choose_first_layer_from_the_list()
        map_page.click_done_button()
        map_page.click_plot_button()
        map_page.click_tool_button()
        map_page.click_line_button()
        map_page.click_default_button()
        map_page.click_in_map_area_2()
        map_page.double_click_in_map_area_3()
        #asset

        main_page.open_MAP()
        map_page.click_layers_button()
        map_page.choose_first_layer_from_the_list()
        map_page.click_done_button()
        map_page.click_plot_button()
        map_page.click_tool_button()
        map_page.click_circle_button()
        map_page.click_default_button()
        map_page.click_in_map_area_2()
        #report

        main_page.open_MAP()
        map_page.click_layers_button()
        map_page.choose_first_layer_from_the_list()
        map_page.click_done_button()
        map_page.click_plot_button()
        map_page.click_tool_button()
        map_page.click_polygon_button()
        map_page.click_default_button()
        map_page.click_in_map_area_1()
        map_page.click_in_map_area_2()
        map_page.double_click_in_map_area_3()
        #task


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCreateObjectsFromMappingLayer)
    unittest.TextTestRunner(verbosity=2).run(suite)

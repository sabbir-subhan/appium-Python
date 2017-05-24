"""A class for methods to handle Map Page """

from Modules.BasePage.BasePage import BasePage
import logging
from time import sleep
from selenium.common.exceptions import NoSuchElementException


class MapPage(BasePage):

    def click_plot_button(self):

        self.switch_context_to_webview()

        logging.info("click Plot button")
        plot_button = self.driver.find_element(*self.configuration.Map.PLOT_BUTTON)
        self.assertIsNotNone(plot_button)
        plot_button.click()

        self.switch_context_to_native()

    def click_tool_button(self):

        sleep(2)
        self.switch_context_to_webview()

        logging.info("click tool button")
        tool_button = self.driver.find_element(*self.configuration.Map.TOOL_BUTTON)
        self.assertIsNotNone(tool_button, "Tool button is not present")
        tool_button.click()

        self.switch_context_to_native()

    def click_point_button(self):

        self.switch_context_to_webview()

        logging.info("click point button")
        point_button = self.driver.find_element(*self.configuration.Map.POINT_BUTTON)
        self.assertIsNotNone(point_button, "point button not found")
        point_button.click()

        self.switch_context_to_native()

    def click_line_button(self):

        self.switch_context_to_webview()

        logging.info("click line button")
        line_button = self.driver.find_element(*self.configuration.Map.LINE_BUTTON)
        self.assertIsNotNone(line_button, "line button not found")
        line_button.click()

        self.switch_context_to_native()

    def click_circle_button(self):

        self.switch_context_to_webview()

        logging.info("click circle button")
        circle_button = self.driver.find_element(*self.configuration.Map.CIRCLE_BUTTON)
        self.assertIsNotNone(circle_button, "circle button not found")
        circle_button.click()

        self.switch_context_to_native()

    def click_polygon_button(self):

        self.switch_context_to_webview()

        logging.info("click polygon button")
        polygon_button = self.driver.find_element(*self.configuration.Map.POLYGON_BUTTON)
        self.assertIsNotNone(polygon_button, "polygon button not found")
        polygon_button.click()

        self.switch_context_to_native()

    def click_default_button(self):

        logging.info("click default button")
        default_button = self.driver.find_element(*self.configuration.Map.DEFAULT_BUTTON)
        self.assertIsNotNone(default_button, "default button not found")
        default_button.click()
        sleep(1)

    def click_point_2_button(self):

        self.switch_context_to_webview()

        logging.info('click "point2" button - new symbology added in OCA')
        point_2_button = self.driver.find_element(*self.configuration.Map.POINT_2_BUTTON)
        self.assertIsNotNone(point_2_button, '"point2" button not found')
        point_2_button.click()

        self.switch_context_to_native()

    # def save_map(self):
    #
    #     logging.info("Save map")
    #     save_map_button = self.driver.find_element(*self.configuration.Map.SAVE_MAP_BUTTON)
    #     self.assertIsNotNone(save_map_button, "save map button not found")
    #     save_map_button.click()
    #     sleep(3)

    def save_map(self):

        self.switch_context_to_webview()

        sleep(1)
        logging.info("Save map")
        save_map_button = self.driver.find_element(*self.configuration.Map.SAVE_MAP_BUTTON)
        self.assertIsNotNone(save_map_button, "save map button not found")
        save_map_button.click()
        sleep(4)

        self.switch_context_to_native()

        sleep(1)

    def choose_plot_type_asset(self):

        self.switch_context_to_webview()

        logging.info("choose plot type")
        choose_plot_type = self.driver.find_element(*self.configuration.Map.PLOT_TYPE_ASSET)
        self.assertIsNotNone(choose_plot_type, "plot type not found")
        choose_plot_type.click()

        self.switch_context_to_native()

    def click_layers_button(self):

        self.switch_context_to_webview()

        logging.info("click layers button")
        click_layers_button = self.driver.find_element(*self.configuration.Map.LAYERS)
        self.assertIsNotNone(click_layers_button)
        click_layers_button.click()

        self.switch_context_to_native()

    def choose_first_layer_from_the_list(self):

        self.switch_context_to_webview()

        logging.info("choose first layer from the list")
        choose_first_layer_from_the_list = self.driver.find_element(*self.configuration.Map.FIRST_LAYER_ON_THE_LIST)
        self.assertIsNotNone(choose_first_layer_from_the_list, "first layer not found")
        choose_first_layer_from_the_list.click()

        self.switch_context_to_native()

    def choose_second_layer_from_the_list(self):

        self.switch_context_to_webview()

        logging.info("choose second layer from the list")
        choose_second_layer_from_the_list = self.driver.find_element(*self.configuration.Map.SECOND_LAYER_ON_THE_LIST)
        self.assertIsNotNone(choose_second_layer_from_the_list, "second layer not found")
        choose_second_layer_from_the_list.click()

        self.switch_context_to_native()
        
    def choose_third_layer_from_the_list(self):

        self.switch_context_to_webview()

        logging.info("choose third layer from the list")
        choose_third_layer_from_the_list = self.driver.find_element(*self.configuration.Map.THIRD_LAYER_ON_THE_LIST)
        self.assertIsNotNone(choose_third_layer_from_the_list, "third layer not found")
        choose_third_layer_from_the_list.click()

        self.switch_context_to_native()

    def click_done_button(self):

        self.switch_context_to_webview()

        logging.info("click done button")
        click_done_button = self.driver.find_element(*self.configuration.Map.LAYERS_DONE)
        self.assertIsNotNone(click_done_button, "Done button not found")
        click_done_button.click()

        self.switch_context_to_native()

    def click_saved_maps_button(self):

        self.switch_context_to_webview()

        logging.info("click Saved maps button")
        click_saved_maps_button = self.driver.find_element(*self.configuration.Map.LAYERS_SAVED_MAPS)
        self.assertIsNotNone(click_saved_maps_button, "Saved maps not found")
        click_saved_maps_button.click()

        self.switch_context_to_native()

    def click_locate_button(self):

        self.switch_context_to_webview()

        logging.info("click locate button")
        click_locate_button = self.driver.find_element(*self.configuration.Map.LOCATE_BUTTON)
        self.assertIsNotNone(click_locate_button, "locate button not found")
        click_locate_button.click()

        self.switch_context_to_native()

    def click_search_button_on_the_map(self):

        self.switch_context_to_webview()

        logging.info("click search button on the map")
        click_search_button = self.driver.find_element(*self.configuration.Map.SEARCH_BUTTON_ON_MAP)
        self.assertIsNotNone(click_search_button, "search button on the map not found")
        click_search_button.click()

        self.switch_context_to_native()

    def type_address_into_search_field(self, text):

        logging.info("type_address_into_search_field")
        search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        self.assertIsNotNone(search_field, "search field not found")
        search_field.click()
        search_field.send_keys(text)

    def click_search_button(self):

        self.switch_context_to_webview()

        logging.info("click search button")
        click_search_button = self.driver.find_element(*self.configuration.Map.SEARCH_BUTTON)
        self.assertIsNotNone(click_search_button, "search button not found")
        click_search_button.click()

        self.switch_context_to_native()

    def click_first_address_on_the_list(self):

        self.switch_context_to_webview()

        logging.info("click first address on the list")
        click_first_address_on_the_list = self.driver.find_element(*self.configuration.Map.FIRST_ADDRESS_ON_THE_LIST)
        self.assertIsNotNone(click_first_address_on_the_list, "first address on the list not found")
        click_first_address_on_the_list.click()

        self.switch_context_to_native()

        sleep(4)  # wait for map to load

    def click_zoom_in_button(self):

        self.switch_context_to_webview()

        logging.info("click zoom in button")
        zoom_in_button = self.driver.find_element(*self.configuration.Map.ZOOM_IN_BUTTON)
        self.assertIsNotNone(zoom_in_button, "zoom in button not found")
        zoom_in_button.click()

        self.switch_context_to_native()

        sleep(1)
        
    def click_zoom_out_button(self):

        self.switch_context_to_webview()

        logging.info("click zoom out button")
        zoom_out_button = self.driver.find_element(*self.configuration.Map.ZOOM_OUT_BUTTON)
        self.assertIsNotNone(zoom_out_button, "zoom out button not found")
        zoom_out_button.click()

        self.switch_context_to_native()

        sleep(1)

    def check_presents_of_added_layer(self):

        self.switch_context_to_webview()

        logging.info("check if added layer is present on the map")
        check_presents_of_added_layer = self.driver.find_element(*self.configuration.Map.MAP_ADDED_LAYER)
        self.assertIsNotNone(check_presents_of_added_layer, "added layer not found")

        self.switch_context_to_native()

    def choose_map_for_mobile(self):

        logging.info("choose saved map 'FOR MOBILE' ")
        choose_map_for_mobile = self.driver.find_element(*self.configuration.Map.SAVED_MAP_FOR_MOBILE)
        self.assertIsNotNone(choose_map_for_mobile, "Saved map 'FOR MOBILE' not found")
        choose_map_for_mobile.click()
        sleep(2)

    def check_absence_of_added_layer(self):

        logging.info("check absence of added layer")

        self.switch_context_to_webview()

        try:
            check_absence_of_added_layer = self.driver.find_element(*self.configuration.Map.MAP_ADDED_LAYER)
            if check_absence_of_added_layer.is_displayed():
                self.fail("layer was not cleared correctly")
            else:
                logging.info("added layer is not displayed")
                pass
        except NoSuchElementException:
            logging.info("layer is not visible = OK")
            pass

        self.switch_context_to_native()

    def click_clear_button(self):

        self.switch_context_to_webview()

        logging.info("click Clear button")
        click_clear_button = self.driver.find_element(*self.configuration.Map.CLEAR_BUTTON)
        self.assertIsNotNone(click_clear_button, "Clear button not found")
        click_clear_button.click()

        self.switch_context_to_native()


"""A class for methods to handle Map Page """

from Modules.BasePage.BasePage import BasePage
import logging
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction


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

    def click_point_default_button(self):

        self.switch_context_to_webview()

        logging.info("click Point default button")
        point_default_button = self.driver.find_element(*self.configuration.Map.POINT_DEFAULT_BUTTON)
        self.assertIsNotNone(point_default_button, "Point default button not found")
        point_default_button.click()

        self.switch_context_to_native()

    def click_line_default_button(self):

        self.switch_context_to_webview()

        logging.info("click Line default button")
        line_default_button = self.driver.find_element(*self.configuration.Map.LINE_DEFAULT_BUTTON)
        self.assertIsNotNone(line_default_button, "Line default button not found")
        line_default_button.click()

        self.switch_context_to_native()

    def click_circle_default_button(self):

        self.switch_context_to_webview()

        logging.info("click Circle default button")
        circle_default_button = self.driver.find_element(*self.configuration.Map.CIRCLE_DEFAULT_BUTTON)
        self.assertIsNotNone(circle_default_button, "Circle default button not found")
        circle_default_button.click()

        self.switch_context_to_native()

    def click_polygon_default_button(self):

        self.switch_context_to_webview()

        logging.info("click Polygon default button")
        polygon_default_button = self.driver.find_element(*self.configuration.Map.POLYGON_DEFAULT_BUTTON)
        self.assertIsNotNone(polygon_default_button, "Polygon default button not found")
        polygon_default_button.click()

        self.switch_context_to_native()

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

        sleep(1)

        self.switch_context_to_webview()

        logging.info("Save map")
        save_map_button = self.driver.find_element(*self.configuration.Map.SAVE_MAP_BUTTON)
        self.assertIsNotNone(save_map_button, "save map button not found")
        save_map_button.click()

        self.switch_context_to_native()

        sleep(4)

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

        sleep(4)  # wait for map to load new layer

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
        sleep(1)

    def click_first_address_on_the_list(self):

        sleep(1)
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

    def check_presents_of_added_layer_for_mobile(self):  # it searches for added graphic layer on the map - "FOR MOBILE" is saved map (created in OCA)

        sleep(1)
        self.switch_context_to_webview()

        logging.info("check if added layer is present on the map")
        check_presents_of_added_layer = self.driver.find_element(*self.configuration.Map.MAP_ADDED_LAYER_FOR_MOBILE)  # first element in <g#mapCanvas_graphics_layer
        self.assertIsNotNone(check_presents_of_added_layer, "added layer not found")

        self.switch_context_to_native()

    # def check_presents_of_added_layer(self):  # it searches for added graphic element on the map
    #
    #     sleep(2)
    #     self.switch_context_to_webview()
    #
    #     logging.info("check if added layer is present on the map")
    #     check_presents_of_added_layer = self.driver.find_element(*self.configuration.Map.MAP_ADDED_LAYER)
    #     self.assertIsNotNone(check_presents_of_added_layer, "added layer not found")
    #
    #     self.switch_context_to_native()

    def check_presents_of_added_layer(self):  # it searches for added graphic element on the map

        sleep(2)
        self.switch_context_to_webview()

        logging.info("check if added layer is present on the map")
        sleep(1)
        # try:
        #     check_presents_of_added_layer = self.driver.find_element(*self.configuration.Map.MAP_ADDED_LAYER)
        #     self.assertIsNotNone(check_presents_of_added_layer, "added layer not found")
        # except NoSuchElementException:
        #     whole_g_element = self.driver.find_element(*self.configuration.Map.MAP_ADDED_LAYER_SECOND_ELEMENT)
        #     self.assertIsNotNone(whole_g_element, "whole graphic element not found")
        try:
            added_layer = self.driver.find_element(*self.configuration.Map.MAP_ADDED_LAYER_SECOND_ELEMENT)  # actually it is first element because first-child is empty <g> tag
            if added_layer.is_displayed():
                self.assertIsNotNone(added_layer, "added layer not found")
            else:
                pass
        except NoSuchElementException:
            logging.warning("added layer not found - check if, for example contact with address, is present")

        self.switch_context_to_native()

    def click_on_added_layer(self):  # it searches for added graphic layer on the map

        sleep(1)
        self.switch_context_to_webview()

        logging.info("click on added layer")

        try:
            el = self.driver.find_element(*self.configuration.Map.MAP_ADDED_LAYER_SECOND_ELEMENT)
            el.click()
        except:
            logging.warning("added layer not found - there is too many elements on map, Appium can't tap on single element because they are overlapping")

        # click_on_added_layer = self.driver.find_elements(*self.configuration.Map.MAP_ADDED_LAYER)
        # self.assertIsNotNone(click_on_added_layer[0], "added layer not found")
        # sleep(1)
        # click_on_added_layer[0].click()

        self.switch_context_to_native()
        sleep(1)

    # def click_on_added_geometry_assets_and_tasks(self):
    #
    #     logging.info("click on added geometry")
    #     sleep(1)
    #
    #     self.switch_context_to_webview()
    #
    #     el = self.driver.find_element(*self.configuration.Map.ALL_ASSETS_AND_TASKS_GEOMETRY)
    #     el.click()

        # try:
        #     print("1")
        #     el = self.driver.find_elements(*self.configuration.Map.MAP_ADDED_GEOMETRY_ALL)
        #     el[0].click()
        #     # el = self.driver.find_element(*self.configuration.Map.MAP_ADDED_LAYER_SECOND_ELEMENT)
        # except NoSuchElementException:
        #     print("2")
        #     el = self.driver.find_element(*self.configuration.Map.MAP_ADDED_LAYER)  # last child
        # sleep(1)
        # el.click()

        # try:
        #     el1 = self.driver.find_element(*self.configuration.Map.MAP_ADDED_LAYER_SECOND_ELEMENT)
        #     el1.click()
        # except NoSuchElementException:
        #     logging.info("search for another element")
        #     el2 = self.driver.find_element(*self.configuration.Map.ALL_ASSETS_AND_TASKS_GEOMETRY)
        #     el2.click()

        # self.switch_context_to_native()

    # def click_on_added_geometry_events_and_contacts(self):
    #
    #     logging.info("click on added geometry")
    #     sleep(1)
    #
    #     self.switch_context_to_webview()
    #
    #     el = self.driver.find_element(*self.configuration.Map.ALL_EVENTS_AND_CONTACTS_GEOMETRY)
    #     el.click()

        # try:
        #     el = self.driver.find_element(*self.configuration.Map.ALL_ASSETS_AND_TASKS_GEOMETRY)
        # except NoSuchElementException:
        #     el = self.driver.find_element(*self.configuration.Map.ALL_EVENTS_AND_CONTACTS_GEOMETRY)
        # el.click()

        # action = TouchAction(self.driver)
        # action.tap(element=el).perform()  # method not yet implemented

        # try:
        #     el1 = self.driver.find_element(*self.configuration.Map.ALL_ASSETS_AND_TASKS_GEOMETRY)
        #     el2 = self.driver.find_element(*self.configuration.Map.ALL_EVENTS_AND_CONTACTS_GEOMETRY)
        #     el3 = self.driver.find_element(*self.configuration.Map.MAP_ADDED_GEOMETRY_ALL)
        #     el4 = self.driver.find_element(*self.configuration.Map.WHOLE_MAP)
        #     if el1.is_displayed():
        #         el1.click()
        #         print("1")
        #     elif el2.is_displayed():
        #         el2.click()
        #         print("2")
        #     elif el3.is_displayed():
        #         el3.click()
        #         print("3")
        #     elif el4.is_displayed():
        #         el4.click()
        #         print("4")
        #     else:
        #         print("elements not found")
        # except NoSuchElementException:
        #     print("elements not found")

        # self.switch_context_to_native()

    # def click_on_added_geometry(self):
    #
    #     logging.info("click on added geometry")
    #     sleep(1)
    #
    #     self.switch_context_to_webview()
    #
    #     try:
    #         el = self.driver.find_element(*self.configuration.Map.ALL_ASSETS_AND_TASKS_GEOMETRY)
    #     except NoSuchElementException:
    #         el = self.driver.find_element(*self.configuration.Map.ALL_EVENTS_AND_CONTACTS_GEOMETRY)
    #     el.click()
    #
    #     self.switch_context_to_native()

    def choose_map_all_tasks(self):

        logging.info("choose saved map 'All tasks' ")
        choose_map_all_tasks = self.driver.find_element(*self.configuration.Map.SAVED_MAP_ALL_TASKS)
        self.assertIsNotNone(choose_map_all_tasks, "Saved map 'All tasks' not found")
        choose_map_all_tasks.click()
        sleep(2)

    def choose_map_all_contacts(self):

        logging.info("choose saved map 'All contacts' ")
        choose_map_all_contacts = self.driver.find_element(*self.configuration.Map.SAVED_MAP_ALL_CONTACTS)
        self.assertIsNotNone(choose_map_all_contacts, "Saved map 'All contacts' not found")
        choose_map_all_contacts.click()
        sleep(2)

    def choose_map_all_assets(self):

        logging.info("choose saved map 'All assets' ")
        choose_map_all_assets = self.driver.find_element(*self.configuration.Map.SAVED_MAP_ALL_ASSETS)
        self.assertIsNotNone(choose_map_all_assets, "Saved map 'All assets' not found")
        choose_map_all_assets.click()
        sleep(2)

    def choose_map_all_active_events(self):

        logging.info("choose saved map 'All active events' ")
        choose_map_all_active_events = self.driver.find_element(*self.configuration.Map.SAVED_MAP_ALL_ACTIVE_EVENTS)
        self.assertIsNotNone(choose_map_all_active_events, "Saved map 'All active events' not found")
        choose_map_all_active_events.click()
        sleep(2)

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

    def choose_first_plot_object(self):  # asset

        self.switch_context_to_webview()

        logging.info("choose first plot object")
        choose_first_plot_object = self.driver.find_element(*self.configuration.Map.FIRST_PLOT_OBJECT)
        self.assertIsNotNone(choose_first_plot_object, "first plot object not found")
        choose_first_plot_object.click()

        self.switch_context_to_native()

    def choose_second_plot_object(self):  # event

        self.switch_context_to_webview()

        logging.info("choose second plot object")
        choose_second_plot_object = self.driver.find_element(*self.configuration.Map.SECOND_PLOT_OBJECT)
        self.assertIsNotNone(choose_second_plot_object, "second plot object not found")
        choose_second_plot_object.click()

        self.switch_context_to_native()
        
    def choose_third_plot_object(self):  # report

        self.switch_context_to_webview()

        logging.info("choose third plot object")
        choose_third_plot_object = self.driver.find_element(*self.configuration.Map.THIRD_PLOT_OBJECT)
        self.assertIsNotNone(choose_third_plot_object, "third plot object not found")
        choose_third_plot_object.click()

        self.switch_context_to_native()
        
    def choose_fourth_plot_object(self):  # task

        self.switch_context_to_webview()

        logging.info("choose fourth plot object")
        choose_fourth_plot_object = self.driver.find_element(*self.configuration.Map.FOURTH_PLOT_OBJECT)
        self.assertIsNotNone(choose_fourth_plot_object, "fourth plot object not found")
        choose_fourth_plot_object.click()

        self.switch_context_to_native()

    def click_view_layer_attributes(self):

        self.switch_context_to_webview()

        logging.info("click view layer attributes, for example view asset button")

        try:
            click_view_layer_attributes = self.driver.find_element(*self.configuration.Map.VIEW_ATTRIBUTES_FROM_LAYER)
            self.assertIsNotNone(click_view_layer_attributes, "view layer attributes button not present")
            click_view_layer_attributes.click()
        except NoSuchElementException:
            logging.info("view layer attributes button not present - previous step was skipped")

        self.switch_context_to_native()

    def click_duplicate_button(self):

        self.switch_context_to_webview()

        logging.info("click duplicate button")
        click_duplicate_button = self.driver.find_element(*self.configuration.Map.DUPLICATE_BUTTON)
        self.assertIsNotNone(click_duplicate_button, "Duplicate button not present")
        click_duplicate_button.click()

        self.switch_context_to_native()

    def click_on_duplicated_geometry(self):

        self.switch_context_to_webview()

        logging.info("click on duplicated geometry")
        click_on_duplicated_geometry = self.driver.find_element(*self.configuration.Map.DUPLICATED_GEOMETRY_ON_MAP)
        self.assertIsNotNone(click_on_duplicated_geometry, "Duplicated geometry not present")
        click_on_duplicated_geometry.click()
        sleep(1)

        self.switch_context_to_native()

    def press_and_drag_duplicated_geometry(self):

        logging.info("press and drag duplicated geometry")
        sleep(1)

        self.switch_context_to_webview()

        duplicated_geometry = self.driver.find_element(*self.configuration.Map.DUPLICATED_GEOMETRY_ON_MAP)
        location = duplicated_geometry.location
        print(location)
        x = int(location["x"])
        y = int(location["y"])
        print(x)
        print(y)
        x = x + x * 0.5
        y = y + y * 0.5
        print(x)
        print(y)
        action = TouchAction(self.driver)
        # action.long_press(el=duplicated_geometry, duration=1000).move_to(x=x, y=y).release().perform()
        sleep(1)
        action.press(el=duplicated_geometry).wait(ms=1500).move_to(x=x, y=y).release()
        # action.press(el=duplicated_geometry).move_to(x=x, y=y).release()
        logging.info("wait a second after dragging")

        self.switch_context_to_native()

        sleep(2)



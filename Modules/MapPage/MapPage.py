"""A class for methods to handle Map Page """

from Modules.BasePage.BasePage import BasePage
import logging
from time import sleep


class MapPage(BasePage):

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
        self.assertIsNotNone(choose_first_layer_from_the_list)
        choose_first_layer_from_the_list.click()

        self.switch_context_to_native()

    def click_done_button(self):

        self.switch_context_to_webview()

        logging.info("click done button")
        click_done_button = self.driver.find_element(*self.configuration.Map.LAYERS_DONE)
        self.assertIsNotNone(click_done_button)
        click_done_button.click()

        self.switch_context_to_native()

    def click_plot_button(self):

        self.switch_context_to_webview()

        logging.info("click Plot button")
        plot_button = self.driver.find_element(*self.configuration.Map.PLOT_BUTTON)
        self.assertIsNotNone(plot_button)
        plot_button.click()

        self.switch_context_to_native()

    def click_tool_button(self):

        self.switch_context_to_webview()

        sleep(1)
        logging.info("click tool button")
        tool_button = self.driver.find_element(*self.configuration.Map.TOOL_BUTTON)
        self.assertIsNotNone(tool_button, "Tool button is not present")
        tool_button.click()

        self.switch_context_to_native()

    def click_point_button(self):

        logging.info("click point button")
        point_button = self.driver.find_element(*self.configuration.Map.POINT_BUTTON)
        self.assertIsNotNone(point_button, "point button not found")
        point_button.click()

    def click_line_button(self):

        logging.info("click line button")
        line_button = self.driver.find_element(*self.configuration.Map.LINE_BUTTON)
        self.assertIsNotNone(line_button, "line button not found")
        line_button.click()

    def click_circle_button(self):

        logging.info("click circle button")
        circle_button = self.driver.find_element(*self.configuration.Map.CIRCLE_BUTTON)
        self.assertIsNotNone(circle_button, "circle button not found")
        circle_button.click()

    def click_polygon_button(self):

        logging.info("click polygon button")
        polygon_button = self.driver.find_element(*self.configuration.Map.POLYGON_BUTTON)
        self.assertIsNotNone(polygon_button, "polygon button not found")
        polygon_button.click()

    def click_default_button(self):

        logging.info("click default button")
        default_button = self.driver.find_element(*self.configuration.Map.DEFAULT_BUTTON)
        self.assertIsNotNone(default_button, "default button not found")
        default_button.click()
        sleep(1)

    # def save_map(self):
    #
    #     logging.info("Save map")
    #     save_map_button = self.driver.find_element(*self.configuration.Map.SAVE_MAP_BUTTON)
    #     self.assertIsNotNone(save_map_button, "save map button not found")
    #     save_map_button.click()
    #     sleep(3)

    def save_map(self):

        self.switch_context_to_webview()

        logging.info("Save map")
        save_map_button = self.driver.find_element(*self.configuration.Map.SAVE_MAP_BUTTON)
        self.assertIsNotNone(save_map_button, "save map button not found")
        save_map_button.click()
        sleep(3)

        self.switch_context_to_native()

    def choose_plot_type_asset(self):

        self.switch_context_to_webview()

        logging.info("choose plot type")
        choose_plot_type = self.driver.find_element(*self.configuration.Map.PLOT_TYPE_ASSET)
        self.assertIsNotNone(choose_plot_type, "plot type not found")
        choose_plot_type.click()

        self.switch_context_to_native()





""" Methods for Android on Reports Page """

from Modules.ReportsPage.ReportsPage import ReportsPage
import logging
from time import sleep
from Modules.load_class import LoadClass
from selenium.common.exceptions import *
from configuration import platform
from appium.webdriver.common.touch_action import TouchAction


class Android(ReportsPage):

    def check_restored_field_1(self):

        logging.info("assert restored field 1")

        self.switch_context_to_webview()

        field_to_restore_1_header = self.driver.find_element(
            *self.configuration.EventEditScreen.FIELD_TO_RESTORE_1_HEADER)
        self.assertIsNotNone(field_to_restore_1_header)

        self.switch_context_to_native()

        sleep(2)
        try:
            field_to_restore_1_value = self.driver.find_element(
                *self.configuration.EventEditScreen.FIELD_TO_RESTORE_1_VALUE)
        except NoSuchElementException:
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.scroll_down_one_view()
            field_to_restore_1_value = self.driver.find_element(
                *self.configuration.EventEditScreen.FIELD_TO_RESTORE_1_VALUE)
        self.assertIsNotNone(field_to_restore_1_value, "field to restore 1 value not found")

    def check_restored_field_2(self):

        logging.info("assert restored field 2")

        self.switch_context_to_webview()

        field_to_restore_2_header = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_2_HEADER)
        self.assertIsNotNone(field_to_restore_2_header)

        self.switch_context_to_native()

        sleep(1)
        try:
            field_to_restore_2_value = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_2_VALUE)
        except NoSuchElementException:
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.scroll_down_one_view()
            field_to_restore_2_value = self.driver.find_element(
                *self.configuration.EventEditScreen.FIELD_TO_RESTORE_2_VALUE)
        self.assertIsNotNone(field_to_restore_2_value, "field to restore 2 value not found")

    def check_restored_field_3(self):

        logging.info("assert restored field 3")

        self.switch_context_to_webview()

        field_to_restore_3_header = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_3_HEADER)
        self.assertIsNotNone(field_to_restore_3_header)

        self.switch_context_to_native()

        sleep(1)
        try:
            field_to_restore_3_value = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_3_VALUE)
        except NoSuchElementException:
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.scroll_down_one_view()
            field_to_restore_3_value = self.driver.find_element(
                *self.configuration.EventEditScreen.FIELD_TO_RESTORE_3_VALUE)
        self.assertIsNotNone(field_to_restore_3_value, "field to restore 3 value not found")

    def scroll_down_to_assets_chooser_field(self):

        logging.info("scroll down to assets chooser field")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()
        common_page.scroll_down_one_view()

    def choose_lodging_agency(self):

        logging.info("choose Lodging Agency")
        lodging_agency = self.driver.find_element(*self.configuration.ReportsScreen.LODGING_AGENCY)
        self.assertIsNotNone(lodging_agency, "Lodging Agency inside picker was not found")
        lodging_agency.click()
        sleep(1)

    def scroll_down_to_publish_button(self):

        logging.info("scroll down to Publish button")
        window_size = self.driver.get_window_size()  # this returns dictionary
        start_x = window_size["width"]*0.25
        # end_x = window_size["width"]*0.75
        start_y = window_size["height"]*0.20
        end_y = window_size["height"]*0.80
        logging.info("scrolling down to Publish button")
        sleep(1)
        scrolls = 10
        while scrolls > 0:
            self.driver.swipe(start_x, end_y, start_x, start_y, 3000)  # each swipe is scrolling one screen
            scrolls = scrolls - 1
        sleep(2)

    def scroll_down_to_on_load_field(self):

        logging.info("scroll down to on load field")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

    def scroll_down_to_option_list(self):

        logging.info("scroll down to option list")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

    def scroll_down_media_release_field(self):

        logging.info("scroll down to media release field")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_half_view()

        # if "emulator" and "5" in platform:
        #     common_page.scroll_down_one_small_view()
        # else:
        #     common_page.scroll_down_one_view()

    def type_text_into_media_release_field(self):

        sleep(1)
        media_release_field = self.driver.find_element(*self.configuration.ReportsScreen.MEDIA_RELEASE_FIELD)
        media_release_field.click()
        sleep(1)
        logging.info("sending keys")
        self.driver.press_keycode(48)  # send letter 'T'
        self.driver.press_keycode(33)  # send letter 'E'
        self.driver.press_keycode(52)  # send letter 'X'
        self.driver.press_keycode(48)  # send letter 'T'

    def click_publish_new_report(self):

        self.switch_context_to_webview()

        try:
            logging.info("click Publish button")
            publish_button = self.driver.find_element(*self.configuration.ReportsScreen.PUBLISH_NEW_REPORT)
            self.assertIsNotNone(publish_button, "Publish button was not found")
            publish_button.click()
        except NoSuchElementException:
            ReportsPage.click_publish_edited_report(self)
        try:  # in some cases after tapping Publish button page jumps to the top
            title = self.driver.find_element(*self.configuration.ReportsScreen.TITLE)
            if title.is_displayed():
                try:
                    self.switch_context_to_native()
                    Android.scroll_down_to_publish_button(self)
                    self.switch_context_to_webview()
                    publish_button = self.driver.find_element(*self.configuration.ReportsScreen.PUBLISH_NEW_REPORT)
                    publish_button.click()
                except WebDriverException:
                    pass
            else:
                pass
        except NoSuchElementException:
            pass

        self.switch_context_to_native()

    def click_assets_chooser_field(self):

        self.switch_context_to_webview()

        logging.info("click assets chooser field")
        if "emulator" and "5" in platform:
            assets_chooser_field = self.driver.find_element(*self.configuration.ReportsScreen.ASSETS_CHOOSER_FIELD)
            self.assertIsNotNone(assets_chooser_field, "assets chooser field not found")
            assets_chooser_field.click()
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            self.switch_context_to_native()
            common_page.scroll_down_one_view()  # some problem on Android 5.1 emulator after clicking to chooser field
            self.switch_context_to_webview()
            assets_chooser_field.click()
        else:
            assets_chooser_field = self.driver.find_element(*self.configuration.ReportsScreen.ASSETS_CHOOSER_FIELD)
            self.assertIsNotNone(assets_chooser_field, "assets chooser field not found")
            assets_chooser_field.click()
        sleep(1)

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

    def create_mapping_data(self):

        self.switch_context_to_webview()

        logging.info("click create mapping data")

        if "emulator" and "5" in platform:
            create_mapping_data = self.driver.find_element(*self.configuration.ReportsScreen.CREATE_MAPPING_DATA)
            self.assertIsNotNone(create_mapping_data, "create mapping data button not found")
            create_mapping_data.click()
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            self.switch_context_to_native()
            common_page.scroll_down_one_view()  # some problem on Android 5.1 emulator after clicking to chooser field
            self.switch_context_to_webview()
            create_mapping_data.click()
        else:
            create_mapping_data = self.driver.find_element(*self.configuration.ReportsScreen.CREATE_MAPPING_DATA)
            self.assertIsNotNone(create_mapping_data, "create mapping data button not found")
            create_mapping_data.click()

        self.switch_context_to_native()
        sleep(2)

    # def click_assets_chooser_field(self):
    #
    #     sleep(1)
    #     logging.info("click assets chooser field")
    #     self.switch_context_to_webview()
    #
    #     assets_chooser_field = self.driver.find_element(*self.configuration.ReportsScreen.ASSETS_CHOOSER_FIELD)
    #     self.assertIsNotNone(assets_chooser_field, "assets chooser field not found")
    #     if "emulator" in platform:
    #         location = assets_chooser_field.location
    #         x = location["x"]
    #         y = location["y"]
    #         x = int(x)
    #         y = int(y)
    #
    #         self.switch_context_to_native()
    #
    #         action = TouchAction(self.driver)
    #         action.tap(element=None, x=x, y=y, count=1).perform()
    #     else:
    #         self.switch_context_to_webview()
    #
    #         assets_chooser_field.click()
    #     sleep(1)
    #
    #     self.switch_context_to_native()
    #
    #     common_page = LoadClass.load_page('CommonPage')
    #     common_page.setDriver(self.driver)
    #     common_page.wait_for_app_loading()


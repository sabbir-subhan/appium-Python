"""A class for methods to handle Common Page """

from Modules.BasePage.BasePage import BasePage
import logging
from time import sleep
import os
from Modules.load_class import LoadClass
from configuration import PROJECT_ROOT
from selenium.common.exceptions import NoSuchElementException
from configuration import platform


class CommonPage(BasePage):

    def back_arrow(self):

        self.switch_context_to_webview()

        logging.info("click back arrow")

        back_arrow = self.driver.find_element(*self.configuration.TopBar.BACK_ARROW)
        self.assertIsNotNone(back_arrow, "back arrow not found")
        back_arrow.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

    def back_arrow_for_emulators(self):

        self.switch_context_to_webview()

        logging.info("click back arrow if running on emulator")

        logging.info("Appium is running on: " + str(platform))
        if "emulator" in str(platform):
            logging.info("Appium is running on emulator")
            back_arrow = self.driver.find_element(*self.configuration.TopBar.BACK_ARROW)
            self.assertIsNotNone(back_arrow, "back arrow not found")
            back_arrow.click()

            self.switch_context_to_native()

            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.wait_for_app_loading()
        else:
            pass

    def hamburger_button(self):

        self.switch_context_to_webview()

        sleep(0.5)
        logging.info("click hamburger button to go back to main menu")

        hamburger_button = self.driver.find_element(*self.configuration.TopBar.HAMBURGER_FOR_MAIN_MENU)
        self.assertIsNotNone(hamburger_button, "hamburger menu button, not found")
        hamburger_button.click()
        # sleep(1)

        self.switch_context_to_native()

        sleep(1)
        # sleep(4)

    def click_device_cancel_button(self):

        logging.info("Click 'Cancel' button")
        cancel_button = self.driver.find_element(*self.configuration.Android.ANDROID_CANCEL_BUTTON)
        self.assertIsNotNone(cancel_button, "Cancel button was not found")
        cancel_button.click()

    def take_screenshot(self, file_name):  # pass file name to this method, without extension

        logging.info("taking screenshot")
        sleep(1)
        path = PROJECT_ROOT + "/screenshots"
        os.chdir(path)
        self.driver.save_screenshot(file_name + ".png")
        sleep(1)
        os.chdir("..")
        sleep(2)

    def reset(self):
        """This method will reset driver - so for example app will be force to logout"""

        logging.info("reset")
        self.driver.reset()

    def click_ok_button(self):

        logging.info("click on 'Ok' button")
        ok_button = self.driver.find_element(*self.configuration.CommonScreen.OK_BUTTON)
        self.assertIsNotNone(ok_button, "Ok button not found")
        ok_button.click()
        sleep(1)

    # def wait_for_app_loading(self):
    #
    #     # logging.info("wait for app loading")
    #     sleep(1)
    #     platform_for_test = str(platform)
    #     if "emulator" in platform_for_test:
    #         sleep(5)
    #     else:
    #         pass
    #     WebDriverWait(self.driver, 25).until(
    #         expected_conditions.invisibility_of_element_located(self.configuration.CommonScreen.LOADING),
    #         "app is still loading - check internet connection")

    def wait_for_app_loading(self):

        sleep(1)

        self.switch_context_to_webview()

        timeout = 600

        try:
            loading_animation = self.driver.find_element(*self.configuration.CommonScreen.LOADING)
            while loading_animation.is_displayed() and timeout > 0:
                logging.info("wait for app loading")
                sleep(2)
                timeout = timeout - 1
                if self.assertIsNot(loading_animation, "end waiting"):
                    break
        except NoSuchElementException:
            logging.info("loading animation not found")
            pass

        self.switch_context_to_native()

    # def wait_for_app_loading(self):
    #
    #     sleep(1)
    #
    #     self.switch_context_to_webview()
    #
    #     try:
    #         loading_animation = self.driver.find_element(*self.configuration.CommonScreen.LOADING)
    #         while loading_animation.is_displayed():
    #             logging.info("wait for app loading")
    #             sleep(2)
    #             if self.assertIsNot(loading_animation, "end waiting"):
    #                 break
    #     except NoSuchElementException:
    #         logging.info("loading animation not found")
    #         pass
    #
    #     self.switch_context_to_native()

    # def wait_for_app_loading(self):
    #
    #     sleep(1)
    #
    #     self.switch_context_to_webview()
    #
    #     try:
    #         loading_animation = self.driver.find_element(*self.configuration.CommonScreen.LOADING)
    #         while loading_animation.is_displayed():
    #             logging.info("wait for app loading")
    #             sleep(2)
    #     except NoSuchElementException:
    #         logging.info("loading animation not found")
    #         pass
    #
    #     self.switch_context_to_native()

    # def additional_wait_for_emulators_in_airplane_mode(self):  # android emulator in airplane mode need a long time to load offline object lists
    #
    #     platform_for_test = str(platform)
    #     if "emulator" in platform_for_test:
    #         logging.info("wait for app loading")
    #
    #         # while expected_conditions.visibility_of_element_located(self.configuration.CommonScreen.LOADING):  # not working
    #         #     logging.info("inside while")
    #         #     try:
    #         #         logging.info("inside try")
    #         #         self.driver.find_element(*self.configuration.CommonScreen.LOADING)
    #         #     except NoSuchElementException:
    #         #         break
    #         #     sleep(2)
    #         #     logging.info("after sleep")
    #         #     if expected_conditions.invisibility_of_element_located(self.configuration.CommonScreen.LOADING):  # looks like this condition is not working properly
    #         #         break
    #         #     else:
    #         #         logging.info("waiting")
    #         #         continue
    #         # logging.info("after while loop")
    #
    #         self.switch_context_to_webview()
    #
    #         try:
    #             loading_animation = self.driver.find_element(*self.configuration.CommonScreen.LOADING)
    #             while loading_animation.is_displayed():
    #                 logging.info("waiting")
    #                 sleep(2)
    #         except NoSuchElementException:
    #             logging.info("loading animation not found")
    #             pass
    #
    #         self.switch_context_to_native()
    #         sleep(1)

    def check_popup_about_unfilled_fields(self):

        logging.info("check Validation error popup about unfilled fields")
        self.switch_context_to_native()
        try:
            check_popup_about_unfilled_fields = self.driver.find_element(*self.configuration.CommonScreen.POPUP_UNFILLED_FIELDS)
            if check_popup_about_unfilled_fields.is_displayed():
                self.fail("Validation error popup is displayed - mandatory fields were not filled")
            else:
                pass
        except NoSuchElementException:
            pass

    def scroll_up_to_name_field(self):

        assets_page = LoadClass.load_page('AssetsPage')
        assets_page.setDriver(self.driver)
        assets_page.scroll_up_to_name_field()

    def scroll_down_to_second_set_of_fields(self):

        assets_page = LoadClass.load_page('AssetsPage')
        assets_page.setDriver(self.driver)
        assets_page.scroll_down_to_second_set_of_fields()

    def scroll_down_to_add_media_button(self):

        assets_page = LoadClass.load_page('AssetsPage')
        assets_page.setDriver(self.driver)
        assets_page.scroll_down_to_add_media_button()

    def click_search_field_in_native_view_to_display_keyboard(self):

        logging.info("click search field in native view to display keyboard")

        search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        self.assertIsNotNone(search_field, "Search field not found")
        search_field.click()

    def offline_retry_button(self):

        self.switch_context_to_webview()
        try:
            offline_retry_button = self.driver.find_element(*self.configuration.OfflinePage.RETRY_BUTTON)
            self.assertIsNotNone(offline_retry_button, "Retry button, not found")
            logging.info("clicking Retry button")
            offline_retry_button.click()
        except NoSuchElementException:
            pass
        self.switch_context_to_webview()

    def check_presence_of_string_in_page_source(self, string):

        self.switch_context_to_webview()

        # logging.warning(self.driver.page_source)
        assert string in self.driver.page_source

        self.switch_context_to_native()

    def get_page_source(self):

        self.switch_context_to_webview()

        file = open('page_source.txt', 'w')
        page_source = self.driver.page_source
        file.write(page_source)
        file.close()

        self.switch_context_to_native()

    def rotate_to_landscape_view(self):

        logging.info("Rotate screen to landscape view")
        self.driver.orientation = 'landscape'

    def rotate_to_portrait_view(self):

        logging.info("Rotate screen to portrait view")
        self.driver.orientation = 'portrait'





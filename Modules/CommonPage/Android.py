""" Methods to handle Android specific actions """

import logging
from time import sleep
from Modules.CommonPage.CommonPage import CommonPage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from Modules.load_class import LoadClass
from Conf.desired_capabilities import DesiredCapabilities
import base64
from configuration import PROJECT_ROOT, platform
import os
import subprocess
from selenium.common.exceptions import NoSuchElementException
from distutils.version import LooseVersion


class Android(CommonPage):

    def push_sample_image_file(self):  # push sample photo file for executing TCs on emulators
        # - works only for rooted android devices and emulators

        # if "emulator" in platform:
        #     logging.info("push image file to the emulator")
        #
        #     image_file_to_send = os.path.join(PROJECT_ROOT, "sample_image.jpg")
        #     path_on_device1 = "/storage/self/primary/DCIM/sample_image.jpg"
        #     with open(file=image_file_to_send, mode='rb') as file2:
        #         encoded_file2 = base64.b64encode(file2.read())
        #     decoded_file2 = encoded_file2.decode()
        #     self.driver.push_file(path_on_device1, decoded_file2)
        #     sleep(1)
        #     # path for some emulators
        #     path_on_device2 = "/storage/sdcard/DCIM/sample_image.jpg"
        #     with open(file=image_file_to_send, mode='rb') as file2:
        #         encoded_file2 = base64.b64encode(file2.read())
        #     decoded_file2 = encoded_file2.decode()
        #     self.driver.push_file(path_on_device2, decoded_file2)
        #     sleep(1)
        #
        #     desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        #     device_name = desired_capabilities.get('deviceName')
        #     # print(device_name)
        #     subprocess.call(["adb", "-s", device_name, "shell", "am", "broadcast", "-a",
        #                      "android.intent.action.MEDIA_MOUNTED", "-d", "file:////sdcard"])
        #     sleep(1)
        # else:
        #     pass

        logging.info("push image file")

        image_file_to_send = os.path.join(PROJECT_ROOT, "sample_image.jpg")
        path_on_device1 = "/storage/self/primary/DCIM/sample_image.jpg"
        with open(file=image_file_to_send, mode='rb') as file2:
            encoded_file2 = base64.b64encode(file2.read())
        decoded_file2 = encoded_file2.decode()
        self.driver.push_file(path_on_device1, decoded_file2)
        sleep(1)

        # path for some emulators
        path_on_device2 = "/storage/sdcard/DCIM/sample_image.jpg"
        with open(file=image_file_to_send, mode='rb') as file2:
            encoded_file2 = base64.b64encode(file2.read())
        decoded_file2 = encoded_file2.decode()
        self.driver.push_file(path_on_device2, decoded_file2)
        sleep(1)

        # path for some Androids, like Android 5.1.1
        path_on_device3 = "/sdcard/DCIM/sample_image.jpg"
        with open(file=image_file_to_send, mode='rb') as file1:
            encoded_file1 = base64.standard_b64encode(file1.read())  # open binary file in read mode
        decoded_file1 = encoded_file1.decode()
        self.driver.push_file(path_on_device3, decoded_file1)
        sleep(1)

        desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        device_name = desired_capabilities.get('deviceName')

        # for emulators (no real device udid)
        logging.warning("try multiple adb broadcast commands to refresh android gallery")
        subprocess.call(["adb", "-s", device_name, "shell", "am", "broadcast", "-a",
                        "android.intent.action.MEDIA_MOUNTED", "-d", "file:////sdcard"])  # works on emulators, on rd throws: "device not found" because for rd -s should point to udid

        device_udid = desired_capabilities.get('udid')  # throws permission denial on not rooted device = Android 7
        logging.warning("try multiple adb broadcast commands to refresh android gallery")
        try:
            subprocess.call(["adb", "-s", device_udid, "shell", "am", "broadcast", "-a",
                             "android.intent.action.MEDIA_MOUNTED", "-d", "file:////sdcard"])
        except:
            pass

        device_udid = desired_capabilities.get('udid')
        logging.warning("try multiple adb broadcast commands to refresh android gallery")
        try:
            subprocess.call(["adb", "-s", device_udid, "shell", "am", "broadcast", "-a",
                             "android.intent.action.MEDIA_MOUNTED", "-d", "file:////storage"])
        except:
            pass

        sleep(10)  # wait for android gallery to refresh

    def push_sample_video_file(self):  # push sample video file for executing TCs on emulators
        # - works only for rooted android devices and emulators

        # if "emulator" in platform:
        #     logging.info("push video file to the emulator")
        #
        #     video_file_to_send = os.path.join(PROJECT_ROOT, "sample_video.mp4")
        #     path_on_device1 = "/storage/self/primary/DCIM/sample_video.mp4"  # works for example for emulator Android 6
        #     with open(file=video_file_to_send, mode='rb') as file1:
        #         encoded_file1 = base64.standard_b64encode(file1.read())  # open binary file in read mode
        #     decoded_file1 = encoded_file1.decode()
        #     self.driver.push_file(path_on_device1, decoded_file1)
        #     sleep(1)
        #     # path for some emulators
        #     path_on_device2 = "/storage/sdcard/DCIM/sample_video.mp4"
        #     # path_on_device2 = "/storage/sdcard/DCIM/Camera/sample_video.mp4"
        #     with open(file=video_file_to_send, mode='rb') as file1:
        #         encoded_file1 = base64.standard_b64encode(file1.read())  # open binary file in read mode
        #     decoded_file1 = encoded_file1.decode()
        #     self.driver.push_file(path_on_device2, decoded_file1)
        #     sleep(1)
        #
        #     desired_capabilities = DesiredCapabilities.get_desired_capabilities()  # create local object
        #     device_name = desired_capabilities.get('deviceName')
        #     # print(device_name)
        #     subprocess.call(["adb", "-s", device_name, "shell", "am", "broadcast", "-a",
        #                      "android.intent.action.MEDIA_MOUNTED", "-d", "file:////sdcard"])
        #     sleep(1)
        # else:
        #     pass

        logging.info("push video file")

        video_file_to_send = os.path.join(PROJECT_ROOT, "sample_video.mp4")

        # path_on_device1 = "/storage/self/primary/DCIM/sample_video.mp4"  # works for example for emulator Android 6
        # path_on_device2 = "/storage/sdcard/DCIM/sample_video.mp4"  # path for some emulators
        # path_on_device3 = "/sdcard/DCIM/sample_video.mp4"  # path for some Androids, like Android 5.1.1
        # if os.path.exists(path_on_device1):
        #     with open(file=video_file_to_send, mode='rb') as file1:
        #         encoded_file1 = base64.standard_b64encode(file1.read())  # open binary file in read mode
        #     decoded_file1 = encoded_file1.decode()
        #     self.driver.push_file(path_on_device1, decoded_file1)
        #     sleep(1)
        # elif os.path.exists(path_on_device2):
        #     with open(file=video_file_to_send, mode='rb') as file1:
        #         encoded_file1 = base64.standard_b64encode(file1.read())  # open binary file in read mode
        #     decoded_file1 = encoded_file1.decode()
        #     self.driver.push_file(path_on_device2, decoded_file1)
        #     sleep(1)
        # elif os.path.exists(path_on_device3):
        #     path_on_device3 = "/sdcard/DCIM/sample_video.mp4"
        #     with open(file=video_file_to_send, mode='rb') as file1:
        #         encoded_file1 = base64.standard_b64encode(file1.read())  # open binary file in read mode
        #     decoded_file1 = encoded_file1.decode()
        #     self.driver.push_file(path_on_device3, decoded_file1)
        #     sleep(1)
        # else:
        #     print("none of paths is valid")

        path_on_device1 = "/storage/self/primary/DCIM/sample_video.mp4"  # works for example for emulator Android 6
        with open(file=video_file_to_send, mode='rb') as file1:
            encoded_file1 = base64.standard_b64encode(file1.read())  # open binary file in read mode
        decoded_file1 = encoded_file1.decode()
        self.driver.push_file(path_on_device1, decoded_file1)
        sleep(1)

        path_on_device2 = "/storage/sdcard/DCIM/sample_video.mp4"  # path for some emulators
        with open(file=video_file_to_send, mode='rb') as file1:
            encoded_file1 = base64.standard_b64encode(file1.read())  # open binary file in read mode
        decoded_file1 = encoded_file1.decode()
        self.driver.push_file(path_on_device2, decoded_file1)
        sleep(1)

        # path for some Androids, like Android 5.1.1
        path_on_device3 = "/sdcard/DCIM/sample_video.mp4"
        with open(file=video_file_to_send, mode='rb') as file1:
            encoded_file1 = base64.standard_b64encode(file1.read())  # open binary file in read mode
        decoded_file1 = encoded_file1.decode()
        self.driver.push_file(path_on_device3, decoded_file1)
        sleep(1)

        desired_capabilities = DesiredCapabilities.get_desired_capabilities()  # create local object
        device_name = desired_capabilities.get('deviceName')
        # print(device_name)

        logging.warning("try multiple adb broadcast commands to refresh android gallery")
        # for emulators (no real device udid)
        subprocess.call(["adb", "-s", device_name, "shell", "am", "broadcast", "-a",
                         "android.intent.action.MEDIA_MOUNTED", "-d", "file:////sdcard"])

        device_udid = desired_capabilities.get('udid')
        logging.warning("try multiple adb broadcast commands to refresh android gallery")
        try:
            subprocess.call(["adb", "-s", device_udid, "shell", "am", "broadcast", "-a",
                             "android.intent.action.MEDIA_MOUNTED", "-d", "file:////sdcard"])
        except:
            pass

        device_udid = desired_capabilities.get('udid')
        logging.warning("try multiple adb broadcast commands to refresh android gallery")
        try:
            subprocess.call(["adb", "-s", device_udid, "shell", "am", "broadcast", "-a",
                             "android.intent.action.MEDIA_MOUNTED", "-d", "file:////storage"])
        except:
            pass

        sleep(10)  # wait for android gallery to refresh

    @staticmethod
    def swipe_up_to_show_control_center():

        pass
        # logging.warning("Appium is running on Android device - there is no control center to show")

    @staticmethod
    def swipe_down_to_hide_control_center():

        pass
        # logging.warning("Appium is running on Android device - there is no control center to hide")

    def swipe_down_to_show_notifications(self):  # this will bring android notifications

        logging.info("swipe down to show notifications")
        window_size = self.driver.get_window_size()  # this returns dictionary
        height_center = window_size["height"] * 0.5
        width_center = window_size["width"] * 0.5
        self.driver.swipe(start_x=width_center, start_y=1, end_x=width_center, end_y=height_center, duration=800)
        sleep(2)

    def swipe_up_to_hide_notifications(self):

        logging.info("swipe up to hide notifications")
        window_size = self.driver.get_window_size()  # this returns dictionary
        start_x = window_size["width"] * 0.5
        start_y = window_size["height"] - 1
        self.driver.swipe(start_x=start_x, start_y=start_y, end_x=start_x, end_y=10, duration=1000)
        sleep(1)

    # def switch_airplane_mode(self):  # method only for iOS
    #
    #     pass

    def switch_wifi(self):

        logging.info("switch wi-fi on/off")
        try:
            switch_wifi = self.driver.find_element(*self.configuration.Android.SWITCH_WIFI_ANDROID_7)
        except NoSuchElementException:
            switch_wifi = self.driver.find_element(*self.configuration.Android.SWITCH_WIFI_ANDROID_7_1)
        self.assertIsNotNone(switch_wifi, "wi-fi button not found")
        switch_wifi.click()

    def switch_off_airplane_mode(self):

        logging.info("switch off airplane mode")
        sleep(1)
        desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        platform_version = desired_capabilities.get('platformVersion')
        if LooseVersion(platform_version) >= LooseVersion("7"):  # platform_version >= "7":
            logging.info("Appium is running on Android version >= 7"
                            " (" + str(platform) + ") -- swipe to show notifications and switch airplane mode")
            # common_page = LoadClass.load_page('CommonPage')
            # common_page.setDriver(self.driver)
            Android.swipe_down_to_show_notifications(self)
            Android.swipe_down_to_show_notifications(self)
            try:
                switch_airplane_mode = self.driver.find_element(*self.configuration.Android.SWITCH_OFF_AIRPLANE_MODE_7)
            except NoSuchElementException:
                switch_airplane_mode = self.driver.find_element(*self.configuration.Android.SWITCH_AIRPLANE_MODE_7_1)
            self.assertIsNotNone(switch_airplane_mode, "airplane mode button not found")
            switch_airplane_mode.click()
            Android.swipe_up_to_hide_notifications(self)
        else:
            logging.info("turn on all network")
            self.driver.set_network_connection(6)  # this is working for Android 6 and older
        sleep(1)

    def switch_on_airplane_mode(self):

        logging.info("switch on airplane mode")
        sleep(1)
        desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        platform_version = desired_capabilities.get('platformVersion')
        if LooseVersion(platform_version) >= LooseVersion("7"):  # platform_version >= "7":
            logging.info("Appium is running on Android version >= 7"
                         " (" + str(platform) + ") -- swipe to show notifications and switch airplane mode")
            # common_page = LoadClass.load_page('CommonPage')
            # common_page.setDriver(self.driver)
            Android.swipe_down_to_show_notifications(self)
            Android.swipe_down_to_show_notifications(self)
            sleep(0.5)
            try:
                switch_airplane_mode = self.driver.find_element(*self.configuration.Android.SWITCH_ON_AIRPLANE_MODE_7)
            except NoSuchElementException:
                switch_airplane_mode = self.driver.find_element(*self.configuration.Android.SWITCH_AIRPLANE_MODE_7_1)
            self.assertIsNotNone(switch_airplane_mode, "airplane mode button not found")
            switch_airplane_mode.click()
            Android.swipe_up_to_hide_notifications(self)
        else:
            logging.info("turn off all network")
            self.driver.set_network_connection(1)  # this is working for Android 6 and older
        sleep(1)

    def turn_off_all_network(self):  # works only on Android

        logging.info("turn off network - data and wifi connections")
        self.driver.set_network_connection(0)

    # def switch_on_airplane_mode(self):
    #
    #     logging.info("switch airplane mode on")
    #     sleep(1)
    #     try:
    #         switch_on_airplane_mode = self.driver.find_element(*self.configuration.Android.SWITCH_ON_AIRPLANE_MODE_7)
    #     except NoSuchElementException:
    #         switch_on_airplane_mode = self.driver.find_element(*self.configuration.Android.SWITCH_AIRPLANE_MODE_7_1)
    #     self.assertIsNotNone(switch_on_airplane_mode, "airplane mode button not found")
    #     switch_on_airplane_mode.click()

    # def turn_on_flight_mode(self):  # works only on Android
    #
    #     logging.info("turn flight mode on")
    #
    #     desired_capabilities = DesiredCapabilities.get_desired_capabilities()
    #     platform_version = desired_capabilities.get('platformVersion')
    #     if LooseVersion(platform_version) >= LooseVersion("7"):  # platform_version >= "7":
    #         logging.warning("Appium is running on Android version >= 7"
    #                         " (" + str(platform) + ") -- swipe to show notifications and switch airplane mode")
    #         common_page = LoadClass.load_page('CommonPage')
    #         common_page.setDriver(self.driver)
    #         common_page.swipe_down_to_show_notifications()
    #         common_page.swipe_down_to_show_notifications()
    #         # common_page.switch_wifi()
    #         common_page.switch_on_airplane_mode()
    #         common_page.swipe_up_to_hide_notifications()
    #     else:
    #         logging.info("Appium is running on real device (" + str(platform) + ") = turn on flight mode")
    #         self.driver.set_network_connection(1)  # this is working for Android 6 and older
    #     sleep(0.5)

    # def turn_on_flight_mode(self):  # works only on Android
    #
    #     logging.info("turn flight mode on")
    #     self.driver.set_network_connection(1)  # not working for Android 7
    #     # self.driver.set_network_connection(2)  # switch wi-fi - not working for Android 7

    # def turn_on_all_network(self):  # works only on Android
    #
    #     logging.info("turn flight mode off")
    #
    #     desired_capabilities = DesiredCapabilities.get_desired_capabilities()
    #     platform_version = desired_capabilities.get('platformVersion')
    #     if LooseVersion(platform_version) >= LooseVersion("7"):  # platform_version >= "7":
    #         logging.warning("Appium is running on Android version >= 7"
    #                         " (" + str(platform) + ") -- swipe to show notifications and switch airplane mode")
    #         common_page = LoadClass.load_page('CommonPage')
    #         common_page.setDriver(self.driver)
    #         common_page.swipe_down_to_show_notifications()
    #         common_page.swipe_down_to_show_notifications()
    #         # common_page.switch_wifi()
    #         common_page.switch_off_airplane_mode()
    #         common_page.swipe_up_to_hide_notifications()
    #     else:
    #         logging.info("turn on all network")
    #         self.driver.set_network_connection(6)
    #     sleep(0.5)

    def clear_Search_field(self):

        logging.info("clear search field")

        search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        search_field.click()
        sleep(1)
        action = TouchAction(self.driver)
        action.long_press(el=search_field, duration=1500).perform()
        self.driver.press_keycode(67)
        sleep(0.5)
        try:
            action.long_press(el=search_field, duration=1500).perform()
            self.driver.press_keycode(67)
        except:
            pass

        # search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        # search_field.click()
        # sleep(1)
        # while len(search_field.text) > 0:
        #     action = TouchAction(self.driver)
        #     action.long_press(el=search_field, duration=1500).perform()
        #     self.driver.press_keycode(67)
        #     sleep(0.5)
        # sleep(0.5)

    # OCA top bar
    # def hamburger_button(self):
    #
    #     sleep(1)
    #     logging.info("click hamburger button to go back to main menu")

        # desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        # platform_version = desired_capabilities.get('platformVersion')
        # # if platform_version < "5":
        # hamburger_button = self.driver.find_element(*self.configuration.TopBar.HAMBURGER_FOR_MAIN_MENU_by_xpath)
        # # else:
        # #     hamburger_button = self.driver.find_element(*self.configuration.TopBar.HAMBURGER_FOR_MAIN_MENU_by_id)
        # self.assertIsNotNone(hamburger_button, "Hamburger button is not present")
        # location = hamburger_button.location
        # print(location)
        # x = location["x"]
        # y = location["y"]
        # print(x)
        # print(y)
        # positions = [(x, y)]
        # self.driver.tap(positions)
        # hamburger_button.click()
        # sleep(5)

    def alert_popup_allow(self):

        logging.info('search for alert and click "Allow" if found')

        # action = TouchAction(self.driver)
        try:
            button_allow1 = self.driver.find_element(*self.configuration.Android.ANDROID_ALLOW)
            # logging.info("Accept for example using location - device will store that info for later use")
            self.assertIsNotNone("button allow not found", button_allow1)
            button_allow1.click()
            sleep(0.5)
            # action.tap(button_allow1, count=1).perform()
        except:
            pass
        try:
            button_allow2 = self.driver.find_element(*self.configuration.Android.ANDROID_ALLOW)
            self.assertIsNotNone("button allow not found", button_allow2)
            button_allow2.click()
            sleep(0.5)
            # action.tap(button_allow2, count=1).perform()
        except:
            pass
        try:
            button_allow3 = self.driver.find_element(*self.configuration.Android.ANDROID_ALLOW)
            self.assertIsNotNone("button allow not found", button_allow3)
            button_allow3.click()
            sleep(0.5)
            # action.tap(button_allow, count=1).perform()
        except:
            pass

    def hide_keyboard(self):

        try:
            logging.info("hide screen keyboard")
            self.driver.hide_keyboard()
            sleep(1)
        except:
            logging.info("screen keyboard not found")

    # def alert_popup_allow(self):
    #
    #     logging.info('search for alert and click "Allow" if found')
    #     # action = TouchAction(self.driver)
    #     try:
    #         button_allow = self.driver.find_element(*self.configuration.Android.ANDROID_ALLOW)
    #         tries = 4
    #         while button_allow.is_displayed() and tries > 0:
    #             # self.assertIsNotNone("button allow not found", button_allow)
    #             button_allow.click()
    #             # action.tap(button_allow, count=1).perform()
    #             sleep(0.5)
    #             tries = tries - 1
    #             # if NoSuchElementException:
    #             #     break
    #     except NoSuchElementException:
    #         pass
    #     sleep(1)

    def click_Return_button_on_keyboard(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.click_search_field_in_native_view_to_display_keyboard()

        logging.info("click Go on keyboard")
        self.driver.press_keycode(66)
        sleep(1)
        # common_page = LoadClass.load_page('CommonPage')
        # common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

        # try:
        #     logging.info("click Go on keyboard")
        #     self.driver.press_keycode(66)
        #     sleep(3)
        # except NoSuchElementException:
        #     logging.info("keyboard not found")

    def scroll_down_one_view(self):
        """Method to scroll down only one screen"""

        window_size = self.driver.get_window_size()  # this will give You a dictionary
        start_x = window_size["width"] * 0.25
        start_y = window_size["height"] * 0.15
        if window_size["height"] <= 800:
            end_y = window_size["height"] * 0.6
        else:
            end_y = window_size["height"] * 0.8
        logging.info("scroll down only one screen")
        sleep(2)
        self.driver.swipe(start_x, end_y, start_x, start_y, 3000)  # each swipe is scrolling one screen
        sleep(1)

    def scroll_down_half_view(self):
        """Method to scroll down only half of the screen"""

        window_size = self.driver.get_window_size()  # this will give You a dictionary
        start_x = window_size["width"] * 0.25
        start_y = window_size["height"] * 0.15
        if window_size["height"] <= 800:
            end_y = window_size["height"] * 0.4
        else:
            end_y = window_size["height"] * 0.5
        logging.info("scroll down half of the screen")
        sleep(1)
        self.driver.swipe(start_x, end_y, start_x, start_y, 3000)  # each swipe is scrolling one screen
        sleep(1)

    def click_back_button(self):
        """ Method to handle back button for Android """

        logging.info("click 'Back' button")
        self.driver.press_keycode(4)
        # self.driver.keyevent(4)
        # self.driver.back()
        sleep(4)
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located(self.configuration.MainMenuScreen.INBOX_BUTTON),
            "Failed to locate Inbox button")

    def click_set_button(self):

        logging.info("Click 'Set' button")
        set_button = self.driver.find_element(*self.configuration.Android.ANDROID_SET_BUTTON)
        self.assertIsNotNone(set_button, "Set button was not found")
        set_button.click()

    def click_device_cancel_button(self):

        logging.info("Click 'Cancel' button")
        cancel_button = self.driver.find_element(*self.configuration.Android.ANDROID_CANCEL_BUTTON)
        self.assertIsNotNone(cancel_button, "Cancel button was not found")
        cancel_button.click()

    def click_clear_button(self):

        logging.info("Click 'Clear' button")
        clear_button = self.driver.find_element(*self.configuration.Android.ANDROID_CLEAR_BUTTON)
        self.assertIsNotNone(clear_button, "Clear button was not found")
        clear_button.click()

    def scroll_up_one_view(self):
        """Method to scroll down only one screen"""

        window_size = self.driver.get_window_size()  # this will give You a dictionary
        start_x = window_size["width"] * 0.25
        start_y = window_size["height"] * 0.15
        end_y = window_size["height"] * 0.8
        logging.info("scroll up only one screen")
        sleep(2)
        self.driver.swipe(start_x, start_y, start_x, end_y, 3000)  # each swipe is scrolling one screen
        sleep(1)

    def additional_appium_actions(self):

        # print(self.driver.contexts)
        # self.driver.refresh()  # Method has not yet been implemented
        print(self.driver.page_source)
        self.driver.press_keycode(3)  # Press Home Key
        self.driver.press_keycode(187)  # KEYCODE_APP_SWITCH
        self.driver.find_element_by_accessibility_id('OCA')  # maximize app

    # @staticmethod
    # def get_platform_version():
    #
    #     desired_capabilities = DesiredCapabilities.get_desired_capabilities()
    #     logging.info(desired_capabilities)
    #     platform_version = desired_capabilities.get('platformVersion')
    #     logging.info(platform_version)

        # if platform_version == "6.0.1":
        #     print(":)")
        # else:
        #     print("x")

    def scroll_up(self):
        """Method to scroll up to top of the screen """

        window_size = self.driver.get_window_size()  # this returns dictionary
        start_x = window_size["width"] * 0.25
        start_y = window_size["height"] * 0.20
        end_y = window_size["height"] * 0.80
        logging.info("scroll up")
        sleep(2)
        scrolls = 3  # number of swipes
        while scrolls > 0:
            self.driver.swipe(start_x, start_y, start_x, end_y, 3000)  # each swipe is scrolling one screen
            scrolls = scrolls - 1
        sleep(2)

    def scroll_down(self):
        """Method to scroll down to bottom of the screen """

        window_size = self.driver.get_window_size()  # this returns dictionary
        start_x = window_size["width"] * 0.25
        start_y = window_size["height"] * 0.20
        end_y = window_size["height"] * 0.80
        logging.info("scroll down")
        sleep(2)
        scrolls = 3  # number of swipes
        while scrolls > 0:
            self.driver.swipe(start_x, end_y, start_x, start_y, 3000)  # each swipe is scrolling one screen
            scrolls = scrolls - 1
        sleep(2)

    def power_button(self):

        logging.info("power button")
        self.driver.press_keycode(26)

    def scroll_down_to_subform_add_row_button(self):
        """Method to scroll down to bottom of the screen to subform add row button """

        window_size = self.driver.get_window_size()  # this returns dictionary
        start_x = window_size["width"] * 0.25
        # end_x = window_size["width"]*0.75
        start_y = window_size["height"] * 0.20
        end_y = window_size["height"] * 0.80
        logging.info("scroll down to subform add row button")
        sleep(1)
        scrolls = 4
        while scrolls > 0:
            self.driver.swipe(start_x, end_y, start_x, start_y, 3000)  # each swipe is scrolling one screen
            scrolls = scrolls - 1
        sleep(1)




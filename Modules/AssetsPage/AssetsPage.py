"""A class for methods to handle Assets Page """

from Modules.BasePage.BasePage import BasePage
import logging
from time import sleep
from selenium.common.exceptions import *
from Modules.load_class import LoadClass
from configuration import platform
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class AssetsPage(BasePage):

    def click_new_button(self):

        self.switch_context_to_webview()

        logging.info('click New button')
        new_button = self.driver.find_element(*self.configuration.AssetsScreen.NEW_BUTTON)
        self.assertIsNotNone(new_button, "new button not found")
        new_button.click()

        self.switch_context_to_native()

    def click_new_asset(self):

        self.switch_context_to_webview()

        logging.info('click New asset')
        new_asset = self.driver.find_element(*self.configuration.AssetsScreen.NEW_ASSET_BUTTON)
        self.assertIsNotNone(new_asset, "new asset button not found")
        new_asset.click()

        self.switch_context_to_native()

    def choose_asset_type(self):  # first asset type on the list

        self.switch_context_to_webview()

        logging.info('choose asset type')
        asset_type = self.driver.find_element(*self.configuration.AssetsScreen.ASSET_TYPE)
        self.assertIsNotNone(asset_type, "asset type not found")
        asset_type.click()

        self.switch_context_to_native()

    def choose_asset_type_with_option_list(self):  # asset type with option list

        logging.info('choose asset type with option list')
        asset_type = self.driver.find_element(*self.configuration.AssetsScreen.ASSET_TYPE_WITH_OPTION_LIST)
        self.assertIsNotNone(asset_type, "asset type not found")
        asset_type.click()

    def choose_asset_type_with_rich_text(self):  # asset type with rich text

        logging.info('choose asset type with rich text')
        asset_type = self.driver.find_element(*self.configuration.AssetsScreen.ASSET_TYPE_WITH_RICH_TEXT)
        self.assertIsNotNone(asset_type, "asset type not found")
        asset_type.click()

    def fill_Name_input_field(self, text):

        self.switch_context_to_webview()

        sleep(1)
        logging.info("type Name")
        name = self.driver.find_element(*self.configuration.AssetsScreen.NAME)
        self.assertIsNotNone(name, "Name input field was not found")
        name.click()
        name.send_keys(text)

        self.switch_context_to_native()

    def fill_name_for_edited_asset(self, text):

        self.switch_context_to_webview()

        # sleep(5)
        sleep(1)
        logging.info("type Name")
        name = self.driver.find_element(*self.configuration.AssetsScreen.NAME_FOR_EDITED_ASSET)
        self.assertIsNotNone(name, "Name input field was not found")
        name.click()
        name.send_keys(text)

        self.switch_context_to_native()

    def open_existing_asset(self):  # first child

        self.switch_context_to_webview()

        logging.info("open first asset on the list")
        sleep(1)
        open_existing_asset = self.driver.find_element(*self.configuration.AssetsScreen.PREVIOUSLY_CREATED_ASSET)
        self.assertIsNotNone(open_existing_asset, "existing asset not found")
        open_existing_asset.click()
        sleep(1)

        self.switch_context_to_native()

    def open_first_pending_asset(self):    # pending asset in offline mode

        self.switch_context_to_webview()

        try:  # appium can't enable airplane mode on IOS emulators
            logging.info("open first pending asset on the list")
            first_pending_asset = self.driver.find_element(*self.configuration.AssetsScreen.FIRST_PENDING_ASSET)
            self.assertIsNotNone(first_pending_asset, "first pending asset not found")
            first_pending_asset.click()
        except NoSuchElementException:
            AssetsPage.open_existing_asset(self)

        self.switch_context_to_native()

    def click_edit_button(self):

        self.switch_context_to_webview()

        logging.info("click edit button")

        edit = self.driver.find_element(*self.configuration.AssetsScreen.EDIT_BUTTON)
        self.assertIsNotNone(edit, "edit button not found")
        edit.click()
        sleep(1)

        self.switch_context_to_native()

    def type_cost_per_unit(self, text):

        sleep(1)
        self.switch_context_to_webview()
        sleep(1)

        logging.info("type cost per unit")
        cost_per_unit = self.driver.find_element(*self.configuration.AssetsScreen.COST_PER_UNIT_FIELD)
        self.assertIsNotNone(cost_per_unit, "Cost per unit input field was not found")
        cost_per_unit.click()
        cost_per_unit.send_keys(text)

        self.switch_context_to_native()

    def type_cost_per_unit_for_new_asset(self, text):  # in offline mode app is using new objects all the time

        sleep(1)
        self.switch_context_to_webview()

        logging.info("type cost per unit")
        try:
            cost_per_unit = self.driver.find_element(*self.configuration.AssetsScreen.COST_PER_UNIT_FIELD)
        except WebDriverException:
            cost_per_unit = self.driver.find_element(*self.configuration.AssetsScreen.COST_PER_UNIT_FIELD_IN_NEW_ASSET)
        self.assertIsNotNone(cost_per_unit, "Cost per unit input field was not found")
        cost_per_unit.click()
        cost_per_unit.send_keys(text)

        self.switch_context_to_native()

    def click_save_button(self):

        logging.info("click Save button")
        try:
            save_button = self.driver.find_element(*self.configuration.CommonScreen.SAVE_BUTTON)
            self.assertIsNot(save_button, "Save button not found")
            save_button.click()
        except NoSuchElementException:
            self.switch_context_to_webview()
            save_button = self.driver.find_element(*self.configuration.AssetsScreen.SAVE_BUTTON)
            self.assertIsNot(save_button, "Save button not found")
            save_button.click()
            self.switch_context_to_native()

    def save_edited_asset(self):

        logging.info('click Save button')
        try:
            save_button = self.driver.find_element(*self.configuration.CommonScreen.SAVE_BUTTON)
            self.assertIsNot(save_button, "Save button not found")
            save_button.click()
        except NoSuchElementException:
            self.switch_context_to_webview()
            save_button = self.driver.find_element(*self.configuration.AssetsScreen.SAVE_EDITED_ASSET)
            self.assertIsNot(save_button, "Save button not found")
            save_button.click()
            self.switch_context_to_native()

    # def click_more_button(self):
    #
    #     self.switch_context_to_webview()
    #
    #     logging.info("click more button")
    #
    #     try:
    #         logging.info("try 1")
    #         click_more_button = self.driver.find_element(*self.configuration.AssetsScreen.MORE_BUTTON)
    #     except NoSuchElementException:
    #         logging.info("except 1")
    #         click_child_asset_inside_other_asset = self.driver.find_element(*self.configuration.AssetsScreen.CHILD_ASSET_INSIDE_OTHER_ASSET)
    #         self.assertIsNotNone(click_child_asset_inside_other_asset, "child asset inside other asset not found")
    #         click_child_asset_inside_other_asset.click()
    #         sleep(1)
    #     try:
    #         logging.info("try 2")
    #         click_more_button = self.driver.find_element(*self.configuration.AssetsScreen.MORE_BUTTON)
    #     except NoSuchElementException:
    #         logging.info("except 2")
    #         click_child_asset_inside_other_asset = self.driver.find_element(*self.configuration.AssetsScreen.CHILD_ASSET_INSIDE_OTHER_ASSET)
    #         self.assertIsNotNone(click_child_asset_inside_other_asset, "child asset inside other asset not found")
    #         click_child_asset_inside_other_asset.click()
    #         sleep(1)
    #
    #     logging.info("after all")
    #     sleep(20)
    #     click_more_button = self.driver.find_element(*self.configuration.AssetsScreen.MORE_BUTTON)
    #     self.assertIsNotNone(click_more_button, "More button not found")
    #     click_more_button.click()
    #
    #     self.switch_context_to_native()

    def click_more_button(self):

        self.switch_context_to_webview()

        logging.info("click more button")
        click_more_button = self.driver.find_element(*self.configuration.AssetsScreen.MORE_BUTTON)
        self.assertIsNotNone(click_more_button, "More button not found")
        click_more_button.click()

        self.switch_context_to_native()

    # def click_more_button(self):

        # logging.info("click more button")
        # # when existing asset already have a child asset, instead "More" button there is "New" button
        # self.switch_context_to_webview()

        # n = int(1)
        # logging.info(n)
        # var = 10
        # while var > 0:
        #     logging.info("loop")
        #     try:
        #         logging.info("check if More button is present and click it")
        #         click_more_button = self.driver.find_element(*self.configuration.AssetsScreen.MORE_BUTTON)
        #         if click_more_button.is_displayed():
        #             self.assertIsNotNone(click_more_button, "More button not found")
        #             click_more_button.click()
        #             break
        #         else:
        #             pass
        #     except NoSuchElementException:
        #         logging.info("More button not found - clicking back arrow and choosing different existing asset")
        #         back_arrow = self.driver.find_element(*self.configuration.TopBar.BACK_ARROW)
        #         self.assertIsNotNone(back_arrow, "back arrow not found")
        #         back_arrow.click()  # return to assets list
        #
        #         # now open nth + 1 asset
        #         css_selector = list('div#assetTreeView>div.ui-content>div.main>ul[data-role="listview"]>li:nth-child(1)>a')
        #         logging.info(css_selector)
        #
        #         n = n + 1
        #         logging.info(n)
        #
        #         css_selector[-4] = str(n)
        #         logging.info(n)
        #         logging.info(css_selector)
        #
        #         open_existing_asset = self.driver.find_element_by_css_selector(''.join(css_selector))
        #         # self.assertIsNotNone(open_existing_asset, "existing asset not found")
        #         open_existing_asset.click()
        #
        #     var = var - 1
        #
        # self.switch_context_to_native()

    def click_delete_this_asset(self):

        self.switch_context_to_webview()

        logging.info("click delete asset")
        click_delete_asset = self.driver.find_element(*self.configuration.AssetsScreen.DELETE_THIS_ASSET)
        self.assertIsNotNone(click_delete_asset, "Delete asset button not found")
        click_delete_asset.click()

        self.switch_context_to_native()

    def alert_accept_delete(self):

        self.switch_context_to_webview()

        logging.info("alert accept delete")
        alert_accept_delete = self.driver.find_element(*self.configuration.AssetsScreen.DELETE_ALERT)
        self.assertIsNotNone(alert_accept_delete, "Delete button on alert not found")
        alert_accept_delete.click()

        self.switch_context_to_native()

    def click_new_child_asset(self):

        self.switch_context_to_webview()

        logging.info("click new child asset")
        new_child_asset = self.driver.find_element(*self.configuration.AssetsScreen.NEW_CHILD_ASSET)
        self.assertIsNotNone(new_child_asset, "New child asset button not found")
        new_child_asset.click()

        self.switch_context_to_native()

    def open_existing_child_asset(self):

        self.switch_context_to_webview()

        logging.info("open first child asset on the list")

        open_existing_child_asset = self.driver.find_element(*self.configuration.AssetsScreen.PREVIOUSLY_CREATED_CHILD_ASSET)
        self.assertIsNotNone(open_existing_child_asset, "existing child asset not found")
        open_existing_child_asset.click()
        sleep(1)

        self.switch_context_to_native()

    def type_text_into_search_field(self, text):

        logging.info("type text into search field")

        self.switch_context_to_webview()

        search_field = self.driver.find_element(*self.configuration.AssetsScreen.SEARCH_FIELD)
        self.assertIsNotNone(search_field, "Search field not found")
        search_field.click()
        sleep(1)
        search_field.send_keys(text)
        sleep(1)

        self.switch_context_to_native()

    # def type_text_into_search_field(self, text):
    #
    #     sleep(1)
    #     events_page = LoadClass.load_page('EventsPage')
    #     events_page.setDriver(self.driver)
    #     events_page.type_text_into_search_field(text)

        # sleep(1)
        # logging.info("type text into search field")
        # search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        # self.assertIsNotNone(search_field, "Search field not found")
        # search_field.click()
        # sleep(2)
        # search_field.send_keys(text)
        # sleep(1)

    def check_result_for_asset_with_name_containing_map(self):

        logging.info("check result")
        try:
            created_map_asset = self.driver.find_elements(*self.configuration.AssetsScreen.CREATED_MAP_ASSET)
            # self.assertIsNotNone(created_map_asset[1], "created map asset not found")
            self.assertIsNotNone(created_map_asset[0], "created map asset not found")
        except NoSuchElementException or IndexError:
            logging.error("created map asset not found")

    def check_result_for_asset_with_name_containing_ballart(self):

        logging.info("check result")
        created_map_asset = self.driver.find_elements(*self.configuration.AssetsScreen.CREATED_ASSET_WITH_NAME_BALLART)
        # self.assertIsNotNone(created_map_asset[1], "created map asset not found")
        self.assertIsNotNone(created_map_asset[0], "created asset named: 'Ballart' not found")

    # def clear_Search_field(self):
    #
    #     logging.info("clear search field")
    #     sleep(1)
    #     self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).click()
    #     self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
    #     self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
    #     self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
    #     sleep(1)

    def choose_asset_type_with_max_number_of_fields(self):

        logging.info('choose asset type with max number of fields')
        asset_type = self.driver.find_element(*self.configuration.AssetsScreen.ASSET_TYPE_WITH_MAX_NUMBER_OF_FIELDS)
        self.assertIsNotNone(asset_type, "asset type with max number of fields not found")
        asset_type.click()

    def choose_asset_type_with_visibility_rules(self):

        logging.info('choose asset type with visibility rules')
        asset_type = self.driver.find_element(*self.configuration.AssetsScreen.ASSET_TYPE_WITH_VISIBILITY_RULES)
        self.assertIsNotNone(asset_type, "asset type with visibility rules not found")
        asset_type.click()

    def click_create_mapping_data_for_new_asset(self):

        self.switch_context_to_webview()

        logging.info("create mapping data")

        click_create_mapping_data = self.driver.find_element(*self.configuration.AssetsScreen.CREATE_MAPPING_DATA)
        self.assertIsNotNone(click_create_mapping_data, "create mapping data not found")
        click_create_mapping_data.click()
        sleep(1)

        self.switch_context_to_native()

    def click_add_media(self):

        self.switch_context_to_webview()

        sleep(1)
        logging.info("click add media")

        click_add_media = self.driver.find_element(*self.configuration.AssetsScreen.ADD_MEDIA_BUTTON)
        self.assertIsNotNone(click_add_media, "add media button not found")
        click_add_media.click()
        sleep(1)

        self.switch_context_to_native()

    def click_on_option_list(self):

        event_edit_page = LoadClass.load_page('EventsPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.click_on_option_list()

    def click_on_option_1(self):

        event_edit_page = LoadClass.load_page('EventsPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.click_on_option_1()

    def click_on_option_2(self):

        event_edit_page = LoadClass.load_page('EventsPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.click_on_option_2()

    def click_on_option_3(self):

        event_edit_page = LoadClass.load_page('EventsPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.click_on_option_3()

    def check_restored_field_1(self):

        logging.info("assert restored field 1")

        self.switch_context_to_webview()

        field_to_restore_1_header = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_1_HEADER)
        self.assertIsNotNone(field_to_restore_1_header)

        self.switch_context_to_native()

        field_to_restore_1_value = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_1_VALUE)
        self.assertIsNotNone(field_to_restore_1_value)

    def check_restored_field_2(self):

        logging.info("assert restored field 2")

        self.switch_context_to_webview()

        field_to_restore_2_header = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_2_HEADER)
        self.assertIsNotNone(field_to_restore_2_header)

        self.switch_context_to_native()

        field_to_restore_2_value = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_2_VALUE)
        self.assertIsNotNone(field_to_restore_2_value)

    def check_restored_field_3(self):

        logging.info("assert restored field 3")

        self.switch_context_to_webview()

        field_to_restore_3_header = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_3_HEADER)
        self.assertIsNotNone(field_to_restore_3_header)

        self.switch_context_to_native()

        field_to_restore_3_value = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_3_VALUE)
        self.assertIsNotNone(field_to_restore_3_value)

    def check_hidden_field_1(self):

        event_edit_page = LoadClass.load_page('EventsPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.check_hidden_field_1()

    def check_hidden_fields_1_and_2(self):

        event_edit_page = LoadClass.load_page('EventsPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.check_hidden_fields_1_and_2()

    def click_back_arrow_if_running_on_ios_emulator(self):

        logging.info("click back arrow if running on emulator")

        logging.info("Appium is running on: " + str(platform))

        if "emulator" in str(platform):
            logging.info("Appium is running on emulator = click back arrow")
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.back_arrow()
        else:
            pass

    def click_back_arrow_if_running_on_emulators(self):

        logging.info("click back arrow if running on emulator")

        logging.info("Appium is running on: " + str(platform))

        if "emulator" in str(platform):
            logging.info("Appium is running on emulator = click back arrow")
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.back_arrow()
        else:
            pass

    def clear_Search_field(self):

        self.switch_context_to_webview()

        try:
            clear_search_field_button = self.driver.find_element(*self.configuration.AssetsScreen.CLEAR_SEARCH_FIELD_BUTTON)
            if clear_search_field_button.is_displayed():
                logging.info("clear Search field by clicking clear button")
                self.assertIsNotNone(clear_search_field_button, "clear search field button not found")
                clear_search_field_button.click()
                sleep(2)
        except NoSuchElementException:
            pass

        self.switch_context_to_native()

    def check_if_view_on_map_button_is_present(self):

        self.switch_context_to_webview()

        logging.info("check if view on map button is present")
        view_on_map_button = self.driver.find_element(*self.configuration.AssetsScreen.VIEW_ON_MAP_BUTTON)
        self.assertIsNotNone(view_on_map_button, "view on map button not found")

        self.switch_context_to_native()

    def check_notification_about_offline_mode(self):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.check_notification_about_offline_mode()

    def ok_button_on_offline_notification_popup(self):

        self.switch_context_to_webview()

        logging.info("click Ok button on offline notification popup")
        try:
            ok_button = self.driver.find_element(*self.configuration.AssetsScreen.OK_BUTTON_ON_OFFLINE_NOTIFICATION_POPUP)
            self.assertIsNotNone(ok_button, "ok button not found")
            ok_button.click()
        except NoSuchElementException:
            logging.warning("offline notification popup not present")
        sleep(1)

        self.switch_context_to_native()

    def read_only_option_list_for_new_asset(self):

        self.switch_context_to_webview()

        logging.info("click option list - Is Read Only ?")

        option_list = self.driver.find_element(*self.configuration.AssetsScreen.OPTION_LIST_READ_ONLY)
        self.assertIsNotNone(option_list, "option list - Is Read Only ?, not found")
        option_list.click()

        self.switch_context_to_native()

    def read_only_option_list_for_edit_asset(self):

        self.switch_context_to_webview()

        logging.info("click option list - Is Read Only ?")

        option_list = self.driver.find_element(*self.configuration.AssetsScreen.OPTION_LIST_READ_ONLY_EDIT)
        self.assertIsNotNone(option_list, "option list - Is Read Only ?, not found")
        option_list.click()

        self.switch_context_to_native()

    # def read_only_option_list(self):
    #
    #     self.switch_context_to_webview()
    #
    #     logging.info("click option list - Is Read Only ?")
    #
    #     try:
    #         option_list = self.driver.find_element(*self.configuration.AssetsScreen.OPTION_LIST_READ_ONLY)
    #         if option_list.is_displayed():
    #             self.assertIsNotNone(option_list, "option list - Is Read Only ?, not found")
    #             option_list.click()
    #         # else:
    #         #     raise ValueError("option list element not displayed")
    #     except NoSuchElementException or WebDriverException:
    #         option_list = self.driver.find_element(*self.configuration.AssetsScreen.OPTION_LIST_READ_ONLY_EDIT)
    #         if option_list.is_displayed():
    #             self.assertIsNotNone(option_list, "option list - Is Read Only ?, not found")
    #             option_list.click()
    #         else:
    #             self.fail("Read Only option list, not found")
    #
    #     self.switch_context_to_native()

    def option_list_option_yes_a(self):

        self.switch_context_to_webview()

        logging.info('choose "Yes A" in "Is Read Only ?" option list')

        option = self.driver.find_element(*self.configuration.AssetsScreen.OPTION_LIST_OPTION_YES_A)
        self.assertIsNotNone(option, "option list - Is Read Only ?, not found")
        option.click()

        self.switch_context_to_native()

    def option_list_option_yes_b(self):

        self.switch_context_to_webview()

        logging.info('choose "Yes B" in "Is Read Only ?" option list')

        option = self.driver.find_element(*self.configuration.AssetsScreen.OPTION_LIST_OPTION_YES_B)
        self.assertIsNotNone(option, "option list - Is Read Only ?, not found")
        option.click()

        self.switch_context_to_native()

    def option_list_option_no(self):

        self.switch_context_to_webview()

        logging.info('choose "No" in "Is Read Only ?" option list')

        option = self.driver.find_element(*self.configuration.AssetsScreen.OPTION_LIST_OPTION_NO)
        self.assertIsNotNone(option, "option list - Is Read Only ?, not found")
        option.click()

        self.switch_context_to_native()

    def save_option_list(self):

        logging.info("save option list")

        option_list_save_button = self.driver.find_element(*self.configuration.AssetsScreen.SAVE_OPTION_LIST)
        self.assertIsNotNone(option_list_save_button, "Option list save button, not found")
        option_list_save_button.click()

    def check_invisibility_of_second_set_of_fields(self):

        logging.info("check invisibility of second set of fields in object with option list")

        try:
            new_date_optional_time2 = self.driver.find_element(*self.configuration.AssetsScreen.NEW_DATE_OPTIONAL_TIME2)
            if new_date_optional_time2.is_displayed():
                self.fail("second set of fields in object with option list is visible")
            else:
                logging.warning("PASUJE BO NIE WIDZE")
                pass
        except NoSuchElementException:
            logging.info("second set of fields in object with option list is not visible = OK")

    # def check_if_first_set_of_fields_in_asset_with_option_list_is_disabled(self):
    #
    #     logging.info('check if "New phone number" field in first set of fields inside object with option list,'
    #                  ' is disabled - field should be read only')
    #     sleep(1)
    #     try:
    #         new_date_optional_time_disabled = self.driver.find_element(*self.configuration.AssetsScreen.NEW_PHONE_NUMBER_DISABLED_1)
    #     except NoSuchElementException:
    #         new_date_optional_time_disabled = self.driver.find_element(*self.configuration.AssetsScreen.NEW_PHONE_NUMBER_DISABLED_2)
    #     # if new_date_optional_time_disabled.is_displayed():  # not working
    #     if new_date_optional_time_disabled:
    #         self.assertIsNotNone(new_date_optional_time_disabled, "New phone number field not found")
    #         logging.info("New phone number field is disabled")
    #     else:
    #         logging.warning("New phone number field is not read only")
    #         self.fail("New phone number field is not read only")

    def check_if_first_set_of_fields_in_asset_with_option_list_is_disabled(self):

        self.switch_context_to_native()

        logging.info('check if "New phone number" field in first set of fields inside object with option list,'
                     ' is disabled - field should be read only')
        sleep(1)
        try:
            try:
                new_date_optional_time_disabled = self.driver.find_element(*self.configuration.AssetsScreen.NEW_PHONE_NUMBER_DISABLED_1)
            except NoSuchElementException:
                new_date_optional_time_disabled = self.driver.find_element(*self.configuration.AssetsScreen.NEW_PHONE_NUMBER_DISABLED_2)
            if new_date_optional_time_disabled:
                self.assertIsNotNone(new_date_optional_time_disabled, "New phone number field not found")
                logging.info("New phone number field is disabled = OK")
            else:
                logging.error("New phone number field is not read only")
                self.fail("New phone number field is not read only")
        except NoSuchElementException:
            logging.error("New phone number field is not read only")
            self.fail("New phone number field is not read only")
            # logging.error("New phone number field is not read only")

    def check_fields_for_values_and_read_only_property(self):

        logging.info('check read only fields for read only property and default values')

        try:
            try:
                new_phone_number_disabled = self.driver.find_element(*self.configuration.AssetsScreen.NEW_PHONE_NUMBER_DISABLED_1)
            except NoSuchElementException:
                new_phone_number_disabled = self.driver.find_element(*self.configuration.AssetsScreen.NEW_PHONE_NUMBER_DISABLED_2)
            try:
                new_fax_number_disabled = self.driver.find_element(*self.configuration.AssetsScreen.NEW_FAX_NUMBER_DISABLED_1)
            except NoSuchElementException:
                new_fax_number_disabled = self.driver.find_element(*self.configuration.AssetsScreen.NEW_FAX_NUMBER_DISABLED_2)
            new_email_address_disabled = self.driver.find_element(*self.configuration.AssetsScreen.NEW_EMAIL_ADDRESS_DISABLED)
            self.assertIsNotNone(new_phone_number_disabled, "new phone number disabled field not found")
            self.assertIsNotNone(new_fax_number_disabled, "new fax number disabled field not found")
            self.assertIsNotNone(new_email_address_disabled, "new email address disabled field not found")
        except NoSuchElementException:
            self.fail("Read only fields are not read only or/and default values are not set")
            # pass

    def check_fields_for_default_values(self):

        logging.info('check read only fields')

        try:
            new_phone_number = self.driver.find_element(*self.configuration.AssetsScreen.NEW_PHONE_NUMBER)
            new_fax_number = self.driver.find_element(*self.configuration.AssetsScreen.NEW_FAX_NUMBER)
            new_email_address = self.driver.find_element(*self.configuration.AssetsScreen.NEW_EMAIL_ADDRESS)
            self.assertIsNotNone(new_phone_number, "new phone number value not found")
            self.assertIsNotNone(new_fax_number, "new fax number value not found")
            self.assertIsNotNone(new_email_address, "new email address value not found")
        except NoSuchElementException:
            logging.warning("Read only fields are not read only")
            pass

    def fill_new_single_line_text2(self, text):

        logging.info("fill new single line text 2 field")

        self.switch_context_to_webview()

        field = self.driver.find_element(*self.configuration.AssetsScreen.NEW_SINGLE_LINE_TEXT2)
        self.assertIsNotNone(field, "input field not found")
        field.click()
        field.clear()
        field.send_keys(text)

        self.switch_context_to_native()

    def fill_new_phone_number2(self, text):

        logging.info("fill new phone number 2 field")

        self.switch_context_to_webview()

        field = self.driver.find_element(*self.configuration.AssetsScreen.NEW_PHONE_NUMBER2)
        self.assertIsNotNone(field, "input field not found")
        field.click()
        field.clear()
        field.send_keys(text)

        self.switch_context_to_native()

    def fill_new_multi_line_text2(self, text):

        logging.info("fill new multi line text 2 field")

        self.switch_context_to_webview()

        field = self.driver.find_element(*self.configuration.AssetsScreen.NEW_MULTI_LINE_TEXT2)
        self.assertIsNotNone(field, "input field not found")
        field.click()
        field.clear()
        field.send_keys(text)

        self.switch_context_to_native()

    def fill_new_fax_number2(self, text):

        logging.info("fill new fax number 2 field")

        self.switch_context_to_webview()

        field = self.driver.find_element(*self.configuration.AssetsScreen.NEW_FAX_NUMBER2)
        self.assertIsNotNone(field, "input field not found")
        field.click()
        field.clear()
        field.send_keys(text)

        self.switch_context_to_native()

    def fill_new_mobile_number2(self, text):

        logging.info("fill new mobile number 2 field")

        self.switch_context_to_webview()

        field = self.driver.find_element(*self.configuration.AssetsScreen.NEW_MOBILE_NUMBER2)
        self.assertIsNotNone(field, "input field not found")
        field.click()
        field.clear()
        field.send_keys(text)

        self.switch_context_to_native()

    def fill_new_email_address2(self, text):

        logging.info("fill new email address 2 field")

        self.switch_context_to_webview()

        field = self.driver.find_element(*self.configuration.AssetsScreen.NEW_EMAIL_ADDRESS2)
        self.assertIsNotNone(field, "input field not found")
        field.click()
        field.clear()
        field.send_keys(text)

        self.switch_context_to_native()

    def fill_new_rich_text2(self, text):

        logging.info("fill new rich text 2 field")

        self.switch_context_to_webview()

        field = self.driver.find_element(*self.configuration.AssetsScreen.NEW_RICH_TEXT2)
        self.assertIsNotNone(field, "input field not found")
        field.send_keys(text)

        self.switch_context_to_native()

    def fill_new_number2(self, text):

        logging.info("fill new number 2 field")

        self.switch_context_to_webview()

        field = self.driver.find_element(*self.configuration.AssetsScreen.NEW_NUMBER2)
        self.assertIsNotNone(field, "input field not found")
        field.click()
        field.clear()
        field.send_keys(text)

        self.switch_context_to_native()

    def fill_new_website_address2(self, text):

        logging.info("fill new website address 2 field")

        self.switch_context_to_webview()

        field = self.driver.find_element(*self.configuration.AssetsScreen.NEW_WEBSITE_ADDRESS2)
        self.assertIsNotNone(field, "input field not found")
        field.click()
        field.clear()
        field.send_keys(text)

        self.switch_context_to_native()

    def scroll_down_one_view(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

    def check_presence_of_image_inside_rich_text_field(self):

        logging.info("View object screen - check presence of image inside rich text field")

        self.switch_context_to_webview()

        self.driver.switch_to.frame(self.driver.find_element(
            *self.configuration.AssetsScreen.RICH_TEXT_IFRAME_VIEW_ASSET))
        image = self.driver.find_element(*self.configuration.AssetsScreen.RICH_TEXT_IFRAME_IMG_TAG)
        self.assertIsNotNone(image, "image tag not found")

        WebDriverWait(self.driver, 7).until(expected_conditions.visibility_of_element_located(
            self.configuration.AssetsScreen.RICH_TEXT_IFRAME_IMAGE_NAME))

        self.driver.switch_to.default_content()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.get_page_source()

        self.switch_context_to_native()

    def check_presence_of_image_inside_rich_text_field_in_subform(self):

        logging.info("View object screen - check presence of image inside rich text field located in subform")

        self.switch_context_to_webview()

        self.driver.switch_to.frame(self.driver.find_element(
            *self.configuration.AssetsScreen.RICH_TEXT_IFRAME_INSIDE_SUBFORM_VIEW_ASSET))
        image = self.driver.find_element(*self.configuration.AssetsScreen.RICH_TEXT_IFRAME_IMG_TAG)
        self.assertIsNotNone(image, "image tag not found")

        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            self.configuration.AssetsScreen.RICH_TEXT_IFRAME_INSIDE_SUBFORM_IMAGE_NAME))

        self.driver.switch_to.default_content()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.get_page_source()

        self.switch_context_to_native()

    def add_subform_row(self):

        logging.info("click 'Add row' button inside subform")

        self.switch_context_to_webview()

        add_row_button = self.driver.find_element(*self.configuration.AssetsScreen.SUBFORM_ADD_ROW)
        self.assertIsNotNone(add_row_button, "Add row button not found")
        add_row_button.click()

        self.switch_context_to_native()









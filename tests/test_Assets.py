# Test Case - Assets -- OCAMOB-50

# before running this test prepare sample video file on device/emulator and create necessary asset types:

# - assets types named: "asset_with_visibility_rules", "asset_with_max_number_of_fields". Asset type with visibility rules with fields:
# "New option list" - with options; "1", "2", "3" that options should restore 3 other fields. "field to restore",
# "New website address" with value: "http://bitnoi.se/" and "New email address" with value: "test@noggin.com" - visibility rules like in TC: Managing Events
# (option 1 restores field to restore, option 2 restores New email address field, option 3 restores New website address)

# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present
# From the main menu click on Assets

# Assets > New > New Asset > Select Type > Create and save
# Asset > open asset > Click on Edit > Update and save
# Asset > Select asset > More > Delete this asset
# Create a Child Asset Asset > Select asset > More > New Child asset > select type > Create asset
# Edit child asset Asset > Select parent > Child is displayed >Select Child > Edit
# Delete child asset Asset > Select parent > Child is displayed >Select Child > More > Delete this asset
# Create an Asset from Map Maps > Layers > Select layers > Tools > Plot a point, line, circle or polygon > Create > Asset > Type > Save
# Click on Assets>Search Assets

# Login to OCA server >Create a new Asset type >Login to OCA mobile app >Click on Assets>New>Select the new asset type created above  -- can't be done using Appium

# Scroll down/Up the Asset list view
# Load an assets with max number of fields
# Click on Asset>Create Asset>New>Select a type>Click on Create mapping data>Add point/line/Circle/Polygon> Click on Add media >Add all files (audio,Video,Document)
# Create an asset that has option lists and fields with visibility rules that clears hidden fields and restores default values.


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest
from time import sleep
import os


class TestAssets(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        path = "./screenshots"
        os.chdir(path)
        self.driver.save_screenshot("test_Assets" + ".png")
        os.chdir("..")

        self.driver.quit()

    def test_Assets(self):

        logging.info("starting Test Case: Assets")
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

        # Assets > New > New Asset > Select Type > Create and save
        main_page.open_ASSETS()
        assets_page = LoadClass.load_page('AssetsPage')
        assets_page.setDriver(self.driver)
        assets_page.click_new_button()
        assets_page.click_new_asset()
        assets_page.choose_asset_type()
        assets_page.fill_Name_input_field("Asset test")
        assets_page.scroll_down_to_save_button()
        assets_page.click_save_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Asset > open asset > Click on Edit > Update and save
        main_page.open_ASSETS()
        assets_page.open_existing_asset()
        assets_page.click_edit_button()
        assets_page.type_cost_per_unit("2")
        common_page.hide_keyboard()
        assets_page.scroll_down_to_save_button()
        assets_page.save_edited_asset()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Asset > Select asset > More > Delete this asset
        main_page.open_ASSETS()
        assets_page.open_existing_asset()
        assets_page.click_more_button()
        assets_page.click_delete_this_asset()
        assets_page.alert_accept_delete()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Create a Child Asset Asset > Select asset > More > New Child asset > select type > Create asset

        # create parent asset
        main_page.open_ASSETS()
        assets_page = LoadClass.load_page('AssetsPage')
        assets_page.setDriver(self.driver)
        assets_page.click_new_button()
        assets_page.click_new_asset()
        assets_page.choose_asset_type()
        assets_page.fill_Name_input_field("Asset test 2")
        assets_page.scroll_down_to_save_button()
        assets_page.click_save_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_ASSETS()
        assets_page.open_existing_asset()
        assets_page.click_more_button()
        assets_page.click_new_child_asset()
        assets_page.choose_asset_type()
        assets_page.fill_Name_input_field("Child Asset test")
        assets_page.scroll_down_to_save_button()
        assets_page.click_save_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Edit child asset Asset > Select parent > Child is displayed > Select Child > Edit
        main_page.open_ASSETS()
        assets_page.open_existing_asset()
        assets_page.open_existing_child_asset()
        assets_page.click_edit_button()
        assets_page.type_cost_per_unit("4")
        common_page.hide_keyboard()
        assets_page.scroll_down_to_save_button()
        assets_page.save_edited_asset()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Delete child asset Asset > Select parent > Child is displayed > Select Child > More > Delete this asset
        main_page.open_ASSETS()
        assets_page.open_existing_asset()
        assets_page.open_existing_child_asset()
        assets_page.click_more_button()
        assets_page.click_delete_this_asset()
        assets_page.alert_accept_delete()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Create an Asset from Map Maps > Layers > Select layers > Tools > Plot a point, line, circle or polygon > Create > Asset > Type > Save
        main_page.open_MAP()
        map_page = LoadClass.load_page('MapPage')
        map_page.setDriver(self.driver)
        common_page.alert_popup_allow()
        map_page.click_layers_button()
        map_page.choose_first_layer_from_the_list()
        map_page.click_done_button()
        map_page.click_plot_button()
        map_page.click_tool_button()
        map_page.click_point_button()
        map_page.click_default_button()
        map_page.click_in_map_area_1()
        map_page.click_tool_button()
        map_page.click_line_button()
        map_page.click_default_button()
        map_page.click_in_map_area_2()
        map_page.double_tap_on_map()
        map_page.click_tool_button()
        map_page.click_circle_button()
        map_page.click_default_button()
        map_page.click_in_map_area_2()
        map_page.click_tool_button()
        map_page.click_polygon_button()
        map_page.click_default_button()
        map_page.click_in_map_area_1()
        map_page.click_in_map_area_2()
        map_page.double_tap_on_map()
        map_page.save_map()
        map_page.choose_plot_type_asset()
        assets_page.choose_asset_type()
        assets_page.fill_Name_input_field("Map asset")
        assets_page.scroll_down_to_save_button()
        assets_page.click_save_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Click on Assets > Search Assets
        main_page.open_ASSETS()
        assets_page.type_text_into_search_field("Map asset")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        assets_page.check_result_for_asset_with_name_containing_map()
        assets_page.clear_Search_field()
        common_page.hide_keyboard()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Login to OCA server >Create a new Asset type >Login to OCA mobile app >Click on Assets>New>Select the new asset type created above  -- can't be done using Appium

        # Scroll down/Up the Asset list view
        main_page.open_ASSETS()
        assets_page.scroll_down()
        assets_page.scroll_up()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Load an assets with max number of fields    - add to readme to create that that type and that bellow
        main_page.open_ASSETS()
        assets_page.click_new_button()
        assets_page.click_new_asset()
        assets_page.choose_asset_type_with_max_number_of_fields()
        assets_page.fill_Name_input_field("Asset with max number of fields")
        assets_page.scroll_down_to_save_button()
        assets_page.click_save_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Click on Asset>Create Asset>New>Select a type>Click on Create mapping data>Add point/line/Circle/Polygon> Click on Add media >Add all files (audio,Video,Document)
        main_page.open_ASSETS()
        assets_page.click_new_button()
        assets_page.click_new_asset()
        assets_page.choose_asset_type()
        assets_page.fill_Name_input_field("Asset with mapping data and media files")
        assets_page.click_create_mapping_data_for_new_asset()
        common_page.alert_popup_allow()
        map_page.click_tool_button()
        map_page.click_point_button()
        map_page.click_default_button()
        map_page.click_in_map_area_1()
        map_page.click_tool_button()
        map_page.click_line_button()
        map_page.click_default_button()
        map_page.click_in_map_area_2()
        map_page.double_tap_on_map()
        map_page.click_tool_button()
        map_page.click_circle_button()
        map_page.click_default_button()
        map_page.click_in_map_area_2()
        map_page.click_tool_button()
        map_page.click_polygon_button()
        map_page.click_default_button()
        map_page.click_in_map_area_1()
        map_page.click_in_map_area_2()
        map_page.double_tap_on_map()
        map_page.save_map()

        assets_page.click_add_media()
        select_media_page = LoadClass.load_page('SelectMediaPage')
        select_media_page.setDriver(self.driver)
        select_media_page.click_take_photo()
        common_page.alert_popup_allow()
        camera_page = LoadClass.load_page('CameraPage')
        camera_page.setDriver(self.driver)
        camera_page.capture_photo()
        camera_page.click_use_photo()
        common_page.alert_popup_allow()
        assets_page.click_back_arrow_if_running_on_ios_emulator()
        common_page.push_sample_video_file()  # push sample video file for emulators
        assets_page.click_add_media()
        select_media_page.click_video_gallery()
        common_page.alert_popup_allow()
        gallery_video_page = LoadClass.load_page('GalleryPage')
        gallery_video_page.setDriver(self.driver)
        gallery_video_page.choose_videos_gallery()
        gallery_video_page.choose_element_from_gallery()
        gallery_video_page.click_use_button()
        common_page.alert_popup_allow()
        assets_page.click_add_media()
        select_media_page.click_record_audio()
        common_page.alert_popup_allow()
        sound_recorder = LoadClass.load_page('SoundRecorderPage')
        sound_recorder.setDriver(self.driver)
        sound_recorder.record_sound()
        sleep(1)  # time for recording sound
        sound_recorder.stop_recording()
        sound_recorder.click_done_button()
        assets_page.click_back_arrow_if_running_on_emulators()
        assets_page.scroll_down_to_save_button()
        assets_page.click_save_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Create an asset that has option lists and fields with visibility rules that clears hidden fields and restores default values
        main_page.open_ASSETS()
        assets_page.click_new_button()
        assets_page.click_new_asset()
        assets_page.choose_asset_type_with_visibility_rules()
        assets_page.fill_Name_input_field("Asset with visibility rules")
        assets_page.click_on_option_list()
        assets_page.click_on_option_1()
        assets_page.check_restored_field_1()
        assets_page.click_on_option_list()
        assets_page.click_on_option_2()
        assets_page.check_restored_field_2()
        assets_page.check_hidden_field_1()
        assets_page.click_on_option_list()
        assets_page.click_on_option_3()
        assets_page.check_hidden_fields_1_and_2()
        assets_page.check_restored_field_3()
        assets_page.scroll_down_to_save_button()
        assets_page.click_save_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAssets)
    unittest.TextTestRunner(verbosity=2).run(suite)

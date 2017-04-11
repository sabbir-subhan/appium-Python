"""A class for methods to handle Assets Page """

from Modules.BasePage.BasePage import BasePage
import logging
from time import sleep
from selenium.common.exceptions import *


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

    def choose_asset_type(self):

        self.switch_context_to_webview()

        logging.info('choose asset type')
        asset_type = self.driver.find_element(*self.configuration.AssetsScreen.ASSET_TYPE)
        self.assertIsNotNone(asset_type, "asset type not found")
        asset_type.click()

        self.switch_context_to_native()

    def fill_Name_input_field(self, text):

        self.switch_context_to_webview()

        logging.info("type title")
        title = self.driver.find_element(*self.configuration.AssetsScreen.NAME)
        self.assertIsNotNone(title, "Title input field was not found")
        title.click()
        title.send_keys(text)

        self.switch_context_to_native()

        # event_edit_page = LoadClass.load_page('EventEditPage')
        # event_edit_page.setDriver(self.driver)
        # event_edit_page.fill_Name_input_field(text)

    # def scroll_down_to_save_button(self):
    #
    #     event_edit_page = LoadClass.load_page('EventEditPage')
    #     event_edit_page.setDriver(self.driver)
    #     event_edit_page.scroll_down_to_save_button()

    def click_save_button(self):

        self.switch_context_to_webview()

        logging.info('click Save button')
        save_button = self.driver.find_element(*self.configuration.AssetsScreen.SAVE_BUTTON)
        save_button.click()

        self.switch_context_to_native()

        # event_edit_page = LoadClass.load_page('EventEditPage')
        # event_edit_page.setDriver(self.driver)
        # event_edit_page.click_save_button()

    def open_existing_asset(self):

        self.switch_context_to_webview()

        logging.info("open first asset on the list")

        open_existing_asset = self.driver.find_element(*self.configuration.AssetsScreen.PREVIOUSLY_CREATED_ASSET)
        self.assertIsNotNone(open_existing_asset, "existing asset not found")
        open_existing_asset.click()
        sleep(1)

        self.switch_context_to_native()

    def click_edit_button(self):

        self.switch_context_to_webview()

        logging.info("click edit button")

        edit = self.driver.find_element(*self.configuration.AssetsScreen.EDIT_BUTTON)
        self.assertIsNotNone(edit, "edit button not found")
        edit.click()

        self.switch_context_to_native()

    def type_cost_per_unit(self, text):

        self.switch_context_to_webview()

        logging.info("type cost per unit")
        cost_per_unit = self.driver.find_element(*self.configuration.AssetsScreen.COST_PER_UNIT_FIELD)
        self.assertIsNotNone(cost_per_unit, "Cost per unit input field was not found")
        # cost_per_unit.click()
        cost_per_unit.send_keys(text)

        self.switch_context_to_native()

    def save_edited_asset(self):

        self.switch_context_to_webview()

        logging.info('click Save button')
        save_button = self.driver.find_element(*self.configuration.AssetsScreen.SAVE_EDITED_ASSET)
        save_button.click()

        self.switch_context_to_native()

    # def click_more_button(self):
    #
    #     self.switch_context_to_webview()
    #
    #     logging.info("click more button")
    #     click_more_button = self.driver.find_element(*self.configuration.AssetsScreen.MORE_BUTTON)
    #     self.assertIsNotNone(click_more_button, "More button not found")
    #     click_more_button.click()
    #
    #     self.switch_context_to_native()

    def click_more_button(self):

        logging.info("click more button")
        # when existing asset already have a child asset, instead "More" button there is "New" button
        self.switch_context_to_webview()

        var = 10
        while var > 0:
            logging.info("loop")
            try:
                logging.info("check if More button is present and click it")
                click_more_button = self.driver.find_element(*self.configuration.AssetsScreen.MORE_BUTTON)
                if click_more_button.is_displayed():
                    self.assertIsNotNone(click_more_button, "More button not found")
                    click_more_button.click()
                    break
                else:
                    pass
            except NoSuchElementException:
                logging.info("More button not found - clicking back arrow and choosing different existing asset")
                back_arrow = self.driver.find_element(*self.configuration.TopBar.BACK_ARROW)
                self.assertIsNotNone(back_arrow, "back arrow not found")
                back_arrow.click()  # return to assets list

                # now open nth + 1 asset
                css_selector = list('div#assetTreeView>div.ui-content>div.main>ul[data-role="listview"]>li:nth-child(1)>a')
                logging.info(css_selector)

                n = int(1)
                logging.info(n)

                n = n + 1
                logging.info(n)

                css_selector[-4] = str(n)
                logging.info(n)
                logging.info(css_selector)

                open_existing_asset = self.driver.find_element_by_css_selector(''.join(css_selector))
                # self.assertIsNotNone(open_existing_asset, "existing asset not found")
                open_existing_asset.click()

            var = var - 1

        self.switch_context_to_native()

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

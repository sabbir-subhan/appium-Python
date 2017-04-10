"""A class for methods to handle Risks Page """

from Modules.BasePage.BasePage import BasePage
import logging
from time import sleep
from appium.webdriver.common.touch_action import TouchAction


class RisksPage(BasePage):

    def create_risk_register(self):

        self.switch_context_to_webview()

        logging.info("create risk register")
        create_risk_register_button = self.driver.find_element(*self.configuration.RisksScreen.CREATE_RISK_REGISTER)
        self.assertIsNotNone(create_risk_register_button, "Create Risk Register button not found")
        create_risk_register_button.click()

        self.switch_context_to_native()

    def type_name_for_new_risk_register(self):

        self.switch_context_to_webview()

        sleep(2)
        logging.info("type Name for new risk register")
        name = self.driver.find_element(*self.configuration.RisksScreen.NAME_FOR_NEW_RISK_REGISTER)
        self.assertIsNotNone(name, "name input field was not found")
        name.click()
        name.send_keys('Appium - new risk register')

        self.switch_context_to_native()

    def create_new_context(self):

        self.switch_context_to_webview()

        logging.info("type name for new context")
        name = self.driver.find_element(*self.configuration.RisksScreen.CREATE_NEW_CONTEXT_INPUT_FIELD)
        self.assertIsNotNone(name, "input field was not found")
        name.click()
        name.send_keys('Appium - new context')

        self.switch_context_to_native()

    def click_save_button(self):

        sleep(1)
        self.switch_context_to_webview()

        logging.info("click save button")
        click_save_button = self.driver.find_element(*self.configuration.RisksScreen.SAVE_BUTTON)
        self.assertIsNotNone(click_save_button, "Save button not found")
        click_save_button.click()

        self.switch_context_to_native()
        sleep(4)

    def filter_risks_registers(self):

        self.switch_context_to_webview()

        logging.info("filter Risks Registers to find previously created Risk register")
        risks_register_search_field = self.driver.find_element(*self.configuration.RisksScreen.SEARCH_FIELD)
        risks_register_search_field.click()
        risks_register_search_field.clear()
        risks_register_search_field.send_keys("Appium")

        self.switch_context_to_native()

    def open_existing_risk_register(self):

        self.switch_context_to_webview()

        logging.info("open first risk register on the list")
        # open_existing_risk_register = self.driver.find_element(*self.configuration.RisksScreen.
        #                                                        PREVIOUSLY_CREATED_RISK_REGISTER)
        # self.assertIsNotNone(open_existing_risk_register, "open existing Risk Register")
        # open_existing_risk_register.click()
        open_existing_risk_register = self.driver.find_element(*self.configuration.RisksScreen.PREVIOUSLY_CREATED_RISK_REGISTER)
        open_existing_risk_register.click()
        # open_existing_risk_register[0].click()

        self.switch_context_to_native()

    def click_new_button(self):

        self.switch_context_to_webview()

        sleep(2)
        logging.info("click new button")
        click_new_button = self.driver.find_element(*self.configuration.RisksScreen.NEW_BUTTON)
        self.assertIsNotNone(click_new_button, "New button not found")
        click_new_button.click()

        self.switch_context_to_native()

    def click_add_new_context(self):

        self.switch_context_to_webview()

        logging.info("click add new context")
        click_add_new_context = self.driver.find_element(*self.configuration.RisksScreen.ADD_NEW_CONTEXT)
        self.assertIsNotNone(click_add_new_context, "Add new context button not found")
        click_add_new_context.click()

        self.switch_context_to_native()

    def type_name_for_new_context(self):

        self.switch_context_to_webview()

        logging.info("type Name for new context")
        name_field = self.driver.find_element(*self.configuration.RisksScreen.NAME_FOR_NEW_CONTEXT)
        self.assertIsNotNone(name_field, "name field not found")
        name_field.clear()
        name_field.click()
        name_field.send_keys("Appium new context")

        self.switch_context_to_native()

    def save_new_context(self):

        self.switch_context_to_webview()

        logging.info("click Save button")
        save = self.driver.find_element(*self.configuration.RisksScreen.SAVE_NEW_CONTEXT)
        self.assertIsNotNone(save, "name field not found")
        save.click()

        self.switch_context_to_native()

        sleep(4)

    def open_existing_context(self):

        self.switch_context_to_webview()

        logging.info("open first context on the list")
        open_existing_context = self.driver.find_element(*self.configuration.RisksScreen.PREVIOUSLY_CREATED_CONTEXT)
        open_existing_context.click()

        self.switch_context_to_native()

    def click_add_new_risk(self):

        self.switch_context_to_webview()

        logging.info("click add new context")
        click_add_new_context = self.driver.find_element(*self.configuration.RisksScreen.ADD_NEW_RISK)
        self.assertIsNotNone(click_add_new_context, "Add new context button not found")
        click_add_new_context.click()

        self.switch_context_to_native()

    def click_add_library_risk(self):

        self.switch_context_to_webview()

        logging.info("click add new context")
        click_add_new_context = self.driver.find_element(*self.configuration.RisksScreen.ADD_NEW_LIBRARY_RISK)
        self.assertIsNotNone(click_add_new_context, "Add new context button not found")
        click_add_new_context.click()

        self.switch_context_to_native()

    def click_add_new_context_in_existing_context(self):

        self.switch_context_to_webview()

        logging.info("click add new context")
        click_add_new_context = self.driver.find_element(*self.configuration.RisksScreen.ADD_NEW_CONTEXT_IN_EXISTING_CONTEXT)
        self.assertIsNotNone(click_add_new_context, "Add new context button not found")
        click_add_new_context.click()

        self.switch_context_to_native()

    def type_name_for_new_risk(self):

        self.switch_context_to_webview()

        logging.info("type Name for new Risk")
        name_field = self.driver.find_element(*self.configuration.RisksScreen.NAME_FOR_NEW_RISK)
        self.assertIsNotNone(name_field, "name field not found")
        name_field.clear()
        name_field.click()
        name_field.send_keys("Appium new risk")

        self.switch_context_to_native()

    def save_new_risk(self):

        self.switch_context_to_webview()

        logging.info("click Save button")
        save = self.driver.find_element(*self.configuration.RisksScreen.SAVE_NEW_RISK)
        self.assertIsNotNone(save, "save new risk button not found")
        save.click()

        self.switch_context_to_native()

        sleep(4)

    def click_ok_button(self):

        self.switch_context_to_webview()

        logging.info("click ok button")
        ok = self.driver.find_element(*self.configuration.RisksScreen.OK_BUTTON)
        self.assertIsNotNone(ok, "ok button not found")
        ok.click()

        self.switch_context_to_native()

    def open_existing_risk(self):

        self.switch_context_to_webview()

        logging.info("open first risk on the list")

        open_existing_risk = self.driver.find_element(*self.configuration.RisksScreen.PREVIOUSLY_CREATED_RISK)
        open_existing_risk.click()

        self.switch_context_to_native()

    def click_more_button(self):

        self.switch_context_to_webview()

        logging.info("click more button")
        click_more_button = self.driver.find_element(*self.configuration.RisksScreen.MORE_BUTTON)
        self.assertIsNotNone(click_more_button, "More button not found")
        click_more_button.click()

        self.switch_context_to_native()

    def click_add_new_control(self):

        self.switch_context_to_webview()

        logging.info("click add new control")
        click_add_new_control = self.driver.find_element(*self.configuration.RisksScreen.ADD_NEW_CONTROL)
        self.assertIsNotNone(click_add_new_control, "Add new control button not found")
        click_add_new_control.click()

        self.switch_context_to_native()

    def click_add_library_control(self):

        self.switch_context_to_webview()

        logging.info("click add library control")
        click_add_library_control = self.driver.find_element(*self.configuration.RisksScreen.ADD_LIBRARY_CONTROL)
        self.assertIsNotNone(click_add_library_control, "Add library control button not found")
        click_add_library_control.click()

        self.switch_context_to_native()

    def click_mark_as_reviewed(self):

        self.switch_context_to_webview()

        logging.info("click mark as reviewed")
        click_mark_as_reviewed = self.driver.find_element(*self.configuration.RisksScreen.MARK_AS_REVIEWED)
        self.assertIsNotNone(click_mark_as_reviewed, "Mark as reviewed button not found")
        click_mark_as_reviewed.click()

        self.switch_context_to_native()

    def click_delete_risk(self):

        self.switch_context_to_webview()

        logging.info("click delete risk")
        click_delete_risk = self.driver.find_element(*self.configuration.RisksScreen.DELETE_RISK)
        self.assertIsNotNone(click_delete_risk, "Delete risk button not found")
        click_delete_risk.click()

        self.switch_context_to_native()

    def alert_accept_delete(self):

        self.switch_context_to_webview()

        logging.info("alert accept delete")
        alert_accept_delete = self.driver.find_element(*self.configuration.RisksScreen.DELETE_ALERT)
        self.assertIsNotNone(alert_accept_delete, "Delete button on alert not found")
        alert_accept_delete.click()

        self.switch_context_to_native()

    def type_name_for_new_control(self):

        self.switch_context_to_webview()

        sleep(1)
        logging.info("type Name for new control")
        name_field = self.driver.find_element(*self.configuration.RisksScreen.NAME_FOR_NEW_CONTROL)
        self.assertIsNotNone(name_field, "name field not found")
        # name_field.clear()
        name_field.click()
        name_field.send_keys("Appium new control")

        self.switch_context_to_native()

    def click_status_selector(self):

        self.switch_context_to_webview()

        logging.info("click status selector")
        click_status_selector = self.driver.find_element(*self.configuration.RisksScreen.STATUS_SELECTOR)
        self.assertIsNotNone(click_status_selector, "status selector not found")
        click_status_selector.click()
        sleep(1)

        self.switch_context_to_native()

    def click_save_new_control(self):

        self.switch_context_to_webview()

        logging.info("click Save button")
        save = self.driver.find_element(*self.configuration.RisksScreen.SAVE_NEW_CONTROL)
        self.assertIsNotNone(save, "name field not found")
        save.click()

        self.switch_context_to_native()

        sleep(4)

    def click_view_button(self):

        self.switch_context_to_webview()

        logging.info("click View button")
        view_button = self.driver.find_element(*self.configuration.RisksScreen.VIEW_BUTTON)
        self.assertIsNotNone(view_button, "View button not found")
        view_button.click()

        self.switch_context_to_native()

    def click_view_register(self):

        self.switch_context_to_webview()

        logging.info("click View register button")
        view_button = self.driver.find_element(*self.configuration.RisksScreen.VIEW_REGISTER_BUTTON)
        self.assertIsNotNone(view_button, "View register button not found")
        view_button.click()

        self.switch_context_to_native()

    def check_if_register_view_was_opened(self):

        self.switch_context_to_webview()

        logging.info("check if register view was opened")
        register_view = self.driver.find_element(*self.configuration.RisksScreen.REGISTER_VIEW)
        self.assertIsNotNone(register_view, "Register view not found")

        self.switch_context_to_native()

    def alert_accept_review(self):

        self.switch_context_to_webview()

        logging.info("alert accept review")
        alert_accept_review = self.driver.find_element(*self.configuration.RisksScreen.REVIEW_ALERT)
        self.assertIsNotNone(alert_accept_review, "Accept review button on alert not found")
        alert_accept_review.click()

        self.switch_context_to_native()



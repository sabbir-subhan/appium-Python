"""A class for methods to handle Inbox Page """

from Modules.BasePage.BasePage import BasePage
# from Modules.load_class import LoadClass
import logging
# from time import sleep
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.ui import WebDriverWait


class InboxPage(BasePage):

    def open_first_msg_on_the_list(self):

        logging.info("open first message on the list")

        self.switch_context_to_webview()

        first_msg_on_the_list = self.driver.find_element(*self.configuration.InboxScreen.FIRST_MSG_ON_THE_LIST)
        self.assertIsNotNone(first_msg_on_the_list, "First msg on the list, not found")
        first_msg_on_the_list.click()

        self.switch_context_to_native()

    def click_forward_button(self):

        logging.info("click forward button")

        self.switch_context_to_webview()

        forward_button = self.driver.find_element(*self.configuration.InboxScreen.FORWARD_BUTTON)
        self.assertIsNotNone(forward_button, "Forward button, not found")
        forward_button.click()

        self.switch_context_to_native()

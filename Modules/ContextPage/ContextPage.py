"""A class for methods to handle Context Page """

from Modules.BasePage.BasePage import BasePage
import logging
from Modules.load_class import LoadClass


class ContextPage(BasePage):

    def open_existing_context(self):

        logging.info("open existing context")
        open_existing_context = self.driver.find_element(*self.configuration.ContextScreen.FIRST_CONTEXT_ON_THE_LIST)
        self.assertIsNotNone(open_existing_context, "open existing context")
        open_existing_context.click()

    def click_new_button(self):

        risk_page = LoadClass.load_page('RiskPage')
        risk_page.setDriver(self.driver)
        risk_page.click_new_button()


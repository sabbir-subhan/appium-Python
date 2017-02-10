from Modules.WelcomePage.WelcomePage import WelcomePage
import logging

""" Methods for IOS"""


class IOS(WelcomePage):

    def click_login_button(self):
        super().click_login_button()  # super wywoluje klase rodzica - nadrzedna
        logging.info("info from IOS")

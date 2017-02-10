""" Methods for IOS9 on Welcome Page """

from Modules.WelcomePage.IOS import IOS
import logging


class IOS9(IOS):

    def click_login_button(self):
        super().click_login_button()  # super wywoluje klase rodzica - nadrzedna
        logging.info("info from IOS9")
        self.driver.reset()  # reset app to avoid problems with locating elements
        logging.info("click in LOGIN button")
        login_button = self.driver.find_element(*self.configuration.WelcomeScreen.LOGIN_BUTTON)
        self.assertIsNotNone(login_button, "Login button not found")
        login_button.click()


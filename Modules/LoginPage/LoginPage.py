class LoginPage(BasePage):
    """A class for methods to handle Login Page"""

    def type_username(self, username):

        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).clear()
        logging.info("type username")
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).send_keys(Credentials.get_username(username))

    def type_password(self, password):

        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).clear()
        logging.info("type password")
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).send_keys(Credentials.get_password(password))

    def type_domain_address(self, domain):

        logging.info("type domain address")
        domain_textfield = self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios)
        domain_textfield.clear()
        domain_textfield.click()
        domain_textfield.clear()
        # domain_textfield.click()
        # domain_textfield.clear()
        domain_textfield.send_keys(Credentials.get_domain(domain))

    def click_submit_button(self):

        logging.info("click in Submit button")
        self.driver.find_element(*LoginScreen.SUBMIT_BUTTON_ios).click()

    def accept_terms(self):

        logging.info("check Terms and Conditions")
        try:
            accept_terms_button = self.driver.find_element(*LoginScreen.ACCEPT_BUTTON_ios)
            if accept_terms_button.is_displayed():
                self.assertIsNotNone(accept_terms_button, "accept button not found")
                logging.info("Accepting terms and conditions")
                accept_terms_button.click()
                sleep(10)
            else:
                pass
        except NoSuchElementException:
            logging.info("Terms are already accepted - Accept button is not present")

    def alert_wrong_password(self):

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element(*LoginScreen.ALERT_MSG_INVALID_ios)
            self.assertIsNotNone(alert_msg, "Alert - wrong pass msg not found")
            self.driver.find_element(*LoginScreen.OK_BUTTON_ios).click()
            logging.info("Successfully try to login using incorrect credentials - message alert is present")
        except NoSuchElementException:
            logging.info("failed - there is no alert message")
            self.fail("failed - there is no alert message")

    def alert_expired_password(self):

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element(*LoginScreen.ALERT_MSG_EXPIRED_ios)
            logging.info("Successfully try to login to account that expired 1 day ago - message alert is present")
            self.assertIsNotNone(alert_msg, "Alert - expired msg not found")
            self.driver.find_element(*LoginScreen.OK_BUTTON_ios).click()
        except NoSuchElementException:
            logging.info("failed - there is no alert message")
            self.fail("failed - there is no alert message")

    def alert_suspended_account(self):

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element(*LoginScreen.ALERT_MSG_SUSPENDED_ios)
            logging.info("Successfully try to login into suspended account - message alert is present")
            self.assertIsNotNone(alert_msg, "Alert - suspended msg not found")
            self.driver.find_element(*LoginScreen.OK_BUTTON_ios).click()
        except NoSuchElementException:
            logging.info("failed - there is no alert message")
            self.fail("failed - there is no alert message")
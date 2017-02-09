""" Methods for IOS9 on Main Page """

#from Modules.MainPage import IOS


class IOS9():

    def __init__(self):
        pass
        # MainPage.__init__(self)

    def dissmise_notification(self):
        logging.info("dismiss notifications")
        try:
            notification_msg_on_ios = self.driver.find_element(*self.configuration.LoginScreen.NOTIFICATION_ABOUT_SENDING_MESSAGES_ios)
            if notification_msg_on_ios.is_displayed():
                logging.info("click 'No' for sending notifications on iOS")
                notification_msg_on_ios = self.driver.find_element(
                    *LoginScreen.NOTIFICATION_ABOUT_SENDING_MESSAGES_ios)
                self.assertIsNotNone(notification_msg_on_ios, "Notification msg on iOS not found")
                self.driver.find_element(*LoginScreen.NO_FOR_SENDING_NOTIFICATIONS_ON_ios).click()
            else:
                pass
        except NoSuchElementException:
            logging.info("notifications alert not present")
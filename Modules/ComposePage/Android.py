"""A class for methods to handle Compose Page on Android"""

from Modules.ComposePage.ComposePage import ComposePage
import logging
from time import sleep


class Android(ComposePage):

    def type_email_message(self):

        sleep(2)
        logging.info('type email msg')
        email_text_field = self.driver.find_element(*self.configuration.ComposeScreen.EMAIL_TEXT_FIELD)
        self.assertIsNotNone(email_text_field, 'email msg field not found')
        sleep(1)
        email_text_field.click()
        sleep(1)

        logging.info("sending keys")
        self.driver.press_keycode(33)  # send letter 'E'
        self.driver.press_keycode(41)  # send letter 'M'
        self.driver.press_keycode(29)  # send letter 'A'
        self.driver.press_keycode(37)  # send letter 'I'
        self.driver.press_keycode(40)  # send letter 'L'

        # email_text_field.send_keys('Test email')
        # sleep(1)


# Test Case 5 - Send Photo -- OCAMOB-43

# before test run - send invitation email from OCA web page -
#  (Contacts - Mobile - Send Invite) to obtain Contact Identifier PIN

# open OCA app
# Press Contact Identifier. Enter contact identifier and save.


from appium import webdriver
from desired_capabilities import DesiredCapabilities
from page_android import *


class test_SetContactIdentifier_Android(unittest.TestCase):
    def setUp(self):

        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")

        # choose desired capabilities from desired_capabilities.py
        desired_capabilities = DesiredCapabilities.desired_capabilities_for_android_6

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

        self.driver.implicitly_wait(20)  # seconds

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_Set_Contact_Identifier(self):

        logging.info("starting Test Case 10: Set Contact Identifier")
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_settings_button()
        welcome_page.type_contact_identifier("test_pin")  # to change Contact Identifier PIN - edit it in credentials.py
        android_device = AndroidDevice(self.driver)
        android_device.hide_keyboard()
        welcome_page.save_button()
        welcome_page.check_if_app_was_activated()
        welcome_page.ok_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_SetContactIdentifier_Android)
    unittest.TextTestRunner(verbosity=2).run(suite)

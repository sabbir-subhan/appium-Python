# Test Case - Rich Text Fields in all Objects -- OCAMOB-69

# before running this test create in OCA web page:
# create a new Asset type that has a rich text field and a subform with a rich text field


# open OCA app
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss notifications
# check if button "EVENTS" is present


# On IM1 stable server (website) create a new Asset that has a rich text field and a subform with a rich text field.
# Add all the formatting available in rich text field to both rich text fields in the asset. Include tables and some images.
# Save the asset. Open it and view it again.
# Login to the OCA mobile app and click on Assets. Edit the asset created above.
# View the rich text fields of the asset. Add more text below the images and save the asset.
# Repeat steps 1-5 for an event.
# Repeat steps 1-5 for a report.
# Repeat steps 1-5 for a log.
# Repeat steps 1-5 for a contact group.
# Repeat steps 1-5 for a contact.


import unittest
import logging
from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
from configuration import PROJECT_ROOT


class TestRichTextFields(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        self.driver.save_screenshot(PROJECT_ROOT + "/screenshots/test_RichTextFields.png")

        self.driver.quit()

    def test_RichTextFields(self):

        logging.info("starting Test Case: Rich Text Fields")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        welcome_page = LoadClass.load_page('WelcomePage')
        welcome_page.setDriver(self.driver)
        welcome_page.click_login_button()
        login_page = LoadClass.load_page('LoginPage')
        login_page.setDriver(self.driver)
        login_page.type_domain_address('QA')
        common_page.hide_keyboard()
        login_page.click_submit_button()
        login_page.type_username('QA')
        login_page.type_password('QA')
        common_page.hide_keyboard()
        login_page.click_submit_button()
        login_page.accept_terms()
        common_page.wait_for_app_loading()
        main_page = LoadClass.load_page('MainPage')
        main_page.setDriver(self.driver)
        main_page.alert_expiring_password()
        main_page.dismiss_notifications()
        main_page.check_presence_of_events_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRichTextFields)
    unittest.TextTestRunner(verbosity=2).run(suite)

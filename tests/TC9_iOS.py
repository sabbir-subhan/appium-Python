# Test Case 9 - Quick Access buttons on OCA app -- OCAMOB-48


# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present
# Login to OCA server>Click on Settings>Mobile Quick access Buttons>Add Quick Access buttons
# Click on Activate workflow quick access
# Click on Create contact quick access link
# Click on Create Task Quick access link
# Click on Create Report Quick access link
# Click on Quick access to link
# Click on Create event ,Asset,Log quick access links


from appium import webdriver
from desired_capabilities import DesiredCapabilities
from page_ios import *


class TestCase9iOS(unittest.TestCase):
    def setUp(self):

        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")

        # choose desired capabilities from desired_capabilities.py
        desired_capabilities = DesiredCapabilities.desired_capabilities_for_iOS_iPad

        self.driver = webdriver.Remote("http://localhost:4725/wd/hub", desired_capabilities)

        self.driver.implicitly_wait(15)  # seconds

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_Quick_Access_buttons(self):

        main_page = MainPage(self.driver)
        main_page.dismiss_ios_notifications()
        main_page.logout_if_already_logged_in()
        logging.info("starting Test Case 9: Quick Access buttons on OCA app")
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.type_username('QA')
        login_page.type_password('QA')
        login_page.type_domain_address('QA')
        ios_device = iOSdevice(self.driver)
        ios_device.hide_keyboard()
        login_page.click_submit_button()
        login_page.accept_terms()
        # main_page.alert_expiring_password()
        # main_page.dismiss_ios_notifications()
        # main_page.check_presence_of_events_button()
        # main_page.click_ACTIVATE_WORKFLOW()
        # main_page.click_ACTIVATE_BUTTON_on_alert()
        # main_page.check_if_alert_WORKFLOW_ACTIVATED_is_present()
        # main_page.open_CREATE_CONTACT()
        # new_contact_page = NewContactPage(self.driver)
        # new_contact_page.type_first_name("Name for new contact test")
        # ios_device.hide_keyboard()
        # new_contact_page.save_button()
        # main_page.open_CREATE_TASK()
        # new_task_page = NewTaskPage(self.driver)
        # new_task_page.type_title("Title for new task test")
        # ios_device.hide_keyboard()
        # new_task_page.click_on_assigned()
        # new_task_page.add_contacts()
        # new_task_page.choose_users()
        # new_task_page.ok_button()
        # new_task_page.choose_start_date()
        # new_task_page.hide_date_picker()
        # new_task_page.save_button()
        # create report - waiting for Lodging agency
        main_page.open_WEBSITE_LINK()
        safari_page = SafariBrowserPage(self.driver)
        safari_page.click_back_to_oca()  # problem with this step
        main_page.open_INCIDENT()
        incident_page = EventEditPage(self.driver)
        incident_page.fill_Name_input_field("Name for new incident test")
        incident_page.save_button()
        main_page.open_CREATE_ASSETS()
        # cdn
        main_page.open_CREATE_LOG()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase9iOS)
    unittest.TextTestRunner(verbosity=2).run(suite)

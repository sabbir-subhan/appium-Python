# Test Case - Assign Tasks directly to Team -- OCAMOB-61

# before running this test:
# - create at least two "Resource structure nodes"
# - create at least two "Resource assignments"


# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present

# Click on Tasks > Create a Task > Assign to Contact
# Click on created Task > Assign to Contact group
# Assign task to resource Structure nodes
# Assign task to Resource assignment
# Click on task > Assigned to >Resource Assignment
# Click on Task>Assigned to > Resource assignment > Select multiple Resource Assignment
# Click on task > Assigned to > Resource structure node > select multiple RS nodes
# Filter by my tasks - Click on tasks > Drop down > My tasks
# Filter by all tasks - Click on tasks > All tasks
# Filter by other types - Click on Tasks > Completed tasks


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest
from configuration import PROJECT_ROOT


class TestAssignTasks(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        self.driver.save_screenshot(PROJECT_ROOT + "/screenshots/test_AssignTasks.png")

        self.driver.quit()

    def test_AssignTasks(self):

        logging.info("starting Test Case: Assign Tasks directly to Team")
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

        main_page.scroll_down_to_tasks_button()
        main_page.open_TASKS()
        tasks_page = LoadClass.load_page('TasksPage')
        tasks_page.setDriver(self.driver)
        tasks_page.create_new_task()
        tasks_page.type_title("Task for contact")
        tasks_page.click_on_assigned()
        tasks_page.add_contacts_and_groups()
        contacts_page = LoadClass.load_page('ContactsPage')
        contacts_page.setDriver(self.driver)
        contacts_page.clear_Search_field()
        contacts_page.type_username_into_search_field()
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        contacts_page.click_first_contact_on_the_list_with_checkbox()
        tasks_page.click_ok_button()
        tasks_page.click_start_date()
        tasks_page.choose_current_date()
        tasks_page.scroll_down_to_save_button()
        tasks_page.click_save_new_task()
        tasks_page.check_if_task_was_filled_correctly()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        main_page.scroll_down_to_tasks_button()
        main_page.open_TASKS()
        tasks_page.create_new_task()
        tasks_page.type_title("Task for contact group")
        tasks_page.click_on_assigned()
        tasks_page.add_contacts_and_groups()
        contacts_page.clear_Search_field()
        contacts_page.type_text_into_search_field("Contacts")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        contacts_page.click_first_contact_group_on_the_list()
        tasks_page.click_ok_button()
        tasks_page.click_start_date()
        tasks_page.choose_current_date()
        tasks_page.scroll_down_to_save_button()
        tasks_page.click_save_new_task()
        tasks_page.check_if_task_was_filled_correctly()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        main_page.scroll_down_to_tasks_button()
        main_page.open_TASKS()
        tasks_page.create_new_task()
        tasks_page.type_title("Task for resource structure node")
        tasks_page.click_on_assigned()
        tasks_page.add_resource_structure_nodes()
        tasks_page.click_first_resource_structure_node_on_the_list()
        tasks_page.click_ok_button()
        tasks_page.click_start_date()
        tasks_page.choose_current_date()
        tasks_page.scroll_down_to_save_button()
        tasks_page.click_save_new_task()
        tasks_page.check_if_task_was_filled_correctly()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        main_page.scroll_down_to_tasks_button()
        main_page.open_TASKS()
        tasks_page.create_new_task()
        tasks_page.type_title("Task for resource assignment")
        tasks_page.click_on_assigned()
        tasks_page.add_resource_assignments()
        tasks_page.click_first_resource_assignment_on_the_list()
        tasks_page.click_ok_button()
        tasks_page.click_start_date()
        tasks_page.choose_current_date()
        tasks_page.scroll_down_to_save_button()
        tasks_page.click_save_new_task()
        tasks_page.check_if_task_was_filled_correctly()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        main_page.scroll_down_to_tasks_button()
        main_page.open_TASKS()
        tasks_page.create_new_task()
        tasks_page.type_title("Task for multiple resource assignments")
        tasks_page.click_on_assigned()
        tasks_page.add_resource_assignments()
        tasks_page.click_first_resource_assignment_on_the_list()
        tasks_page.click_second_resource_assignment_on_the_list()
        tasks_page.click_last_resource_assignment_on_the_list()
        tasks_page.click_ok_button()
        tasks_page.click_start_date()
        tasks_page.choose_current_date()
        tasks_page.scroll_down_to_save_button()
        tasks_page.click_save_new_task()
        tasks_page.check_if_task_was_filled_correctly()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        main_page.scroll_down_to_tasks_button()
        main_page.open_TASKS()
        tasks_page.create_new_task()
        tasks_page.type_title("Task for multiple resource structure nodes")
        tasks_page.click_on_assigned()
        tasks_page.add_resource_structure_nodes()
        tasks_page.click_first_resource_structure_node_on_the_list()
        tasks_page.click_second_resource_structure_node_on_the_list()
        tasks_page.click_last_resource_structure_node_on_the_list()
        tasks_page.click_ok_button()
        tasks_page.click_start_date()
        tasks_page.choose_current_date()
        tasks_page.scroll_down_to_save_button()
        tasks_page.click_save_new_task()
        tasks_page.check_if_task_was_filled_correctly()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        main_page.scroll_down_to_tasks_button()
        main_page.open_TASKS()
        tasks_page.clear_Search_field()
        common_page.hide_keyboard()
        tasks_page.filter_tasks_to_my_tasks()
        common_page.take_screenshot("Tasks_my_tasks")
        tasks_page.filter_tasks_to_all_tasks()
        common_page.take_screenshot("Tasks_all_tasks")
        tasks_page.filter_tasks_to_completed_tasks()
        common_page.take_screenshot("Tasks_completed_tasks")
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignTasks)
    unittest.TextTestRunner(verbosity=2).run(suite)

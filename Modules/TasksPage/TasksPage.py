"""A class for methods to handle Tasks Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass
from selenium.common.exceptions import *
import logging
from time import sleep
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction


class TasksPage(BasePage):

    def type_title(self, text):

        self.switch_context_to_webview()

        logging.info("type title")
        title = self.driver.find_element(*self.configuration.TasksScreen.TITLE)
        self.assertIsNotNone(title, "Title input field not found")
        title.click()
        title.send_keys(text)

        self.switch_context_to_native()

    def click_on_assigned(self):

        logging.info("click on Assigned field")
        assigned = self.driver.find_element(*self.configuration.TasksScreen.ASSIGNED)
        self.assertIsNotNone(assigned, "Assigned field not found")
        assigned.click()

    def add_contacts_and_groups(self):

        logging.info("Add Contacts and Groups")
        add_contacts_and_groups = self.driver.find_element(*self.configuration.TasksScreen.ADD_CONTACTS_AND_GROUPS)
        self.assertIsNotNone(add_contacts_and_groups, "Add Contacts and Groups button not found")
        add_contacts_and_groups.click()

    def choose_users(self):

        logging.info("Choose Users")
        choose_users = self.driver.find_element(*self.configuration.TasksScreen.CHOOSE_USERS)
        self.assertIsNotNone(choose_users, "Users option list not found")
        choose_users.click()

    def choose_contacts(self):

        logging.info("Choose Contacts")
        choose_contacts = self.driver.find_element(*self.configuration.TasksScreen.CHOOSE_CONTACTS)
        self.assertIsNotNone(choose_contacts, "Contacts option list not found")
        choose_contacts.click()

    def add_resource_structure_nodes(self):

        logging.info("Add Resource Structure Nodes")
        add_resource_structure_nodes = self.driver.find_element(*self.configuration.TasksScreen.ADD_RESOURCE_STRUCTURE_NODES)
        self.assertIsNotNone(add_resource_structure_nodes, "Add Resource Structure Nodes button not found")
        add_resource_structure_nodes.click()

    def click_first_resource_structure_node_on_the_list(self):

        self.switch_context_to_webview()

        logging.info("Choose first structure node on the list")
        click_first_resource_structure_node_on_the_list = self.driver.find_element(*self.configuration.TasksScreen.FIRST_STRUCTURE_NODE_ON_THE_LIST)  # first - child
        self.assertIsNotNone(click_first_resource_structure_node_on_the_list, "Structure node not found")
        click_first_resource_structure_node_on_the_list.click()

        self.switch_context_to_native()

    def click_second_resource_structure_node_on_the_list(self):

        self.switch_context_to_webview()

        logging.info("Choose second structure node on the list")
        click_second_resource_structure_node_on_the_list = self.driver.find_element(*self.configuration.TasksScreen.SECOND_STRUCTURE_NODE_ON_THE_LIST)  # second - child
        self.assertIsNotNone(click_second_resource_structure_node_on_the_list, "Structure node not found")
        click_second_resource_structure_node_on_the_list.click()

        self.switch_context_to_native()

    def click_last_resource_structure_node_on_the_list(self):

        self.switch_context_to_webview()

        logging.info("Choose last structure node on the list")
        click_last_resource_structure_node_on_the_list = self.driver.find_element(*self.configuration.TasksScreen.LAST_STRUCTURE_NODE_ON_THE_LIST)  # last- child
        self.assertIsNotNone(click_last_resource_structure_node_on_the_list, "Structure node not found")
        click_last_resource_structure_node_on_the_list.click()

        self.switch_context_to_native()

    def add_resource_assignments(self):

        logging.info("Add Resource Assignments")
        add_resource_assignments = self.driver.find_element(*self.configuration.TasksScreen.ADD_RESOURCE_ASSIGNMENTS)
        self.assertIsNotNone(add_resource_assignments, "Add Resource Assignments button not found")
        add_resource_assignments.click()

    def click_first_resource_assignment_on_the_list(self):

        self.switch_context_to_webview()

        logging.info("Choose first resource assignment on the list")
        click_first_resource_assignment_on_the_list = self.driver.find_element(*self.configuration.TasksScreen.FIRST_RESOURCE_ASSIGNMENT_ON_THE_LIST)  # first - child
        self.assertIsNotNone(click_first_resource_assignment_on_the_list, "Resource assignment not found")
        try:
            click_first_resource_assignment_on_the_list.click()
        except WebDriverException:
            pass
            # self.switch_context_to_native()
            # action = TouchAction(self.driver)
            # action.tap(click_first_resource_assignment_on_the_list, count=1).perform()

        self.switch_context_to_native()

    def click_second_resource_assignment_on_the_list(self):

        self.switch_context_to_webview()

        logging.info("Choose second resource assignment on the list")
        click_second_resource_assignment_on_the_list = self.driver.find_element(*self.configuration.TasksScreen.SECOND_RESOURCE_ASSIGNMENT_ON_THE_LIST)  # second - child
        self.assertIsNotNone(click_second_resource_assignment_on_the_list, "Resource assignment not found")
        click_second_resource_assignment_on_the_list.click()

        self.switch_context_to_native()

    def click_last_resource_assignment_on_the_list(self):

        self.switch_context_to_webview()

        logging.info("Choose last resource assignment on the list")
        click_last_resource_assignment_on_the_list = self.driver.find_element(*self.configuration.TasksScreen.LAST_RESOURCE_ASSIGNMENT_ON_THE_LIST)  # last- child
        self.assertIsNotNone(click_last_resource_assignment_on_the_list, "Resource assignment not found")
        click_last_resource_assignment_on_the_list.click()

        self.switch_context_to_native()

    def click_start_date(self):  # Android is using other method

        logging.info("Choose Start Date")
        sleep(2)
        start_date = self.driver.find_element(*self.configuration.TasksScreen.START_DATE)
        self.assertIsNotNone(start_date, "Start Date field not found")
        start_date.click()

    def click_ok_button(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.click_ok_button()

    def scroll_down_to_save_button(self):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.scroll_down_to_save_button()

    def click_save_new_task(self):

        self.switch_context_to_webview()

        logging.info('click Save button')
        save_button = self.driver.find_element(*self.configuration.TasksScreen.SAVE_NEW_TASK_BUTTON)
        self.assertIsNotNone(save_button, "save button not found")
        save_button.click()

        self.switch_context_to_native()

    def click_save_edited_task(self):

        self.switch_context_to_webview()

        logging.info('click Save button')
        save_button = self.driver.find_element(*self.configuration.TasksScreen.SAVE_EDITED_TASK_BUTTON)
        self.assertIsNotNone(save_button, "save button not found")
        save_button.click()

        self.switch_context_to_native()

    def type_text_into_search_field(self, text):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.type_text_into_search_field(text)

        # logging.info("filter list by search field")
        #
        # search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        # self.assertIsNotNone(search_field, "Search field not found")
        # search_field.click()
        # sleep(2)
        # search_field.send_keys(text)
        # sleep(1)

    # def open_existing_task(self):
    #
    #     self.switch_context_to_webview()
    #
    #     logging.info('edit created report approval task')
    #     edit_created_task = self.driver.find_element(*self.configuration.TasksScreen.FIRST_TASK_ON_THE_LIST)
    #     self.assertIsNotNone(edit_created_task, 'previously created task, not found')
    #     edit_created_task.click()
    #     sleep(2)
    #
    #     self.switch_context_to_native()

    def click_button_yes_for_action_required(self):

        self.switch_context_to_webview()

        logging.info('click yes button in Action Required section')
        click_button_yes_for_action_requred = self.driver.find_element(*self.configuration.TasksScreen.YES_BUTTON_FOR_ACTION_REQUIRED)
        self.assertIsNotNone(click_button_yes_for_action_requred, "button yes for action requred not found")
        click_button_yes_for_action_requred.click()

        self.switch_context_to_native()

    def alert_confirm_action_required(self):

        self.switch_context_to_webview()

        logging.info('click yes in alert to confirm action required')
        alert_confirm_action_required = self.driver.find_element(*self.configuration.TasksScreen.ALERT_CONFIRM_ACTION_REQUIRED)
        self.assertIsNotNone(alert_confirm_action_required, "alert confirm action required not found")
        alert_confirm_action_required.click()

        self.switch_context_to_native()

    def filter_tasks_to_my_tasks(self):

        self.switch_context_to_webview()

        logging.info("filter tasks to my tasks")

        expand_filters = self.driver.find_element(*self.configuration.TasksScreen.FILTERS)
        self.assertIsNotNone(expand_filters, "filters not found")
        expand_filters.click()

        self.switch_context_to_native()

        choose_my_tasks = self.driver.find_element(*self.configuration.TasksScreen.MY_TASKS)
        self.assertIsNotNone(choose_my_tasks, "my tasks filter not found")
        choose_my_tasks.click()
        sleep(1)

    def filter_tasks_to_all_tasks(self):

        self.switch_context_to_webview()

        logging.info("filter tasks to all tasks")

        expand_filters = self.driver.find_element(*self.configuration.TasksScreen.FILTERS)
        self.assertIsNotNone(expand_filters, "filters not found")
        expand_filters.click()

        self.switch_context_to_native()

        choose_all_tasks = self.driver.find_element(*self.configuration.TasksScreen.ALL_TASKS)
        self.assertIsNotNone(choose_all_tasks, "all tasks filter not found")
        choose_all_tasks.click()
        sleep(1)

    def filter_tasks_to_completed_tasks(self):

        self.switch_context_to_webview()

        logging.info("filter tasks to completed tasks")

        expand_filters = self.driver.find_element(*self.configuration.TasksScreen.FILTERS)
        self.assertIsNotNone(expand_filters, "filters not found")
        expand_filters.click()

        self.switch_context_to_native()

        completed_tasks = self.driver.find_element(*self.configuration.TasksScreen.COMPLETED_TASKS)
        self.assertIsNotNone(completed_tasks, "completed tasks filter not found")
        completed_tasks.click()
        sleep(1)

    def filter_tasks_to_incomplete_tasks(self):

        self.switch_context_to_webview()

        logging.info("filter tasks to incomplete tasks")

        expand_filters = self.driver.find_element(*self.configuration.TasksScreen.FILTERS)
        self.assertIsNotNone(expand_filters, "filters not found")
        expand_filters.click()

        self.switch_context_to_native()

        incomplete_tasks = self.driver.find_element(*self.configuration.TasksScreen.INCOMPLETE_TASKS)
        self.assertIsNotNone(incomplete_tasks, "incomplete tasks filter not found")
        incomplete_tasks.click()
        sleep(1)

    def filter_tasks_to_required_action(self):

        self.switch_context_to_webview()

        logging.info("filter tasks to action required tasks")

        expand_filters = self.driver.find_element(*self.configuration.TasksScreen.FILTERS)
        self.assertIsNotNone(expand_filters, "filters not found")
        expand_filters.click()

        self.switch_context_to_native()
        sleep(1)
        choose_action_required_tasks = self.driver.find_element(*self.configuration.TasksScreen.ACTION_REQUIRED_TASKS)
        self.assertIsNotNone(choose_action_required_tasks, "action required tasks filter not found")
        choose_action_required_tasks.click()
        sleep(1)

    def clear_Search_field(self):

        self.switch_context_to_webview()

        try:
            clear_search_field_button = self.driver.find_element(*self.configuration.TasksScreen.CLEAR_SEARCH_FIELD_BUTTON)
            if clear_search_field_button.is_displayed():
                logging.info("clear Search field by clicking clear button")
                self.assertIsNotNone(clear_search_field_button, "clear search field button not found")
                clear_search_field_button.click()
                sleep(2)
        except NoSuchElementException:
            pass

        self.switch_context_to_native()

    def check_if_view_on_map_button_is_present(self):

        self.switch_context_to_webview()

        logging.info("check if view on map button is present")
        view_on_map_button = self.driver.find_element(*self.configuration.TasksScreen.VIEW_ON_MAP_BUTTON)
        self.assertIsNotNone(view_on_map_button, "view on map button not found")

        self.switch_context_to_native()

    def create_new_task(self):

        self.switch_context_to_webview()

        logging.info("click Create new task button")
        create_new_task = self.driver.find_element(*self.configuration.TasksScreen.CREATE_NEW_TASK_BUTTON)
        self.assertIsNotNone(create_new_task, "create new task button not found")
        create_new_task.click()

        self.switch_context_to_native()

    def click_first_task_on_the_list(self):

        self.switch_context_to_webview()

        logging.info('click first task on the list')
        first_task_on_the_list = self.driver.find_element(*self.configuration.TasksScreen.FIRST_TASK_ON_THE_LIST)  # first-child
        self.assertIsNotNone(first_task_on_the_list, 'first task on the list, not found')
        first_task_on_the_list.click()

        self.switch_context_to_native()
        sleep(2)

    def edit_task(self):

        self.switch_context_to_webview()

        logging.info("click on edit button after opening existing task")
        edit_button = self.driver.find_element(*self.configuration.TasksScreen.EDIT_BUTTON)
        self.assertIsNotNone(edit_button, "edit button not found")
        edit_button.click()

        self.switch_context_to_native()

    def check_if_task_was_filled_correctly(self):

        self.switch_context_to_webview()

        logging.info("check if task form was filled correctly - Validation error is not present")
        WebDriverWait(self.driver, 1).until(
            expected_conditions.invisibility_of_element_located(self.configuration.TasksScreen.VALIDATION_ERROR_POPUP),
            "Validation Error popup is present - form was not filled correctly")

        # validation_error_popup = self.driver.find_element(*self.configuration.TasksScreen.VALIDATION_ERROR_POPUP)
        # self.assertIsNone(validation_error_popup, "Validation Error popup is present")

        self.switch_context_to_native()

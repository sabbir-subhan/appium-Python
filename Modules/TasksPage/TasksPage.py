"""A class for methods to handle Tasks Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass
from selenium.common.exceptions import *
import logging
from time import sleep


class TasksPage(BasePage):

    def type_title(self, text):

        self.switch_context_to_webview()

        logging.info("type title")
        title = self.driver.find_element(*self.configuration.TasksScreen.TITLE)
        self.assertIsNotNone(title, "Title input field was not found")
        title.click()
        title.send_keys(text)

        self.switch_context_to_native()

        # try:
        #     title = self.driver.find_element(*self.configuration.TasksScreen.TITLE)
        # except NoSuchElementException:
        #     title = self.driver.find_element(*self.configuration.TasksScreen.TITLE2)
        # self.assertIsNotNone(title, "Title input field was not found")
        # title.click()
        # title.send_keys(text)

    def click_on_assigned(self):

        logging.info("click on Assigned field")
        assigned = self.driver.find_element(*self.configuration.TasksScreen.ASSIGNED)
        self.assertIsNotNone(assigned, "Assigned field was not found")
        assigned.click()

    def add_contacts(self):

        logging.info("Add Assignees")
        assignees = self.driver.find_element(*self.configuration.TasksScreen.ADD_CONTACTS_AND_GROUPS)
        self.assertIsNotNone(assignees, "Assignees field was not found")
        assignees.click()

    def choose_users(self):

        logging.info("Choose Users")
        assignees = self.driver.find_element(*self.configuration.TasksScreen.CHOOSE_USERS)
        self.assertIsNotNone(assignees, "Users option list was not found")
        assignees.click()

    def click_start_date(self):

        logging.info("Choose Start Date")
        try:
            start_date = self.driver.find_element(*self.configuration.TasksScreen.START_DATE)
        except NoSuchElementException:
            start_date = self.driver.find_element(*self.configuration.TasksScreen.START_DATE2)
        self.assertIsNotNone(start_date, "Start Date field was not found")
        start_date.click()

    def click_ok_button(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.click_ok_button()

    def scroll_down_to_save_button(self):

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.scroll_down_to_save_button()

    def click_save_button(self):

        self.switch_context_to_webview()

        logging.info('click Save button')
        save_button = self.driver.find_element(*self.configuration.TasksScreen.SAVE_BUTTON)
        save_button.click()

        self.switch_context_to_native()

        # event_edit_page = LoadClass.load_page('EventEditPage')
        # event_edit_page.setDriver(self.driver)
        # event_edit_page.click_save_button()

    def clear_Search_field(self):

        logging.info("clear search field")
        sleep(1)
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).click()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()  # each clear is clearing one character
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        sleep(1)

    def type_text_into_search_field(self, text):

        logging.info("filter reports by search field")

        search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        self.assertIsNotNone(search_field, "Search field not found")
        search_field.click()
        sleep(2)
        search_field.send_keys(text)
        sleep(1)

    def edit_created_task_with_approval(self):

        self.switch_context_to_webview()

        logging.info('edit created report approval task')
        edit_created_task = self.driver.find_element(*self.configuration.TasksScreen.FIRST_TASK_ON_THE_LIST)
        self.assertIsNotNone(edit_created_task, 'previously created task, not found')
        edit_created_task.click()
        sleep(2)

        self.switch_context_to_native()

        # logging.info('edit created report approval task')
        # sleep(2)
        # edit_created_task = self.driver.find_elements(*self.configuration.TasksScreen.CREATED_TASK_WITH_APPROVAL)
        # self.assertIsNotNone(edit_created_task, 'created task with approval, not found')
        # edit_created_task[0].click()
        # sleep(2)

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

    def filter_tasks_to_all_tasks(self):

        self.switch_context_to_webview()

        logging.info("filter tasks to all tasks")

        expand_filters = self.driver.find_element(*self.configuration.TasksScreen.FILTERS)
        self.assertIsNotNone(expand_filters, "filters not found")
        expand_filters.click()

        choose_all_tasks = self.driver.find_element(*self.configuration.TasksScreen.ALL_TASKS)
        self.assertIsNotNone(choose_all_tasks, "all tasks filter not found")
        choose_all_tasks.click()
        sleep(1)

        self.switch_context_to_native()

    def filter_tasks_to_required_action(self):

        self.switch_context_to_webview()

        logging.info("filter tasks to action required tasks")

        expand_filters = self.driver.find_element(*self.configuration.TasksScreen.FILTERS)
        self.assertIsNotNone(expand_filters, "filters not found")
        expand_filters.click()

        choose_action_required_tasks = self.driver.find_element(*self.configuration.TasksScreen.ACTION_REQUIRED_TASKS)
        self.assertIsNotNone(choose_action_required_tasks, "action required tasks filter not found")
        choose_action_required_tasks.click()
        sleep(1)

        self.switch_context_to_native()

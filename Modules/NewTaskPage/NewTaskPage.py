"""A class for methods to handle New Task Page """

from Modules.BasePage.BasePage import BasePage
import logging


class NewTaskPage(BasePage):

    def type_title(self, text):

        logging.info("type title")
        title = self.driver.find_element(*self.configuration.NewTaskScreen.TITLE)
        self.assertIsNotNone(title, "Title input field was not found")
        title.click()
        title.send_keys(text)

    def click_on_assigned(self):

        logging.info("click on Assigned field")
        assigned = self.driver.find_element(*self.configuration.NewTaskScreen.ASSIGNED)
        self.assertIsNotNone(assigned, "Assigned field was not found")
        assigned.click()

    def add_contacts(self):

        logging.info("Add Assignees")
        assignees = self.driver.find_element(*self.configuration.NewTaskScreen.ADD_CONTACTS_AND_GROUPS)
        self.assertIsNotNone(assignees, "Assignees field was not found")
        assignees.click()

    def choose_users(self):

        logging.info("Choose Users")
        assignees = self.driver.find_element(*self.configuration.NewTaskScreen.CHOOSE_USERS)
        self.assertIsNotNone(assignees, "Users option list was not found")
        assignees.click()

    def choose_start_date(self):

        logging.info("Choose Start Date")
        start_date = self.driver.find_element(*self.configuration.NewTaskScreen.START_DATE)
        self.assertIsNotNone(start_date, "Start Date field was not found")
        start_date.click()

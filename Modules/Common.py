from Modules.BasePage import BasePage


class Common(BasePage):
    """A class for methods to handle Common buttons from different screens"""

    # OCA top bar
    def hamburger_button(self):
        # add coordinates for iPhones - clicking is not working because button is invisible
        logging.info("click hamburger button to go back to main menu")
        try:
            hamburger_button = self.driver.find_element(*TopBar.HAMBURGER_FOR_MAIN_MENU_ios)
            if hamburger_button.is_displayed():
                self.assertIsNotNone(hamburger_button, "Hamburger button is not present")
                hamburger_button.click()
        except NoSuchElementException:
            positions_for_hamburger_button = [(730, 20)]
            sleep(1)
            self.driver.tap(positions_for_hamburger_button)

    def click_save_button(self):

        logging.info("click Save button")
        save_button = self.driver.find_element(*CommonScreen.SAVE_BUTTON_ios)
        self.assertIsNotNone(save_button, "Save button not found")
        save_button.click()
        sleep(10)

    def click_cancel_button(self):
        logging.info("click on Cancel button")
        cancel_button = self.driver.find_element(*CommonScreen.CANCEL_BUTTON_ios)
        self.assertIsNotNone(cancel_button, "Cancel button not found")
        cancel_button.click()

    def click_ok_button(self):
        logging.info("click on 'Ok' button")
        ok_button = self.driver.find_element(*CommonScreen.OK_BUTTON_ios)
        self.assertIsNotNone(ok_button, "Ok button not found")
        ok_button.click()

    def fill_Name_input_field(self, text):

        logging.info("fill Name input field")
        try:
            name_field = self.driver.find_element(*EventEditScreen.NAME_FIELD_ios)
            if name_field.is_displayed():
                name_field.click()
                name_field.send_keys(text)
        except NoSuchElementException:
            name_field_by_index = self.driver.find_element(*EventEditScreen.NAME_FIELD_by_index_ios)
            if name_field_by_index.is_displayed():
                name_field_by_index.click()
                name_field_by_index.send_keys(text)

    def scroll_down_one_view(self):

        logging.info("scroll down one view")
        self.driver.execute_script("mobile: scroll", {"direction": "down"})

    def scroll_down_to_save_button(self):
        """Method to scroll down to bottom of the screen - to 'Save' button"""

        #if BasePage.platform_name(self) == iOS and BasePage.platform_version(self) == 10.2:

        logging.info("scroll down with loop")
        scroll = 0
        while scroll == 0:
            logging.info("check if save button is visible")
            save_button = self.driver.find_element(*CommonScreen.SAVE_BUTTON_ios)
            if save_button.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                # scroll -= 1
        # else:
        #     pass
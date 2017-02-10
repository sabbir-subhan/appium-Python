from Modules.BasePage import BasePage


class PhotoPage(BasePage):
    """A class for methods to handle Photo Page"""

    def check_if_photo_page_was_opened(self):

        photo_page_header = self.driver.find_element(*PhotoScreen.PHOTO_PAGE_HEADER_ios)
        self.assertIsNotNone(photo_page_header, "Photo page header was not found")
        logging.info("Photo page was opened")

    def type_description(self, description):

        sleep(2)
        logging.info("type text into description field")
        description_field = self.driver.find_element(*PhotoScreen.DESCRIPTION_FIELD_ios)
        self.assertIsNotNone(description_field, "Description field not found")
        description_field.click()
        description_field.send_keys(description)

    def click_gallery_button(self):

        # add coordinates for iPhones - clicking is not working because button is invisible
        logging.info("clicking in 'Gallery' button")
        try:
            action = TouchAction(self.driver)
            action.tap(element=None, x=180, y=158, count=1).perform()
        except NoSuchElementException:
            gallery_button = self.driver.find_element(*PhotoScreen.GALLERY_BUTTON_ios)
            if gallery_button.is_displayed():
                self.assertIsNotNone(gallery_button, "Gallery button not found")
                gallery_button.click()

    def click_take_new_button(self):
        # add coordinates for iPhones
        logging.info("clicking in 'Take new' button")
        try:
            action = TouchAction(self.driver)
            action.tap(element=None, x=548, y=158, count=1).perform()
            # take_new_button = self.driver.find_element(*PhotoScreen.TAKE_NEW_BUTTON_ios)
            # if take_new_button.is_displayed():
            #     self.assertIsNotNone(take_new_button, "Take new button not found")
            #     take_new_button.click()
        except NoSuchElementException:
            self.fail("could not tap 'Take new' button")

    def click_send_button(self):

        sleep(1)
        logging.info("click 'Send' button")
        send_button = self.driver.find_element(*PhotoScreen.SEND_BUTTON_ios)
        self.assertIsNotNone(send_button, "Send button not found")
        send_button.click()
        sleep(2)
        logging.info("sending file")
        WebDriverWait(self.driver, 420).until(
            expected_conditions.presence_of_element_located(MainMenuScreen.EVENTS_BUTTON_ios),
            "Failed to send file")
        logging.info("File was sent")

    def click_reset_button(self):

        logging.info("click 'Reset' button")
        reset_button = self.driver.find_element(*PhotoScreen.RESET_BUTTON_ios)
        self.assertIsNotNone(reset_button, "Reset button not found")
        reset_button.click()
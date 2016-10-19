# Test Case 3 - Managing events

import os
import unittest
from appium import webdriver
from time import sleep
import logging
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
logging.basicConfig(filename='OCAapp_TC3.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.getLogger().addHandler(logging.StreamHandler())
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.multi_action import MultiAction


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TC3(unittest.TestCase):
    def setUp(self):
        desired_capabilities = {}
        desired_capabilities["platformName"] = "Android"
        desired_capabilities["platformVersion"] = "4.4"
        desired_capabilities["deviceName"] = "QUANTUM_2_400"
        desired_capabilities["app"] = PATH("E:/repos/appium_OCA_mobile_app/testing-oca-mobile-app/com.noggin.oca.apk")
        desired_capabilities["appPackage"] = "com.noggin.oca"
        desired_capabilities["appActivity"] = "com.noggin.oca.OCApp"

        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
        self.driver.implicitly_wait(15)  # seconds

    def tearDown(self):
        logging.info("Quitting")
        self.driver.quit()

    def test_manage_Events(self):

        username = "bitnoise"
        password = "Bitn0!$e"
        domain = "https://bitnoiseqa.nogginoca.com"

        logging.info("click in LOGIN button")
        login_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "LOGIN")]]').click()

        logging.info("typing username, password and OCA domain")
        logging.info("locating input fields")
        textfield = self.driver.find_elements_by_class_name("android.widget.EditText")

        logging.info("clear input field and type username")
        textfield[0].clear()
        textfield[0].send_keys(username)

        logging.info("clear input field and type pass")
        textfield[1].clear()
        textfield[1].send_keys(password)

        logging.info("clear input field and type domain address")
        textfield[2].clear()
        textfield[2].send_keys(domain)

        logging.info("hide screen keyboard")
        self.driver.hide_keyboard()

        logging.info("click in Submit button")
        submit_button = self.driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='Submit']").click()

        logging.info("wait until app will login")
        sleep(10)

        logging.info("accept Terms if needed")
        try:
            logging.info("check and click on Accept button if needed")
            accept_button = self.driver.find_element_by_xpath('.//android.widget.Button'
                                                              '[@content-desc="Accept"]').click()
            logging.info("Accept button is present")
            sleep(10)
        except NoSuchElementException:
            logging.info("Terms are already accepted - Accept button is not present")

        logging.info("checking alert message")
        try:
            logging.info("click Ok on alert msg")
            click_ok = self.driver.find_element_by_xpath(
                './/android.view.View[@content-desc="Ok"]').click()
            sleep(3)
        except NoSuchElementException:
            logging.info("there is no alert message")

        sleep(2)
        logging.info("clicking on Events button")
        events_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "EVENTS")]]').click()

        logging.info("check if Events were opened")
        events_header = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Events"]')
        self.assertIsNotNone(events_header)

        logging.info("filtering events by Type")
        any_type_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "Any Type click to expand")]]').click()
        incident_type = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Incident"]').click()
        any_type_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "Incident click to expand")]]').click()
        any_type = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Any Type"]').click()

        logging.info("filtering events by Status")
        any_status_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "Any Status click to expand")]]').click()
        active_status = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Active"]').click()
        active_status_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "Active click to expand")]]').click()
        inactive_status = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Inactive"]').click()
        inactive_status_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "Inactive click to expand")]]').click()
        draft_status = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Draft"]').click()
        draft_status_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "Draft click to expand")]]').click()
        any_status = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Any Status"]').click()

        logging.info("clicking on 'More' button")
        more_button = self.driver.find_element_by_xpath(
            './/android.widget.Spinner[@content-desc[contains(., "More")]]').click()

        logging.info("clicking on New event button")
        new_event_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "New event")]]').click()

        logging.info("input Name")
        # name_field = self.driver.find_element_by_xpath(".//android.widget.EditText[@content-desc='Name']")\
        name_field = self.driver.find_element_by_xpath(".//android.widget.EditText[@index='1']") \
            .send_keys("Test Appium")
        self.driver.hide_keyboard()

        logging.info("click on severity level field")
        severity_level_field = self.driver.find_element_by_xpath(
            ".//android.widget.ListView[@index='0']"
            "//android.view.View[@index='3']"
            "//android.widget.Spinner[@index='2']").click()

        logging.info("choose_severity_lvl")
        choose_severity_lvl = self.driver.find_element_by_name("Severity 1").click()

        logging.info("click on finished_field")
        finished_field = self.driver.find_element_by_xpath(
            ".//android.view.View[@content-desc='Finished']").click()

        logging.info("choose time and date")
        time_date = self.driver.find_element_by_xpath(
            ".//android.widget.ImageButton[@content-desc='Increase year']").click()
        click_on_set = self.driver.find_element_by_id("android:id/button1").click()

        logging.info("scroll down")
        elm1 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Finished"]')
        action = TouchAction(self.driver)
        action.press(elm1).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm2 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Lead agency"]')
        action = TouchAction(self.driver)
        action.press(elm2).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm3 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Impact"]')
        action = TouchAction(self.driver)
        action.press(elm3).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm4 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Cause"]')
        action = TouchAction(self.driver)
        action.press(elm4).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm5 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Situation"]')
        action = TouchAction(self.driver)
        action.press(elm5).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm6 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Issues"]')
        action = TouchAction(self.driver)
        action.press(elm6).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm7 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Objectives"]')
        action = TouchAction(self.driver)
        action.press(elm7).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm8 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Strategies"]')
        action = TouchAction(self.driver)
        action.press(elm8).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm9 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Tactics"]')
        action = TouchAction(self.driver)
        action.press(elm9).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm10 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Communications"]')
        action = TouchAction(self.driver)
        action.press(elm10).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm11 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Related"]')
        action = TouchAction(self.driver)
        action.press(elm11).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)

        logging.info("Save event")
        save_button = self.driver.find_element_by_xpath(".//android.widget.Button[@content-desc='Save']").click()

        logging.info("open created event")
        created_event = self.driver.find_element_by_xpath(
            ".//android.view.View[@content-desc[contains(., 'Test Appium')]]").click()

        logging.info("edit previously created event")
        button_edit = self.driver.find_element_by_xpath(".//android.widget.Button[@content-desc='Edit']").click()
        sleep(3)

        logging.info("scroll down to Description field")
        elm1 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Finished"]')
        action = TouchAction(self.driver)
        action.press(elm1).perform()
        action.move_to(x=0, y=100).perform()
        sleep(2)
        elm2 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Lead agency"]')
        action = TouchAction(self.driver)
        action.press(elm2).perform()
        action.move_to(x=0, y=100).perform()
        sleep(3)

        logging.info("type some text into description field")
        description_field = self.driver.find_element_by_xpath(
            ".//android.widget.ListView[@index='0']"
            "//android.view.View[@index='8']"
            "//android.view.View[@index='1']"
            "//android.view.View[@index='1']"
            "//android.view.View[@index='0']"
            "//android.view.View[@index='0']").send_keys("test")
        self.driver.hide_keyboard()

        logging.info("scroll down to Save button")
        elm1 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Description"]')
        action = TouchAction(self.driver)
        action.press(elm1).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm2 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Impact"]')
        action = TouchAction(self.driver)
        action.press(elm2).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm3 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Cause"]')
        action = TouchAction(self.driver)
        action.press(elm3).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm4 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Situation"]')
        action = TouchAction(self.driver)
        action.press(elm4).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm5 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Issues"]')
        action = TouchAction(self.driver)
        action.press(elm5).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm6 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Objectives"]')
        action = TouchAction(self.driver)
        action.press(elm6).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm7 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Strategies"]')
        action = TouchAction(self.driver)
        action.press(elm7).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm8 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Tactics"]')
        action = TouchAction(self.driver)
        action.press(elm8).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm9 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Communications"]')
        action = TouchAction(self.driver)
        action.press(elm9).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm10 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Related"]')
        action = TouchAction(self.driver)
        action.press(elm10).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)

        logging.info("Save event")
        save_button = self.driver.find_element_by_xpath(".//android.widget.Button[@content-desc='Save']").click()

        logging.info("clicking on 'More' button")
        more_button = self.driver.find_element_by_xpath(
            ".//android.view.View[@index='1']"
            "//android.view.View[@index='0']"
            "//android.widget.ListView[@index='0']"
            "//android.view.View[@index='1']"
            "//android.widget.Spinner[@index='0']").click()
            #"//android.widget.Spinner[@content-desc[contains(., 'More')]]").click()

        logging.info("clicking on 'Delete event' button")
        delete_button = self.driver.find_element_by_xpath(
            "//android.widget.ListView[@index='2']"
            "//android.view.View[@index='2']"
            "//android.view.View[@content-desc[contains(., 'Delete event')]]").click()

        logging.info("confirm delete")
        delete_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Delete"]').click()
        self.assertTrue(True)
        sleep(5)
            # moze tu druga definicja i jao test2
        logging.info("create second event")
        logging.info("clicking on 'More' button")
        more_button = self.driver.find_element_by_xpath(
            './/android.widget.Spinner[@content-desc[contains(., "More")]]').click()

        logging.info("clicking on New event button")
        new_event_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "New event")]]').click()

        logging.info("input Name")
        name_field = self.driver.find_element_by_xpath(".//android.widget.EditText[@index='1']")\
            .send_keys("Test Appium - second event")
        self.driver.hide_keyboard()

        logging.info("click on severity level field")
        severity_level_field = self.driver.find_element_by_xpath(
            ".//android.widget.ListView[@index='0']"
            "//android.view.View[@index='3']"
            "//android.widget.Spinner[@index='2']").click()

        logging.info("choose_severity_lvl")
        choose_severity_lvl = self.driver.find_element_by_name("Severity 1").click()

        logging.info("click on finished_field")
        finished_field = self.driver.find_element_by_xpath(
            ".//android.view.View[@content-desc='Finished']").click()

        logging.info("choose time and date")
        time_date = self.driver.find_element_by_xpath(
            ".//android.widget.ImageButton[@content-desc='Increase year']").click()
        click_on_set = self.driver.find_element_by_id("android:id/button1").click()

        logging.info("scroll down")
        elm1 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Finished"]')
        action = TouchAction(self.driver)
        action.press(elm1).perform()
        action.move_to(x=0, y=100).perform()
        sleep(2)
        elm2 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Lead agency"]')
        action = TouchAction(self.driver)
        action.press(elm2).perform()
        action.move_to(x=0, y=100).perform()
        sleep(2)
        elm3 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Impact"]')
        action = TouchAction(self.driver)
        action.press(elm3).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm4 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Cause"]')
        action = TouchAction(self.driver)
        action.press(elm4).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm5 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Situation"]')
        action = TouchAction(self.driver)
        action.press(elm5).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm6 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Issues"]')
        action = TouchAction(self.driver)
        action.press(elm6).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm7 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Objectives"]')
        action = TouchAction(self.driver)
        action.press(elm7).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm8 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Strategies"]')
        action = TouchAction(self.driver)
        action.press(elm8).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm9 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Tactics"]')
        action = TouchAction(self.driver)
        action.press(elm9).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm10 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Communications"]')
        action = TouchAction(self.driver)
        action.press(elm10).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm11 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Related"]')
        action = TouchAction(self.driver)
        action.press(elm11).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)

        logging.info("Save event")
        save_button = self.driver.find_element_by_xpath(".//android.widget.Button[@content-desc='Save']").click()
        sleep(3)

        logging.info("open Event click on Edit and Create mapping data")
        created_event = self.driver.find_element_by_xpath(
            ".//android.view.View[@content-desc[contains(., 'Test Appium - second event')]]").click()

        logging.info("edit previously created event")
        button_edit = self.driver.find_element_by_xpath(".//android.widget.Button[@content-desc='Edit']").click()

        logging.info("scroll down")
        elm1 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Finished"]')
        action = TouchAction(self.driver)
        action.press(elm1).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm2 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Lead agency"]')
        action = TouchAction(self.driver)
        action.press(elm2).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm3 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Impact"]')
        action = TouchAction(self.driver)
        action.press(elm3).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm4 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Cause"]')
        action = TouchAction(self.driver)
        action.press(elm4).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm5 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Situation"]')
        action = TouchAction(self.driver)
        action.press(elm5).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm6 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Issues"]')
        action = TouchAction(self.driver)
        action.press(elm6).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm7 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Objectives"]')
        action = TouchAction(self.driver)
        action.press(elm7).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm8 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Strategies"]')
        action = TouchAction(self.driver)
        action.press(elm8).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm9 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Tactics"]')
        action = TouchAction(self.driver)
        action.press(elm9).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm10 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Communications"]')
        action = TouchAction(self.driver)
        action.press(elm10).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm11 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Related"]')
        action = TouchAction(self.driver)
        action.press(elm11).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)

        create_mapping_data_buton = self.driver.find_element_by_xpath(
            ".//android.view.View[@content-desc[contains(., 'Create mapping data')]]").click()
        logging.info("wait for map")
        sleep(10)
        logging.info("add point into the map")
        tool_buton = self.driver.find_element_by_xpath(
            ".//android.widget.Spinner[@content-desc[contains(., 'Tool')]]").click()
        poin_button = self.driver.find_element_by_xpath(
            ".//android.view.View[@content-desc[contains(., 'Point click to expand')]]").click()
        poin_default_button = self.driver.find_element_by_xpath(
            ".//android.view.View[@content-desc='Default']").click()
        add_point_on_map = self.driver.find_element_by_xpath(
            ".//android.widget.Image[@index='6']").click()
        sleep(2)
        logging.info("add line into the map")
        tool_buton = self.driver.find_element_by_xpath(
            ".//android.widget.Spinner[@content-desc[contains(., 'Tool')]]").click()
        line_button = self.driver.find_element_by_xpath(
            ".//android.view.View[@content-desc[contains(., 'Line click to expand')]]").click()
        line_default_button = self.driver.find_element_by_xpath(
            ".//android.view.View[@content-desc='Default']").click()
        add_line1 = self.driver.find_element_by_xpath(
            ".//android.widget.Image[@index='5']").click()
        add_line2 = self.driver.find_element_by_xpath(
            ".//android.widget.Image[@index='6']").click()
        sleep(2)
        logging.info("add circle into the map")
        tool_buton = self.driver.find_element_by_xpath(
            ".//android.widget.Spinner[@content-desc[contains(., 'Tool')]]").click()
        circle_button = self.driver.find_element_by_xpath(
            ".//android.view.View[@content-desc[contains(., 'Circle click to expand')]]").click()
        circle_default_button = self.driver.find_element_by_xpath(
            ".//android.view.View[@content-desc='Default']").click()
        add_circle_on_map = self.driver.find_element_by_xpath(
            ".//android.widget.Image[@index='6']").click()
        sleep(2)

        logging.info("add polygon into the map")
        tool_buton = self.driver.find_element_by_xpath(
            ".//android.widget.Spinner[@content-desc[contains(., 'Tool')]]").click()
        polygon_button = self.driver.find_element_by_xpath(
            ".//android.view.View[@content-desc[contains(., 'Polygon click to expand')]]").click()
        polygon_default_button = self.driver.find_element_by_xpath(
            ".//android.view.View[@content-desc='Default']").click()
        add_polygon1 = self.driver.find_element_by_xpath(
            ".//android.widget.Image[@index='2']").click()
        add_polygon2 = self.driver.find_element_by_xpath(
            ".//android.widget.Image[@index='5']").click()
        add_polygon3 = self.driver.find_element_by_xpath(
            ".//android.widget.Image[@index='6']").click()
        sleep(2)
        logging.info("Save map")
        save_map_button = self.driver.find_element_by_xpath(
            ".//android.widget.Button[@content-desc='Save']").click()
        sleep(2)
        logging.info("Save event")
        save_button = self.driver.find_element_by_xpath(".//android.widget.Button[@content-desc='Save']").click()
        sleep(3)

        # jakas drobna poprawka jak sie da - bo ten image z indexem 2 na mapie to robi od razu klik w zoom i cos linia
        # jakby sie nie dodala
        # now I should land on that created event and next step is clicking on more button ...

        sleep(20)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TC3)
    unittest.TextTestRunner(verbosity=2).run(suite)

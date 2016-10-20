# Test Case 3 - Managing events

import os
import unittest
from appium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.common.keys import Keys
import logging
logging.basicConfig(filename='OCAapp_TC3.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.getLogger().addHandler(logging.StreamHandler())


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
        #self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
        self.driver = webdriver.Remote("http://localhost:4444/wd/hub", desired_capabilities)
        self.driver.implicitly_wait(15)  # seconds

        # credentials

        self.username = "bitnoise"
        self.password = "Bitn0!$e"
        self.domain = "https://bitnoiseqa.nogginoca.com"

    def tearDown(self):
        logging.info("Quitting")
        self.driver.quit()

    def login(self):
        logging.info("starting def with login")
        logging.info("click in LOGIN button")
        login_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "LOGIN")]]').click()

        logging.info("typing username, password and OCA domain")
        logging.info("locating input fields")
        textfield = self.driver.find_elements_by_class_name("android.widget.EditText")

        logging.info("clear input field and type username")
        textfield[0].clear()
        textfield[0].send_keys(self.username)

        logging.info("clear input field and type pass")
        textfield[1].clear()
        textfield[1].send_keys(self.password)

        logging.info("clear input field and type domain address")
        textfield[2].clear()
        textfield[2].send_keys(self.domain)

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
            logging.info("click Ok on alert msg if needed")
            click_ok = self.driver.find_element_by_xpath(
                './/android.view.View[@content-desc="Ok"]').click()
            sleep(3)
        except NoSuchElementException:
            logging.info("there is no alert message")
        sleep(3)
        self.assertTrue(True)

    def test1(self):
        logging.info("filter events, create first Event and delete it")

        self.login()

        sleep(3)
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
        sleep(1)
        active_status_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "Active click to expand")]]').click()
        inactive_status = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Inactive"]').click()
        sleep(1)
        inactive_status_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "Inactive click to expand")]]').click()
        draft_status = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Draft"]').click()
        sleep(1)
        draft_status_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "Draft click to expand")]]').click()
        any_status = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Any Status"]').click()
        sleep(1)

        try:
            logging.info("search field - search event named: 'search'")
            search_field = self.driver.find_element_by_xpath(
                './/android.widget.EditText[@index="3"]').send_keys("search")
            self.driver.keyevent(66)
            sleep(3)
            self.driver.hide_keyboard()
            sleep(2)
        except NoSuchElementException:
            pass

        logging.info("clicking on 'More' button")
        more_button = self.driver.find_element_by_xpath(
            './/android.widget.Spinner[@content-desc[contains(., "More")]]').click()

        logging.info("clicking on New event button")
        new_event_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "New event")]]').click()
        sleep(3)

        try:
            event_type = self.driver.find_element_by_xpath(
                ".//android.view.View[@content-desc[contains(., 'Incident')]]").click()
            logging.info("choosing Incident type of new event")
        except NoSuchElementException:
            pass

        logging.info("input Name")
        name_field = self.driver.find_element_by_xpath(".//android.widget.EditText[@index='1']") \
            .send_keys("Test Appium")
        self.driver.hide_keyboard()

        logging.info("click on severity level field")
        severity_level_field = self.driver.find_element_by_xpath(
            ".//android.widget.ListView[@index='0']"
            "//android.view.View[@index='3']"
            "//android.widget.Spinner[@index='2']").click()
        sleep(2)

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

        action.press(elm2).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm3 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Impact"]')
        action.press(elm3).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm4 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Cause"]')
        action.press(elm4).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm5 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Situation"]')
        action.press(elm5).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm6 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Issues"]')
        action.press(elm6).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm7 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Objectives"]')
        action.press(elm7).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm8 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Strategies"]')
        action.press(elm8).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm9 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Tactics"]')
        action.press(elm9).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm10 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Communications"]')
        action.press(elm10).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm11 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Related"]')
        action.press(elm11).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)

        logging.info("Save event")
        save_button = self.driver.find_element_by_xpath(".//android.widget.Button[@content-desc='Save']").click()
        sleep(10)

        logging.info("open created event")
        created_event = self.driver.find_element_by_xpath(
            ".//android.view.View[@content-desc[contains(., 'Test')]]").click()
        sleep(3)

        logging.info("edit previously created event")
        button_edit = self.driver.find_element_by_xpath(".//android.widget.Button[@content-desc='Edit']").click()
        sleep(5)

        logging.info("scroll down to Description field")
        elm1 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Finished"]')
        action.press(elm1).perform()
        action.move_to(x=0, y=100).perform()
        sleep(2)
        elm2 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Lead agency"]')
        action.press(elm2).perform()
        action.move_to(x=0, y=100).perform()
        sleep(3)

        try:
            logging.info("type some text into description field")
            description_field = self.driver.find_element_by_xpath(
                ".//android.widget.ListView[@index='0']"
                "//android.view.View[@index='8' and @content-desc[contains(., 'Description')]]"
                "//android.view.View[@index='1']"
                "//android.view.View[@index='1']"
                "//android.view.View[@index='0']"
                "//android.view.View[@index='0']"
                "//android.view.View[@clickable='true']").send_keys("test")
            sleep(2)
            self.driver.hide_keyboard()
        except NoSuchElementException:
            logging.info("text field couldn't be selected")
            pass

        logging.info("scroll down to Save button")
        elm1 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Description"]')
        action.press(elm1).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm2 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Impact"]')
        action.press(elm2).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm3 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Cause"]')
        action.press(elm3).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm4 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Situation"]')
        action.press(elm4).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm5 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Issues"]')
        action.press(elm5).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm6 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Objectives"]')
        action.press(elm6).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm7 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Strategies"]')
        action.press(elm7).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm8 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Tactics"]')
        action.press(elm8).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm9 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Communications"]')
        action.press(elm9).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm10 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Related"]')
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
            "//android.widget.Spinner[@index='0'and @content-desc[contains(., 'More')]]").click()

        sleep(1)
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

    def test2(self):
        logging.info("create second event and add map")

        self.login()

        sleep(3)
        logging.info("clicking on Events button")
        events_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "EVENTS")]]').click()

        logging.info("check if Events were opened")
        events_header = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Events"]')
        self.assertIsNotNone(events_header)

        logging.info("clicking on 'More' button")
        more_button = self.driver.find_element_by_xpath(
            './/android.widget.Spinner[@content-desc[contains(., "More")]]').click()

        logging.info("clicking on New event button")
        new_event_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "New event")]]').click()
        sleep(3)

        try:
            event_type = self.driver.find_element_by_xpath(
                ".//android.view.View[@content-desc[contains(., 'Incident')]]").click()
            logging.info("choosing Incident type of new event")
        except NoSuchElementException:
            pass

        logging.info("input Name")
        name_field = self.driver.find_element_by_xpath(".//android.widget.EditText[@index='1']")\
            .send_keys("Test Appium - second event")
        self.driver.hide_keyboard()

        logging.info("click on severity level field")
        severity_level_field = self.driver.find_element_by_xpath(
            ".//android.widget.ListView[@index='0']"
            "//android.view.View[@index='3']"
            "//android.widget.Spinner[@index='2']").click()
        sleep(1)

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
        action.press(elm2).perform()
        action.move_to(x=0, y=100).perform()
        sleep(2)
        elm3 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Impact"]')
        action.press(elm3).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm4 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Cause"]')
        action.press(elm4).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm5 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Situation"]')
        action.press(elm5).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm6 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Issues"]')
        action.press(elm6).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm7 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Objectives"]')
        action.press(elm7).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm8 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Strategies"]')
        action.press(elm8).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm9 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Tactics"]')
        action.press(elm9).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm10 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Communications"]')
        action.press(elm10).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm11 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Related"]')
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
        sleep(3)

        logging.info("scroll down")
        elm1 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Finished"]')
        action.press(elm1).perform()
        action.move_to(x=0, y=100).perform()
        sleep(2)
        elm2 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Lead agency"]')
        action.press(elm2).perform()
        action.move_to(x=0, y=100).perform()
        sleep(2)
        elm3 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Impact"]')
        action.press(elm3).perform()
        action.move_to(x=0, y=100).perform()
        sleep(2)
        elm4 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Cause"]')
        action.press(elm4).perform()
        action.move_to(x=0, y=100).perform()
        sleep(2)
        elm5 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Situation"]')
        action.press(elm5).perform()
        action.move_to(x=0, y=100).perform()
        sleep(2)
        elm6 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Issues"]')
        action.press(elm6).perform()
        action.move_to(x=0, y=100).perform()
        sleep(2)
        elm7 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Objectives"]')
        action.press(elm7).perform()
        action.move_to(x=0, y=100).perform()
        sleep(2)
        elm8 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Strategies"]')
        action.press(elm8).perform()
        action.move_to(x=0, y=100).perform()
        sleep(2)
        elm9 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Tactics"]')
        action.press(elm9).perform()
        action.move_to(x=0, y=100).perform()
        sleep(2)
        elm10 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Communications"]')
        action.press(elm10).perform()
        action.move_to(x=0, y=100).perform()
        sleep(2)
        elm11 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Related"]')
        action.press(elm11).perform()
        action.move_to(x=0, y=100).perform()
        sleep(2)

        create_mapping_data_buton = self.driver.find_element_by_xpath(
            ".//android.view.View[@content-desc[contains(., ' mapping data')]]").click()
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
        sleep(1)
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
        action.tap(add_line2).perform()
        action.tap(add_line2).perform()
        sleep(3)

        logging.info("add circle into the map")
        tool_buton = self.driver.find_element_by_xpath(
            ".//android.widget.Spinner[@content-desc[contains(., 'Tool')]]").click()
        circle_button = self.driver.find_element_by_xpath(
            ".//android.view.View[@content-desc[contains(., 'Circle click to expand')]]").click()
        circle_default_button = self.driver.find_element_by_xpath(
            ".//android.view.View[@content-desc='Default']").click()
        add_circle_on_map = self.driver.find_element_by_xpath(
            ".//android.widget.Image[@index='6']").click()
        sleep(1)

        logging.info("add polygon into the map")
        tool_buton = self.driver.find_element_by_xpath(
            ".//android.widget.Spinner[@content-desc[contains(., 'Tool')]]").click()
        polygon_button = self.driver.find_element_by_xpath(
            ".//android.view.View[@content-desc[contains(., 'Polygon click to expand')]]").click()
        polygon_default_button = self.driver.find_element_by_xpath(
            ".//android.view.View[@content-desc='Default']").click()
        add_polygon1 = self.driver.find_element_by_xpath(
            ".//android.widget.Image[@index='5']").click()
        add_polygon2 = self.driver.find_element_by_xpath(
            ".//android.widget.Image[@index='6']").click()
        add_polygon3 = self.driver.find_element_by_xpath(
            ".//android.widget.Image[@index='9']").click()
        action.tap(add_polygon3).perform()
        action.tap(add_polygon3).perform()
        sleep(3)
        # self.driver.save_screenshot("screen.png")

        logging.info("Save map")
        save_map_button = self.driver.find_element_by_xpath(
            ".//android.widget.Button[@content-desc='Save']").click()
        sleep(3)
        logging.info("Save event")
        save_button = self.driver.find_element_by_xpath(".//android.widget.Button[@content-desc='Save']").click()
        sleep(5)
        self.assertTrue(True)

        sleep(5)

    def test3(self):
        logging.info("crete sub event, set event as primary and after that clear it")

        self.login()

        sleep(3)
        logging.info("clicking on Events button")
        events_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "EVENTS")]]').click()

        logging.info("check if Events were opened")
        events_header = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Events"]')
        self.assertIsNotNone(events_header)

        # before creating sub event - normal event is necessary
        logging.info("clicking on 'More' button")
        more_button = self.driver.find_element_by_xpath(
            './/android.widget.Spinner[@content-desc[contains(., "More")]]').click()

        logging.info("clicking on New event button")
        new_event_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "New event")]]').click()
        sleep(3)

        try:
            event_type = self.driver.find_element_by_xpath(
                ".//android.view.View[@content-desc[contains(., 'Incident')]]").click()
            logging.info("choosing Incident type of new event")
        except NoSuchElementException:
            pass

        logging.info("input Name")
        name_field = self.driver.find_element_by_xpath(".//android.widget.EditText[@index='1']")\
            .send_keys("Test to create sub event")
        self.driver.hide_keyboard()

        logging.info("click on severity level field")
        severity_level_field = self.driver.find_element_by_xpath(
            ".//android.widget.ListView[@index='0']"
            "//android.view.View[@index='3']"
            "//android.widget.Spinner[@index='2']").click()
        sleep(1)

        logging.info("choose_severity_lvl")
        choose_severity_lvl = self.driver.find_element_by_name("Severity 3").click()

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
        action.press(elm2).perform()
        action.move_to(x=0, y=100).perform()
        sleep(2)
        elm3 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Impact"]')
        action.press(elm3).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm4 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Cause"]')
        action.press(elm4).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm5 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Situation"]')
        action.press(elm5).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm6 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Issues"]')
        action.press(elm6).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm7 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Objectives"]')
        action.press(elm7).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm8 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Strategies"]')
        action.press(elm8).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm9 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Tactics"]')
        action.press(elm9).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm10 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Communications"]')
        action.press(elm10).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm11 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Related"]')
        action.press(elm11).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)

        logging.info("Save event")
        save_button = self.driver.find_element_by_xpath(".//android.widget.Button[@content-desc='Save']").click()
        sleep(3)

        logging.info("open previously created event")
        created_event = self.driver.find_element_by_xpath(
            ".//android.view.View[@content-desc[contains(., 'Test to create sub event')]]").click()
        sleep(3)

        logging.info("clicking on 'More' button")
        more_button = self.driver.find_element_by_xpath(
            './/android.widget.Spinner[@content-desc[contains(., "More")]]').click()

        logging.info("clicking on 'New sub event' button")
        more_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "New sub event")]]').click()
        sleep(3)

        try:
            event_type = self.driver.find_element_by_xpath(
                ".//android.view.View[@content-desc[contains(., 'Incident')]]").click()
            logging.info("choosing Incident type of new event")
        except NoSuchElementException:
            pass

        logging.info("input Name for new sub event")
        name_field = self.driver.find_element_by_xpath(".//android.widget.EditText[@index='1']") \
            .send_keys("Test Appium - sub event")
        self.driver.hide_keyboard()

        logging.info("click on severity level field")
        severity_level_field = self.driver.find_element_by_xpath(
            ".//android.widget.ListView[@index='0']"
            "//android.view.View[@index='3']"
            "//android.widget.Spinner[@index='2']").click()
        sleep(1)

        logging.info("choose_severity_lvl")
        choose_severity_lvl = self.driver.find_element_by_name("Severity 2").click()

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

        action.press(elm2).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm3 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Impact"]')
        action.press(elm3).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm4 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Cause"]')
        action.press(elm4).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm5 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Situation"]')
        action.press(elm5).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm6 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Issues"]')
        action.press(elm6).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm7 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Objectives"]')
        action.press(elm7).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm8 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Strategies"]')
        action.press(elm8).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm9 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Tactics"]')
        action.press(elm9).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm10 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Communications"]')
        action.press(elm10).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm11 = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Related"]')
        action.press(elm11).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)

        logging.info("Save event")
        save_button = self.driver.find_element_by_xpath(".//android.widget.Button[@content-desc='Save']").click()
        sleep(5)

        logging.info("open previously created event")
        created_event = self.driver.find_element_by_xpath(
            ".//android.view.View[@content-desc[contains(., 'Test ')]]").click()
        sleep(3)

        logging.info("clicking on 'More' button")
        more_button = self.driver.find_element_by_xpath(
            './/android.widget.Spinner[@content-desc[contains(., "More")]]').click()

        logging.info("clicking on 'Set as primary' button")
        more_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "Set as primary")]]').click()
        sleep(2)

        logging.info("go back to main menu")
        arrow_back = self.driver.find_element_by_xpath(".//android.webkit.WebView[@index='0']"
                                                       "//android.view.View[@index='0']"
                                                       "//android.view.View[@index='0']").click()
        sleep(2)

        logging.info("clicking on Events button")
        events_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "EVENTS")]]').click()

        logging.info("check if Events were opened")
        events_header = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Events"]')
        self.assertIsNotNone(events_header)

        logging.info("clicking on 'More' button")
        more_button = self.driver.find_element_by_xpath(
            './/android.widget.Spinner[@content-desc[contains(., "More")]]').click()
        sleep(5)
        logging.info("clicking on 'Clear primary event' button")
        clear_primary_event_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "Clear primary event")]]').click()

        logging.info("checking notification - 'Primary event cleared'")
        notification = self.driver.find_element_by_xpath(".//android.view.View[@content-desc='Primary event cleared']")
        self.assertIsNotNone(notification)

        self.assertTrue(True)
        sleep(5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TC3)
    unittest.TextTestRunner(verbosity=2).run(suite)

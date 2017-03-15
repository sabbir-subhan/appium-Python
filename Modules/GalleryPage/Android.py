"""A class for methods to handle Gallery Page on Android"""

from Modules.GalleryPage.GalleryPage import GalleryPage
import logging
from Modules.load_class import LoadClass
from Conf.desired_capabilities import DesiredCapabilities
from appium.webdriver.common.touch_action import TouchAction
from time import sleep


class Android(GalleryPage):

    def choose_element_1(self):

        logging.info("choosing element 1 - Android")

        self.driver.find_element_by_id('com.android.documentsui:id/menu_list').click()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]').click()
        sleep(2)

        # desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        # platform_version = desired_capabilities.get('platformVersion')
        # if platform_version >= "7":
        #     choose_element_1_android7 = self.driver.find_element(*self.configuration.GalleryScreen.
        #                                                          GALLERY_ELEMENT_1_android7)
        #     # choose_element_1_android7.click()  # for some reason it is not working with Android 7
        #     location = choose_element_1_android7.location
        #     logging.info(location)
        #     x = location["x"]
        #     y = location["y"]
        #     logging.info(x)
        #     logging.info(y)
            # positions = [(x, y)]
            # action = TouchAction(self.driver)
            # action.press(el=choose_element_1_android7, x=x, y=y).release().perform()
            # action.tap(element=choose_element_1_android7, x=x, y=y, count=1).perform()
            #print(positions)
            #self.driver.tap(positions)  # not working, also Touch Action is not working in Android 7 Gallery
        #     logging.info("log after tap - to test Android 7")  # TEST
        # else:
        #     choose_element_1 = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_ELEMENT_1)
        #     choose_element_1.click()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.alert_popup_allow()
        # try:  # on Android 6 sometimes it is necessary to reopen gallery after allowing access to photos/videos
        #     photo_page = LoadClass.load_page('PhotoPage')
        #     photo_page.setDriver(self.driver)
        #     photo_page.click_gallery_button()
        #     common_page = LoadClass.load_page('CommonPage')
        #     common_page.setDriver(self.driver)
        #     common_page.alert_popup_allow()
        #     Android.choose_element_1(self)
        # except:
        #     pass

    def choose_video_from_gallery(self):

        common_page = LoadClass.load_page('GalleryPage')
        common_page.setDriver(self.driver)
        common_page.choose_element_1()


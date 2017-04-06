""" Methods for IOS9 on Photo Page """

from Modules.PhotoPage.IOS import IOS
import logging


class IOS9(IOS):

    pass

    # def click_gallery_button(self):
    #
    #     logging.info("clicking in 'Gallery' button")
    #     gallery_button = self.driver.find_element(*self.configuration.PhotoScreen.GALLERY_BUTTON)
    #     location = gallery_button.location
    #     print(location)
    #     x = location["x"]
    #     y = location["y"]
    #     print(x)
    #     print(y)
    #     positions = [(x, y)]
    #     self.driver.tap(positions)
    #
    # def click_take_new_button(self):
    #
    #     logging.info("clicking in 'Take new' button")
    #     take_new_button = self.driver.find_element(*self.configuration.PhotoScreen.TAKE_NEW_BUTTON)
    #     location = take_new_button.location
    #     print(location)
    #     x = location["x"]
    #     y = location["y"]
    #     print(x)
    #     print(y)
    #     positions = [(x, y)]
    #     self.driver.tap(positions)





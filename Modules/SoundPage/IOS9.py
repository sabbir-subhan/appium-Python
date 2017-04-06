""" Methods for IOS9 on Sound Page """

from Modules.SoundPage.IOS import IOS
import logging


class IOS9(IOS):

    pass
    # def click_record_sound_icon(self):
    #
    #     logging.info("clicking in 'Record Sound' icon")
    #     record_sound_button = self.driver.find_element(*self.configuration.SoundScreen.RECORD_SOUND_BUTTON)
    #     location = record_sound_button.location
    #     print(location)
    #     x = location["x"]
    #     y = location["y"]
    #     print(x)
    #     print(y)
    #     positions = [(x + 1, y + 1)]  # adding +1 to coordinates to avoid problem with tapping in icon
    #     print(positions)
    #     self.driver.tap(positions)




"""Script containing configurations for running tests"""

import logging
import os
from settings import Settings
from settings import SettingsPort
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DEFINITIONS_ROOT = os.path.join(PROJECT_ROOT)

platform = Settings.platform
PORT = SettingsPort.port

logging.warning("platform = " + str(platform))
logging.warning("port = " + str(PORT))

# platform = "IOS_9_emulator"  # use this for fixed values
# PORT = "4723"  # port on which Appium server is running  # use this for fixed values

# You can use:

# Android_4
# Android_4.4
# Android_4_emulator
# Android_5
# Android_5_emulator
# Android_6
# Android_6_emulator
# Android_7
# Android_7_emulator
# Android_7.1_emulator
# IOS_9_iPad
# IOS_9_emulator
# IOS_10_iPhone
# IOS_10_iPad
# IOS_10_emulator


# devices are defined in /Conf/desired_capabilities.py


if platform == "IOS_9_iPad":

    ENVIRONMENT_TEST = "IOS9"
    ENVIRONMENT_MIDDLE_CLASS = "IOS"
    PLATFORM_VERSION = ""

elif platform == "IOS_9_emulator":

    ENVIRONMENT_TEST = "IOS9"
    ENVIRONMENT_MIDDLE_CLASS = "IOS"
    PLATFORM_VERSION = ""

elif platform == "IOS_10_iPhone":

    ENVIRONMENT_TEST = "IOS10"
    ENVIRONMENT_MIDDLE_CLASS = "IOS"
    PLATFORM_VERSION = ""

elif platform == "IOS_10_iPad":

    ENVIRONMENT_TEST = "IOS10"
    ENVIRONMENT_MIDDLE_CLASS = "IOS"
    PLATFORM_VERSION = ""

elif platform == "IOS_10_emulator":

    ENVIRONMENT_TEST = "IOS10"
    ENVIRONMENT_MIDDLE_CLASS = "IOS"
    PLATFORM_VERSION = ""

elif platform == "Android_8_emulator":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "8.0"

elif platform == "Android_7":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "7.0"

elif platform == "Android_7_emulator":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "7.0"

elif platform == "Android_7.1_emulator":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "7.1"

elif platform == "Android_6":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "6.0"

elif platform == "Android_6_emulator":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "6.0"

elif platform == "Android_5":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "5.1.1"

elif platform == "Android_5_emulator":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "5.1.0"

elif platform == "Android_4.4":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "4.4.4"

elif platform == "Android_4":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "4.4.2"

elif platform == "Android_4_emulator":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "4.4.2"

else:
    print("ENVIRONMENT FOR TESTS not found")


"""Script containing configurations for running tests"""

from run3 import runner
import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DEFINITIONS_ROOT = os.path.join(PROJECT_ROOT)

platform = runner()
print("platform passed into configuration.py: " + platform)

# platform = main
# print("print platform: " + str(platform))
# platform = str(platform).replace("test=", "")
# print("po zabawie " + platform)
# platform = "IOS_10_emulator"
# platform, test = Runner.func(platform, test)
# platform = Runner.get_platform(getattr())
# x = Runner.get_platform()
# # x = Runner.get_platform()
# y = x.platform
# platform = Runner.get_platform
# platform = main.platform
# platform = main()  # method main return default platform ?
# platform = GetPlatform().get_platform()
# platform = GetPlatform.get_platform(platform="")
# platform = main.platform
# print("platform passed into configuration.py = " + main.platform)

# You can use:

# Android_4
# Android_5
# Android_5_emulator
# Android_6
# Android_6_emulator
# Android_7
# Android_7_emulator
# Android_7.1_emulator
# IOS_9
# IOS_9_emulator
# IOS_10
# IOS_10_emulator


# devices are defined in /Conf/desired_capabilities.py

PORT = "4723"  # port on which Appium server is running

if platform == "IOS_9":

    ENVIRONMENT_TEST = "IOS9"
    ENVIRONMENT_MIDDLE_CLASS = "IOS"
    PLATFORM_VERSION = ""

elif platform == "IOS_9_emulator":

    ENVIRONMENT_TEST = "IOS9"
    ENVIRONMENT_MIDDLE_CLASS = "IOS"
    PLATFORM_VERSION = ""

elif platform == "IOS_10":

    ENVIRONMENT_TEST = "IOS10"
    ENVIRONMENT_MIDDLE_CLASS = "IOS"
    PLATFORM_VERSION = ""

elif platform == "IOS_10_emulator":

    ENVIRONMENT_TEST = "IOS10"
    ENVIRONMENT_MIDDLE_CLASS = "IOS"
    PLATFORM_VERSION = ""

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

# if platform == "IOS 9":
#
#     ENVIRONMENT_TEST = "IOS9"
#     ENVIRONMENT_MIDDLE_CLASS = "IOS"
#     PLATFORM_VERSION = ""
#
# elif platform == "IOS 9 emulator":
#
#     ENVIRONMENT_TEST = "IOS9"
#     ENVIRONMENT_MIDDLE_CLASS = "IOS"
#     PLATFORM_VERSION = ""
#
# elif platform == "IOS 10":
#
#     ENVIRONMENT_TEST = "IOS10"
#     ENVIRONMENT_MIDDLE_CLASS = "IOS"
#     PLATFORM_VERSION = ""
#
# elif platform == "IOS 10 emulator":
#
#     ENVIRONMENT_TEST = "IOS10"
#     ENVIRONMENT_MIDDLE_CLASS = "IOS"
#     PLATFORM_VERSION = ""
#
# elif platform == "Android 7":
#
#     ENVIRONMENT_TEST = "Android"
#     ENVIRONMENT_MIDDLE_CLASS = None
#     PLATFORM_VERSION = "7.0"
#
# elif platform == "Android 7 emulator":
#
#     ENVIRONMENT_TEST = "Android"
#     ENVIRONMENT_MIDDLE_CLASS = None
#     PLATFORM_VERSION = "7.0"
#
# elif platform == "Android 7.1 emulator":
#
#     ENVIRONMENT_TEST = "Android"
#     ENVIRONMENT_MIDDLE_CLASS = None
#     PLATFORM_VERSION = "7.1"
#
# elif platform == "Android 6":
#
#     ENVIRONMENT_TEST = "Android"
#     ENVIRONMENT_MIDDLE_CLASS = None
#     PLATFORM_VERSION = "6.0"
#
# elif platform == "Android 6 emulator":
#
#     ENVIRONMENT_TEST = "Android"
#     ENVIRONMENT_MIDDLE_CLASS = None
#     PLATFORM_VERSION = "6.0"
#
# elif platform == "Android 5":
#
#     ENVIRONMENT_TEST = "Android"
#     ENVIRONMENT_MIDDLE_CLASS = None
#     PLATFORM_VERSION = "5.1.1"
#
# elif platform == "Android 5 emulator":
#
#     ENVIRONMENT_TEST = "Android"
#     ENVIRONMENT_MIDDLE_CLASS = None
#     PLATFORM_VERSION = "5.1.0"
#
# elif platform == "Android 4":
#
#     ENVIRONMENT_TEST = "Android"
#     ENVIRONMENT_MIDDLE_CLASS = None
#     PLATFORM_VERSION = "4.4.2"
#
# elif platform == "Android 4 emulator":
#
#     ENVIRONMENT_TEST = "Android"
#     ENVIRONMENT_MIDDLE_CLASS = None
#     PLATFORM_VERSION = "4.4.2"
#
# else:
#     print("fail to load ENVIRONMENT FOR TESTS")

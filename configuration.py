""" Choose platform to run tests """

platform = "Android 7.1 emulator"

# You can use:

# Android 4
# Android 5
# Android 5 emulator
# Android 6
# Android 6 emulator
# Android 7
# Android 7 emulator
# Android 7.1 emulator
# IOS 9
# IOS 9 emulator
# IOS 10
# IOS 10 emulator


# devices are defined in /Conf/desired_capabilities.py

PORT = "4723"  # port on which Appium server is running

if platform == "IOS 9":

    ENVIRONMENT_TEST = "IOS9"
    ENVIRONMENT_MIDDLE_CLASS = "IOS"
    PLATFORM_VERSION = ""

elif platform == "IOS 9 emulator":

    ENVIRONMENT_TEST = "IOS9"
    ENVIRONMENT_MIDDLE_CLASS = "IOS"
    PLATFORM_VERSION = ""

elif platform == "IOS 10":

    ENVIRONMENT_TEST = "IOS10"
    ENVIRONMENT_MIDDLE_CLASS = "IOS"
    PLATFORM_VERSION = ""

elif platform == "IOS 10 emulator":

    ENVIRONMENT_TEST = "IOS10"
    ENVIRONMENT_MIDDLE_CLASS = "IOS"
    PLATFORM_VERSION = ""

elif platform == "Android 7":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "7.0"

elif platform == "Android 7 emulator":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "7.0"

elif platform == "Android 7.1 emulator":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "7.1"

elif platform == "Android 6":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "6.0"

elif platform == "Android 6 emulator":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "6.0"

elif platform == "Android 5":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "5.1.1"

elif platform == "Android 5 emulator":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "5.1.0"

elif platform == "Android 4":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "4.4.2"

elif platform == "Android 4 emulator":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "4.4.2"

else:
    print("fail to load ENVIRONMENT FOR TESTS")

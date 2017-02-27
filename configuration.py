""" Choose platform to run tests """

platform = "Android 7"

# Android 4
# Android 5
# Android 6
# Android 6.0
# Android 7
# IOS 9
# IOS 10


if platform == "IOS 9":

    ENVIRONMENT_TEST = "IOS9"
    ENVIRONMENT_MIDDLE_CLASS = "IOS"
    PLATFORM_VERSION = ""

elif platform == "IOS 10":

    ENVIRONMENT_TEST = "IOS10"
    ENVIRONMENT_MIDDLE_CLASS = "IOS"
    PLATFORM_VERSION = ""

elif platform == "Android 7":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "7.0"

elif platform == "Android 6":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "6.0.1"

elif platform == "Android 6.0":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "6.0"

elif platform == "Android 5":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "5.1.1"

elif platform == "Android 4":

    ENVIRONMENT_TEST = "Android"
    ENVIRONMENT_MIDDLE_CLASS = None
    PLATFORM_VERSION = "4.4.2"

else:
    print("fail to load ENVIRONMENT FOR TESTS")



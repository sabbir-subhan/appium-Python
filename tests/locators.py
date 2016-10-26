from selenium.webdriver.common.by import By


class WelcomeScreen(object):
    """A class for welcome screen locators - first screen after lunching the app."""
    LOGIN_BUTTON = (By.XPATH, './/android.view.View[@content-desc[contains(., "LOGIN")]]')


class LoginScreen(object):
    """A class for login screen locators - screen after clicking into LOGIN."""
    TEXTFIELD_USERNAME = (By.XPATH, './/android.widget.EditText[@index="1"]')
    TEXTFIELD_PASSWORD = (By.XPATH, './/android.widget.EditText[@index="3"]')
    TEXTFIELD_DOMAIN = (By.XPATH, './/android.widget.EditText[@index="5"]')
    SUBMIT_BUTTON = (By.XPATH, '//android.widget.Button[@content-desc="Submit"]')
    ACCEPT_BUTTON = (By.XPATH, './/android.widget.Button[@content-desc="Accept"]')


class MainMenuScreen(object):
    """A class for main menu screen locators - first screen after correct login into the app."""
    LOGOUT_BUTTON = (By.XPATH, './/android.view.View[@content-desc[contains(., "LOGOUT")]]')
    BUTTONS = (By.CLASS_NAME, 'android.view.View')


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass



from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class MainPage:
    def __init__(self, browser):
        self.browser = browser

    def user_avatar(self):
        return WebDriverWait(self.browser, timeout=10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException, TimeoutException]).until(
            EC.element_to_be_clickable(Locators.USER_AVATAR)
        )

    def exit_menu(self):
        return WebDriverWait(self.browser, timeout=10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException, TimeoutException]).until(
            EC.element_to_be_clickable(Locators.EXIT_MENU)
        )
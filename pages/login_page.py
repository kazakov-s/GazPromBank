from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from constants import TEST_URL
from locators import Locators


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(TEST_URL)

    def telefon_field(self):
        return WebDriverWait(self.browser, timeout=3, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException, TimeoutException]).until(
            EC.element_to_be_clickable(Locators.TEL_FIELD)
        )

    def password_field(self):
        return WebDriverWait(self.browser, timeout=3, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException, TimeoutException]).until(
            EC.element_to_be_clickable(Locators.PASSWD_FIELD)
        )

    def login_btn1(self):
        return WebDriverWait(self.browser, 1).until(
            EC.element_to_be_clickable(Locators.LOGIN_BTN1)
        )

    def login_btn2(self):
        return WebDriverWait(self.browser, 1).until(
            EC.element_to_be_clickable(Locators.LOGIN_BTN2)
        )

    def name_field(self):
        return WebDriverWait(self.browser, timeout=3, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException, TimeoutException]).until(
            EC.element_to_be_clickable(Locators.NAME_FIELD)
        )

    def agree_box(self):
        return WebDriverWait(self.browser, 1).until(
            EC.element_to_be_clickable(Locators.AGREE_BOX)
        )

    def register_btn(self):
        return WebDriverWait(self.browser, 1).until(
            EC.element_to_be_clickable(Locators.REGISTER_BTN)
        )
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import ELEMENT_LOAD_SECONDS


def wait(self):
    return WebDriverWait(self.driver, ELEMENT_LOAD_SECONDS)


def find(self, by_locator, message):
    return self.wait().until(EC.presence_of_element_located(by_locator), message)

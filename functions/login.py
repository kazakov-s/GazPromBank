import time

from constants import MY_PHONE_NUMBER, MY_NAME, TEST_URL
from pages.login_page import LoginPage


def fill_login_form(driver):
    login_page = LoginPage(driver)
    login_page.telefon_field().send_keys(MY_PHONE_NUMBER)
    login_page.login_btn1().click()
    try:
        login_page.name_field().send_keys(MY_NAME)
        login_page.agree_box().click()
        login_page.login_btn2().click()
    except Exception:
        login_page.password_field().send_keys('Wcppos321-')
        login_page.login_btn1().click()


def wait_for_login(driver):
    while driver.current_url != TEST_URL:
        time.sleep(1)

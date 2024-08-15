from selenium.webdriver.common.by import By


class Locators:
    TEL_FIELD = (By.ID, 'loginTel')
    PASSWD_FIELD = (By.XPATH, '//input[@name="password"]')
    LOGIN_BTN1 = (By.XPATH, '//button[@class="btn btn-primary"]')
    LOGIN_BTN2 = (By.XPATH, '//input[@class="btn btn-primary mb-2"]')
    NAME_FIELD = (By.XPATH, '//input[@name="name"]')
    AGREE_BOX = (By.XPATH, '//div[@class="custom-control custom-checkbox "]')
    SMS_CHECKBOX = (By.XPATH, '//input[@class="sms-code"][6]')
    ERROR_ALERT = (By.XPATH, '//div[@class="alert alert-danger"]')
    REGISTER_BTN = (By.XPATH, '//button[@class="btn btn-primary"]')
    USER_AVATAR = (By.XPATH, '//span[@class="user-avatar"]')
    EXIT_MENU = (By.XPATH, '//a[text()="Выход"]')

import logging
from time import sleep

from constants import TEST_URL, LOGIN_URL
from functions.login import fill_login_form, wait_for_login
from functions.main import logout
from pages.login_page import LoginPage

logger = logging.getLogger(__name__)


def test_login(driver):
    logger.info(f"Тест {test_login.__name__} запущен - OK!")
    login_page = LoginPage(driver)
    login_page.load()
    fill_login_form(driver)
    wait_for_login(driver)
    sleep(5)  # Демо-пауза для визуализации факта перехода в личное пространство клиента. В боевых прогонах удалить.
    assert driver.current_url == TEST_URL, 'Current URL does not match test criteria - ERROR!'
    logger.info("Пользователь успешно авторизован - OK!")


def test_logout(driver):
    logger.info(f"Тест {test_logout.__name__} запущен - OK!")
    logout(driver)
    sleep(5)  # Демо-пауза для визуализации факта разлогина. В боевых прогонах удалить
    assert driver.current_url == LOGIN_URL, 'Current URL does not match test criteria - ERROR!'
    logger.info("Пользователь успешно закрыл сессию - OK!")
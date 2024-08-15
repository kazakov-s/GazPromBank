import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session')
def driver(request):

    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1024,1024")
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()


# @pytest.fixture(scope='session')
# def driver(request):
#     chr_options = Options()
#     chr_options.add_experimental_option('detach', True)
#     chr_options.headless = False
#     chr_options.add_argument("--start-maximized")
#
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
#     driver.implicitly_wait(10)
#
#     yield driver
#     driver.quit()

import os
import pytest
import config

from selenium import webdriver
from selenium.webdriver.firefox.service import Service


def pytest_addoption(parser):
    parser.addoption('--chromeOptions',
                     action='store',
                     default='--start-maximized',
                     help='the chrome options driver will use')
    parser.addoption('--baseUrl',
                     default='http://automationpractice.com/',
                     help='base URL for the application under test')
    parser.addoption('--B',
                     default='chrome',
                     help='browser, default is chrome, available : firefox')


@pytest.fixture(scope="class", autouse=True)
def setup(request):
    config.chrome_options = request.config.getoption("--chromeOptions")
    config.baseUrl = request.config.getoption("--baseUrl")
    config.browser = request.config.getoption('--B')
    driver = None
    print("Initializing driver")
    if config.browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(config.chrome_options)
        chrome_options.add_argument('--disable-dev-shm-usage')
        prefs = {"download.default_directory": os.getcwd()+"/Downloads"}
        chrome_options.add_experimental_option('prefs', prefs)
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(10)  # seconds
    if config.browser == "firefox":
        driver = webdriver.Firefox()
    request.cls.driver = driver
    yield driver
    driver.save_screenshot(
        "./FailureScreenShots/screenshot_%s.png" % request.node.name)
    driver.quit()

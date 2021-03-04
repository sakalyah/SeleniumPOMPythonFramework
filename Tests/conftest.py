from urllib import request

import pytest
from selenium import webdriver

from Base.WebDriverFactory import WebDriverFactory
from Pages.Homepage.Login_page import Login_page


@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class") #scope ="module" if we want totest any module
def oneTimeSetUp(request):
    print("Running one time setUp")
    wdf = WebDriverFactory("chrome") #browser will be taken from CMD arguments
    driver = wdf.getWebDriverInstance()
    # if browser == 'firefox':
    #     driver = webdriver.Firefox(executable_path="D:\\PythonProject\\SeleniumProject\\Drivers\\geckodriver")
    #     driver.maximize_window()
    #     baseurl = "https://www.saucedemo.com/"
    #     driver.get(baseurl)
    #     print("Running tests on FF")
    # else:
    #     driver = webdriver.Chrome(executable_path="D:\\PythonProject\\SeleniumProject\\Drivers\\chromedriver")
    #     driver.maximize_window()
    #     baseurl = "https://www.saucedemo.com/"
    #     driver.get(baseurl)
    #     print("Running tests on chrome")
    #lp = Login_page(driver)
    #lp.login("standard_user","secret_sauce") --- > Please Enable these if testing any class other than login_tests
    if request.cls is not None :
        request.cls.driver = driver
    yield driver
    print("Running one time tearDown")

# def pytest_addoption(parser):
#     parser.addoption("--browser")
#     parser.addoption("--osType", help="Type of operating system")
#
# @pytest.fixture(scope="session")
# def browser(request):
#     return request.config.getoption("--browser")
#
# @pytest.fixture(scope="session")
# def osType(request):
#     return request.config.getoption("--osType")
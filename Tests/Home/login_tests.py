import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import *
import unittest
from Utilities.TestStatus import TestStatus
from Utilities.Readdata import getCSVData
from Pages.Homepage.Login_page import *
from ddt import ddt,data,unpack
from Base.Selenium_Driver import SeleniumDriver
import html

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
@ddt
class login_tests(unittest.TestCase):

    @pytest.fixture(autouse=True)  # Since we need this object for all methods we use autouse argument
    def classSetup(self,oneTimeSetUp):
        self.lp = Login_page(self.driver)
        self.ts = TestStatus(self.driver)
        self.sd = SeleniumDriver(self.driver)

    @pytest.mark.run(order=3)
    def test_validlogin(self):
        #self.driver.get(self.baseurl)

        self.lp.login("standard_user","secret_sauce")
        self.sd.shortteermwait(2)
        # result = self.lp.titlepagevalidation()
        result = self.lp.verifyLoginTitle()
        self.ts.mark(result, "Title Validation")
        # title = self.driver.title
        # # print(title)
        self.driver.implicitly_wait(3)
        # if title == "Swag Labs":
        #     print("Tests Successful")
        # assert title == "Swag Labs"
        # assert result==True
        result2 = self.lp.loginsuccess()
        self.ts.markFinal("Successful Login",result2,"Login Unsuccessful")
        self.lp.logout()
        self.driver.quit()

    @pytest.mark.run(order=1) #Used CSV Utility concept to parametarize the tests.
    @data(("standard_user", "secrets_sauce"), ("locked_out_user", "secrets_sauce"))
    @unpack
    def test_invalidloginA(self,username,password):
        #self.driver.get(self.baseurl)
        self.lp.login(username, password)
        reult = self.lp.login_unsuccess()
        assert reult == True
        self.sd.shortteermwait(2)

        # self.driver.quit()

    @pytest.mark.run(order=2)  # Used DDT concept to parametarize the tests.
    @data(*getCSVData("Readdata.csv")) #In Practice It is always good to give the whole path here.
    @unpack
    def test_invalidloginB(self, username, password):
        # self.driver.get(self.baseurl)
        self.lp.login(username, password)
        reult = self.lp.login_unsuccess()
        assert reult == True
        self.sd.shortteermwait(2)

        # self.driver.quit()

# a = login_tests()
# a.test_validlogin()#Do not create Objects and Run


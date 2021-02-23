import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import *
import unittest
from Utilities.TestStatus import TestStatus
from Pages.Homepage.Login_page import *

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class login_tests(unittest.TestCase):

    @pytest.fixture(autouse=True)  # Since we need this object for all methods we use autouse argument
    def classSetup(self,oneTimeSetUp):
        self.lp = Login_page(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validlogin(self):
        #self.driver.get(self.baseurl)

        self.lp.login("standard_user","secret_sauce")
        result = self.lp.titlepagevalidation()
        self.ts.mark(result, "Title Validation Failed")
        # title = self.driver.title
        # # print(title)
        self.driver.implicitly_wait(3)
        # if title == "Swag Labs":
        #     print("Tests Successful")
        # assert title == "Swag Labs"
        # assert result==True
        result2 = self.lp.loginsuccess()
        self.ts.markFinal("Successful Login",result2,"Login Unsuccessful")
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalidlogin(self):
        #self.driver.get(self.baseurl)
        self.lp.login("standard_user", "secrets_sauce")
        reult = self.lp.login_unsuccess()
        assert reult == True

# a = login_tests()
# a.test_validlogin()#Do not create Objects and Run


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import *
import unittest
from Pages.Homepage.Login_page import *

class login_tests(unittest.TestCase):
    driver = webdriver.Chrome(executable_path="D:\\PythonProject\\SeleniumProject\\Drivers\\chromedriver")
    driver.maximize_window()
    baseurl = "https://www.saucedemo.com/"
    lp = Login_page(driver)
    @pytest.mark.run(order=2)
    def test_validlogin(self):
        self.driver.get(self.baseurl)
        self.lp.login("standard_user","secret_sauce")
        title = self.driver.title
        print(title)
        self.driver.implicitly_wait(3)
        # if title == "Swag Labs":
        #     print("Tests Successful")
        assert title == "Swag Labs"
        result = self.lp.loginsuccess()
        assert result==True
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalidlogin(self):
        self.driver.get(self.baseurl)
        self.lp.login("standard_user", "secrets_sauce")
        reult = self.lp.login_unsuccess()
        assert reult == True

# a = login_tests()
# a.test_validlogin()


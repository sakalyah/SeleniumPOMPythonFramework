import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import *
import unittest

from Pages.Products.products import Products
from Utilities.TestStatus import TestStatus
from Utilities.Readdata import getCSVData
from Pages.Products import products
from Pages.Homepage.Login_page import Login_page
from ddt import ddt,data,unpack

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
@ddt
class product_tests(unittest.TestCase):

    @pytest.fixture(autouse=True)  # Since we need this object for all methods we use autouse argument
    def objectSetup(self,oneTimeSetUp):
        self.products = Products(self.driver)
        self.ts = TestStatus(self.driver)
        self.lp = Login_page(self.driver)

    @pytest.mark.run(order=1)
    @data(("performance_glitch_user","secret_sauce"))
    @unpack
    def test_addProducts(self,username,password):
        self.lp.login(username,password)
        self.products.clickaddtocart()
        self.lp.logout()
        self.driver.quit()
        time.sleep(1)



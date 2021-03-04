from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import *
from Base.Selenium_Driver import SeleniumDriver
import Utilities.CustomLogger as cl
import logging
from  Base.Basepage import BasePage

class Products(BasePage):
    log = cl.customLogger(logging.DEBUG)  # After Logging replced all Print statements to Log statements.

    def __init__(self, driver):
        super().__init__(driver)

    addtocart = "//button[text()='ADD TO CART']"

    def clickaddtocart(self):

        buttons = self.getElementList(self.addtocart,"xpath")
        for i in buttons :
            i.click()
            self.shortteermwait(1)

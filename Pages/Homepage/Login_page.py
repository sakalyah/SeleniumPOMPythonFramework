from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import *
from Base.Selenium_Driver import SeleniumDriver
import Utilities.CustomLogger as cl
import logging


class Login_page(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)  # After Logging replced all Print statements to Log statements.
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    # def getemailfield(self):
    #     return  self.driver.find_element(By.ID, "user-name")
    # def getpwdfield(self):
    #     return  self.driver.find_element(By.ID, "password")
    # def loginbtn(self):
    #     return self.driver.find_element(By.ID, "login-button")
    def enteremail(self,email):
        #self.getemailfield().send_keys(email)
       self.inputtextbyID("user-name",email)
    def enterpwd(self,pwd):
        #self.getpwdfield().send_keys(pwd)
        self.inputtextbyID("password", pwd)
    def click_login(self):
        #self.loginbtn().click()
        self.clickelementbyID("login-button")

    def login(self,username,password):
        #loginLink = self.driver.find_element(By.LINK_TEXT, "Login")
        #loginLink.click()
        self.enteremail(username)
        self.enterpwd(password)
        self.click_login()
        # emailField = self.driver.find_element(By.ID, "user-name")
        # emailField.send_keys(username)
        #
        # passwordField = self.driver.find_element(By.ID, "password")
        # passwordField.send_keys(password)
        #
        # time.sleep(2)
        #
        # loginButton = self.driver.find_element(By.ID, "login-button")
        # loginButton.click()

    def loginsuccess(self):

        result = self.isElementVisible(By.CLASS_NAME,"product_sort_container")
        return result

    def login_unsuccess(self):

        result = self.isElementVisible(By.XPATH,"//h3[@data-test='error']")
        return result
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import *
from Base.Selenium_Driver import SeleniumDriver
import Utilities.CustomLogger as cl
import logging
from  Base.Basepage import BasePage


class Login_page(BasePage): #Replacing SeleniumDriver class with Basepage class ----> Multi Level Inheritance
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

    def pagetitle(self):
        return self.driver.title

    def titlepagevalidation(self):

        if "Swag Labs"  in self.pagetitle():
            return True
        else :
            return False
        #if "Google"  in self.pagetitle(): To CHeck Failure

    def verifyLoginTitle(self):
        #return self.verifyPageTitle("Google") #Inherited from BasePage class -- Explicitly Failed
        return self.verifyPageTitle("Swag Labs") #Inherited from BasePage class
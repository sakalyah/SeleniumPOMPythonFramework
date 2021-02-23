import os
import time

from traceback import print_stack

from selenium import webdriver
from selenium.webdriver.common.by import By

from Drivers.BrowserLaunch import BrowserLaunch
from Drivers.BrowserLaunch import ElementsandData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import Utilities.CustomLogger as cl
import logging

class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG) #After Logging replced all Print statements to Log statements.

    def __init__(self,driver):
        self.driver = driver

    def getByType(self,locatorType):
        locatorType = locatorType.lower()
        if locatorType=='id':
            return By.ID
        elif locatorType=='xpath':
            return By.XPATH
        elif locatorType=='css':
            return By.CSS_SELECTOR
        else:
            self.log.info("Locator Type Not Defined")

    def getelement(self,locator,locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType,locator)
            self.log.info("Element Found")
        except:
            self.log.info("Element Not FOund")
        return element

    def getelement2(self,TypeBy,selector):

        element1 = None
        try:
            element1 = self.driver.find_element(TypeBy,selector)
            if element1 is not  None:
                self.log.info("Selector Found")
        except:
            self.log.info("Something Went Wrong")
        return element1

    def isElementVisible(self,TypeBy,selector):
        element = None
        try:
            element = self.driver.find_element(TypeBy,selector)
            if element.is_displayed():
                self.log.info("Element is Visible on Page")
                return  True
            else :
                self.log.info("Element is not Visible on Page")
                return False
        except:
            self.log.info("Something Went Wrong")
            return False

    def waitforElementtoVisible(self,timeout,TypeBy,selector):
        try :
          element = None
          wait = WebDriverWait(self.driver,timeout,poll_frequency=10,ignored_exceptions=
                             [NoSuchElementException,ElementNotVisibleException,InvalidSelectorException])
          element = wait.until(EC.visibility_of_element_located((TypeBy,selector)))
          self.log.info("Waited till Element was Visible")
          return element
        except Exception as e :
            self.log.info("No Such Element Found",e)
            print_stack()
            raise e

    def takeScreenshot(self):
        filename ='jin'+str(1000)+'.png'
        destinationfile = ElementsandData.DestinationFIle + filename
        try:
           self.driver.save_screenshot(destinationfile)
           self.log.info("Screenshot taken successfully")
        except NotADirectoryError:
            self.log.info("Screenshot Failed")

    def clickelementbyxpath(self,xpath):
        try:
          ele = self.waitforElementtoVisible(10,By.XPATH,xpath)
          ele.click()
          self.log.info("Clicked Successfully")
        except :
            self.log.info("Cannot CLick the Element By xpath"+xpath)
            print_stack()

    def clickelementbyID(self,ID):
        try:
          ele = self.waitforElementtoVisible(10,By.ID,ID)
          ele.click()
          self.log.info("Clicked Successfully")
        except :
            self.log.info("Cannot CLick the Element By ID "+ID)
            print_stack()

    def inputtextbyXpath(self,xpath,value):
        try:
            ele = self.waitforElementtoVisible(10,By.XPATH,xpath)
            ele.send_keys(value)
            self.log.info("Entered Successfully "+value)
        except:
            self.log.info("Cannot Send keys to locator " + xpath)
            print_stack()
    def inputtextbyID(self,ID,value):
        try:
            ele = self.waitforElementtoVisible(10,By.ID,ID)
            ele.clear()
            ele.send_keys(value)
            self.log.info("Entered Successfully "+value)
        except:
            self.log.info("Cannot Send keys to locator " + ID)
            print_stack()

    def takescreenshot(self,resultMessage):

        """
                Takes screenshot of the current open web page #FrameworkLevel
                """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png" #Will create multiple Files
        screenshotDirectory = "../Screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()
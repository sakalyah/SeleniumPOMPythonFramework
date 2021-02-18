import inspect
import logging

def customLogger(logLevel):
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3] #Gives the Name of the Method or class which is calling this customLogger Method
    logger = logging.getLogger(loggerName)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("SeleniumPOMFramework.log", mode='a')#FIle name should be provided otherwise each class will create one log file
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger

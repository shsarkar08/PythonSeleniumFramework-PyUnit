import datetime

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.support.wait import WebDriverWait
from Config.Logger import pyLog


                                            ###############################################
                                            ###    Base Utility Class                  ####
                                            ###    All Pages should extend this class  ####
                                            ###############################################


class BasePage:

    def __init__(self,driver):
        self.driver = driver

        self.logger = pyLog.logr(__name__)
        self.logger.propagate = False

    def get_locator_type(self, locator_type):
        try:
            locator_type = locator_type.lower()

            if locator_type=="id":
                return By.ID
            elif locator_type=="xpath":
                return By.XPATH
            elif locator_type=="name":
                return By.NAME
            elif locator_type=='tag':
                return By.TAG_NAME
            elif locator_type=="class":
                return By.CLASS_NAME
            elif locator_type=="link":
                return By.LINK_TEXT
            elif locator_type=="partiallink":
                return By.PARTIAL_LINK_TEXT
        except:
            self.logger.error("Locator Type "+str(locator_type)+" is not listed.")

    def findelement(self,locator_type,locator_properties):
        try:
            return self.driver.find_element(self.get_locator_type(locator_type),locator_properties)
        except Exception as e:
            self.logger.error(e)

    def findelements(self,locator_type,locator_properties):
        try:
            return self.driver.find_elements(self.get_locator_type(locator_type),locator_properties)
        except Exception as e:
            self.logger.error(e)

    def click(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(
                cond.visibility_of_element_located((by_locator))
            ).click()
        except Exception as e:
            self.logger.error(e)


    def set_text_value(self, locator_type, locator_properties, text: str):
        """
        :param locator_type: xpath or id or name
        :param locator_properties: locator string
        :param text: text to be injected
        """
        try:
            self.driver.find_element(self.get_locator_type(locator_type),locator_properties).send_keys(text)
            return text
        except Exception as e:
            self.logger.error(e)

    def get_attribute_value(self, locator_type, locator_properties):
        """
        :param locator_type: xpath or id or name
        :param locator_properties: locator string
        :return Webelement get attribute value
        """
        try:
            return self.findelement(locator_type,locator_properties).get_attribute('value')
        except Exception as e:
            self.logger.error(e)

    def get_text(self,locator_type,locator_properties):
        try:
            return self.findelement(locator_type,locator_properties).text
        except Exception as e:
            self.logger.error(e)

    def wait_for_element_to_be_present(self, locator_properties: str, locator_type="xpath", max_time_out: int = 15):
        """
        check for the presence of the element
        :param locator_properties: locator string
        :param locator_type: xpath or id or name
        :param max_time_out: 15
        :return: bool
        """
        try:
            WebDriverWait(self.driver,max_time_out,ignored_exceptions=[StaleElementReferenceException]).until(
                cond.presence_of_element_located((self.get_locator_type(locator_type),locator_properties))
            )
            return True
        except TimeoutError:
            return False

    def element_enabled(self, locator_type,locator_properties):
        return self.driver.find_element(self.get_locator_type(locator_type),locator_properties).is_enabled()


    def switchFrame(self,frame_locator):
        """  :param frame_locator: name/id/xpath for iframe
        """
        try:
            self.driver.switch_to.frame(frame_locator)
            self.logger.info('successfully switched to iframe')
        except Exception as e:
            self.logger.error(e)

    def switchWindow(self):

        __phandle = self.driver.current_window_handle
        self.logger.info("Parent Window :{} ".format(self.driver.title))

        handles = self.driver.window_handles
        h_size = len(handles)

        for hdl in range(h_size):
            if handles[hdl] != __phandle:
                self.driver.switch_to.window(handles[hdl])
                self.logger.info('Current New Window :{} '.format(self.driver.title))
                break

    def switchDefaultWindow(self):

        __pwindow = self.driver.window_handles[0]
        self.driver.switch_to.window(__pwindow)
        self.logger.info('Switched to Parent window :{} '.format(self.driver.title))

    def keyAction(self,element,keys ):
        element.send_keys(keys)

    def getTime(self):
       return datetime.datetime.now().strftime("%H:%M:%S")

    def selectJavaScript(self,elementName,value):
        try:
            jse = "document.getElementsByName('"+elementName+"')[0].value = "+value+";"
            self.driver.execute_script(jse)
        except Exception as e:
            self.logger.error(e)
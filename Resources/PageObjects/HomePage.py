from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from Resources.PageObjects.BasePage import BasePage
from Resources.TestData import TestData
from Resources.Locators import Locators
import time


class Homepage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def getUserName(self):
        username = self.get_text('xpath',Locators.NAME)
        self.logger.info('Username ~ {}'.format(username))

    def validateURL(self):
        try:
            WebDriverWait(self.driver, 20).until(
                cond.url_contains('home')
            )
        except Exception as e:
            self.logger.error('URL doesn\'t contain \'home\'  in it', e)

        self.logger.info(self.driver.current_url)
        time.sleep(2)

    def applyFilter(self):

        query = self.set_text_value('xpath',Locators.FILTER_BOX,TestData.QUERY)
        self.logger.info('Query applied as ~ {}'.format(query))
        self.click(Locators.CREATE_NEW_WIDGET)
        self.logger.info('Clicked on Create New')

        time.sleep(2)

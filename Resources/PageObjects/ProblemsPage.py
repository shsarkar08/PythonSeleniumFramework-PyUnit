import time
import unittest
from selenium.webdriver.common.keys import Keys
from Resources.PageObjects.BasePage import BasePage
from Resources.PageObjects.ServiceTicket import TicketCreation
from Resources.Locators import Locators


class AllProblems(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    """
    Search for Ticket
    """

    def searchTicket(self):

        self.driver.switch_to.default_content()
        self.switchFrame(Locators.IFRAME)

        tc = TicketCreation(self.driver)
        self.inp_st = tc.getPrbStmt()

        jse = self.driver.execute_script(Locators.SEARCH_ICON_ATTRIBUTE)
        self.logger.debug('Search-icon Expanded ? {} '.format(jse))

        try:
            assert jse == 'false',"Search Menu is Already Expanded"
            self.click(Locators.SEARCH_ICON)

        except Exception as e:
            self.logger.error(e)

        finally:
            search_box = self.findelement('xpath', Locators.SEARCH_BOX)
            self.set_text_value('xpath', Locators.SEARCH_BOX, self.inp_st)
            self.keyAction(search_box, Keys.ENTER)
            time.sleep(2)


    """
     Validate Problem Number
    :Zero Matches
    :Similar Matches
    :Exact Match
    """

    def verifyTicket(self):

        no_of_rows = len(self.findelements('xpath',Locators.RESULT_ROW))
        self.logger.info('Search Rows Found :{} '.format(no_of_rows))

        try:
            assert no_of_rows != 0 , "No Rows Available"

            prb_stmt = self.get_text('xpath',Locators.RESULT_PRB_STMT)
            self.logger.info('Found Row/Rows with problem statement : {} '.format(prb_stmt))

            try:
                t= unittest.TestCase()
                t.assertEqual(self.inp_st, prb_stmt , 'Problem Statement is not getting matched')

            except AssertionError as e:
                self.logger.error(e)
        except AssertionError as ae:
            self.logger.error(ae)

        self.driver.save_screenshot('..\\Screenshots\\SN_Test.png')
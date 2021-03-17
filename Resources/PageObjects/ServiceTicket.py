from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from Resources.PageObjects.BasePage import BasePage
from Resources.TestData import TestData
from Resources.Locators import Locators
import time
import random
import unittest


class TicketCreation(BasePage):

    inp_st = ""

    def __init__(self,driver):
        super().__init__(driver)

    """
    Methods to Suppport Actions for New Ticket Creation
    """

    def get_problem_no(self):

        self.switchFrame(Locators.IFRAME)
        time.sleep(5)

        is_enabled = self.element_enabled('xpath',Locators.PROBLEM_NUMBER)
        self.logger.info('Number Input Field is Enabled ? {}'.format(is_enabled))
        pr_no = self.get_attribute_value('xpath',Locators.PROBLEM_NUMBER)
        self.logger.info('Problem Number: {} '.format(pr_no))

    """
    Selecting Task - First reported by
    """

    def selectTask(self):

        self.click(Locators.TASK_SEARCH_ICON)
        time.sleep(2)
        self.switchWindow()

        """
        Selecting Random Row
        """
        no_of_rows = len(self.findelements('xpath',Locators.TASK_REPORTED_BY))
        r_int = random.randrange(0, no_of_rows, 1)

        try:
            self.driver.find_element_by_xpath("//tr[contains(@id,'row_task')]["+str(r_int+1)+"]//a").click()
            print('Task selected')
        except Exception as e:
            self.logger.error('Unable to select task - ', e)

        self.switchDefaultWindow()
        self.switchFrame(Locators.IFRAME)
        time.sleep(2)

    '''
    Selecting Last option from Category Dropdown
    '''

    def selectCategory(self):

        category = Select(self.findelement('xpath',Locators.CATEGORY))
        lopt = len(category.options)

        try:
            category.select_by_index(lopt-1)
        except Exception as e:
            self.logger.error(e)
        time.sleep(2)

    """
    Selecting longest sub-category from dropdown [Without Select Method]
    """

    def selectSubCategory(self):

        sub_category = self.findelement('xpath',Locators.SUB_CATEGORY)
        options = sub_category.find_elements_by_tag_name('option')

        t_option=""

        ilen = -1
        for option in options:
            r=option.text
            if len(r) > ilen:
                ilen = len(r)
                t_option = r

        self.logger.info('Longest s-category found :{} '.format(t_option))

        for se_option in options:
            if se_option.text == t_option:
                se_option.click()

        time.sleep(1)

    """
    Selecting Last Item from Service Table
    """

    def selectService(self):

        self.click(Locators.SERVICE_ICON)
        time.sleep(2)

        self.switchWindow()
        self.click(Locators.NEXT_BUTTON_SERVICE)
        time.sleep(2)
        no_of_serv_rows = len(self.findelements('xpath',Locators.SERVICES))
        v_last_row_sev = self.driver.find_element_by_xpath(
            '//tr[contains(@id,"row_cmdb_ci_service")]'+
            '['+str(no_of_serv_rows)+']//a').get_attribute('text')
        print(v_last_row_sev)
        self.driver.find_element_by_xpath('//tr[contains(@id,"row_cmdb_ci_service")]['+str(no_of_serv_rows)+']//a').click()
        self.logger.info('Service Selected ')

        self.switchDefaultWindow()
        self.switchFrame(Locators.IFRAME)

        time.sleep(2)

    """
    Choose Configuration Item
    """

    def selectConfItem(self):

        self.click(Locators.CONFIGURATION_SEARCH_ICON)
        time.sleep(2)

        self.switchWindow()

        t_cnf_item = self.get_text('xpath',Locators.CONFIGURATION_TOTAL_ROWS)
        self.logger.info('Total Conf Item ~ {}'.format(t_cnf_item))

        ft = t_cnf_item.replace(',', '')
        cnf_no = random.randrange(0, int(ft), 1)

        inp_page_no = self.findelement('xpath',Locators.CONFIGURATION_INPUT)
        inp_page_no.clear()
        self.set_text_value('xpath',Locators.CONFIGURATION_INPUT,cnf_no)

        self.keyAction(inp_page_no,Keys.ENTER)
        time.sleep(2)

        self.click(Locators.CONFIGURATION_ITEM_ROW)
        self.logger.info('Configuration item selected')

        self.switchDefaultWindow()
        self.switchFrame(Locators.IFRAME)

    """
    Type Problem Statement
    """

    def problemStmt(self):

        time_now = self.getTime()
        TicketCreation.inp_st = TestData.PROBLEM_STATEMENT + time_now

        self.set_text_value('xpath',Locators.PROBLEM_STATEMENT,TicketCreation.inp_st)

    def getPrbStmt(self):

        print("Problem Statement to Match ~ {} ".format(TicketCreation.inp_st))
        return TicketCreation.inp_st

    """
    Confirm State Value
    """

    def ticketState(self):

        state_value = self.get_text('xpath',Locators.TICKET_STATE)
        self.logger.info('State Value Fetched As ~{} '.format(state_value))
        #self.assertEqual(TestData.STATE, state_value, 'Problem Status value is not getting Matched')
        t = unittest.TestCase('__str__')
        t.assertEqual(TestData.STATE, state_value, 'Problem Status value is not getting Matched')

    """
    Select Impact & Urgency [Using JavaScript Method]
    """

    def selectImpactUrgency(self):

        self.selectJavaScript(TestData.IMPACT_NAME,TestData.IMPACT_VALUE)
        self.selectJavaScript(TestData.URGENCY_NAME, TestData.URGENCY_VALUE)

        time.sleep(1)

    """
    Choose Assigned To
    """
    def selectAssignTo(self):

        inp = self.findelement('xpath',Locators.ASSIGNED_TO)
        self.set_text_value('xpath',Locators.ASSIGNED_TO,TestData.ASSIGNED_TO_INPUT)
        time.sleep(3)
        self.keyAction(inp,Keys.DOWN)
        self.keyAction(inp,Keys.ENTER)
        time.sleep(1)

    """
    Submit the ticket
    """
    def submit(self):

        self.click(Locators.SUBMIT_BUTTON)
        self.logger.info('Ticket Submitted')


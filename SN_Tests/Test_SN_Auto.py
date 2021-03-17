import unittest
from selenium import webdriver
from Resources.PageObjects.Login_LandingPage import LoginPage
from Resources.PageObjects.HomePage import Homepage
from Resources.PageObjects.ServiceTicket import TicketCreation
from Resources.PageObjects.ProblemsPage import AllProblems
from Config.Logger import pyLog



                                            ###############################################
                                            ####      Service NOW Ticket Creation      ####
                                            ####      Test Script file                 ####
                                            ###############################################

class ServiceNow(unittest.TestCase):

    logger = pyLog.logr(__name__)

    def setUp(self):

        options = webdriver.ChromeOptions()
        options.add_experimental_option('useAutomationExtension', False)
        # options.add_argument('--headless')ure

        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.driver.get('about:blank')

    def tearDown(self):

        self.logger.info("Test {0} has been executed Successfully".format(__name__))
        try:
            self.driver.quit()
        except Exception as e:
            self.logger.error(e)


class TestServiceNow(ServiceNow):
    # def setUp(self):
    #     super().setUp()


    def test_ServiceNow(self):

        self.loginPage = LoginPage(self.driver)
        self.loginPage.login()

        self.homepage = Homepage(self.driver)
        self.homepage.getUserName()
        self.homepage.validateURL()
        self.homepage.applyFilter()

        self.sticket = TicketCreation(self.driver)
        self.sticket.get_problem_no()
        self.sticket.selectTask()
        self.sticket.selectCategory()
        self.sticket.selectSubCategory()
        self.sticket.selectService()
        self.sticket.selectConfItem()
        self.sticket.problemStmt()
       # self.sticket.getPrbStmt()
        self.sticket.ticketState()
        self.sticket.selectImpactUrgency()
        self.sticket.selectAssignTo()
        self.sticket.submit()

        self.allproblems = AllProblems(self.driver)
        self.allproblems.searchTicket()
        self.allproblems.verifyTicket()

        self.loginPage.logout()

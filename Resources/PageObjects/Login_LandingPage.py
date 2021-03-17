from Resources.PageObjects.BasePage import BasePage
from Resources.TestData import TestData
from Resources.Locators import Locators
import time


class LoginPage(BasePage,TestData):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def login(self):

        self.switchFrame(Locators.IFRAME)
        #self.driver.switch_to.frame(Locators.IFRAME)
        time.sleep(2)

        # self.findelement('xpath',Locators.USERNAME)
        # self.findelement('xpath',Locators.PASSWORD)

        self.set_text_value('xpath',Locators.USERNAME,TestData.USERNAME)
        self.set_text_value('xpath',Locators.PASSWORD,TestData.PASSWORD)

        time.sleep(2)

        self.click(Locators.LOGIN_BTN)
        self.logger.info('Log In Successful')

        self.driver.switch_to.default_content()

    """
    Logout
    """

    def logout(self):

        self.driver.switch_to.default_content()

        self.click(Locators.USER_DROPDOWN)
        time.sleep(1)
        menus = self.driver.find_elements_by_tag_name('li')
        for menu in menus:
            try:
                if menu.text == TestData.LOGOUT:
                    menu.click()
                    self.logger.info('Logged Out Successfully')
                    break
            except Exception as e:
                self.logger.error('Logout- Option Not found')
        time.sleep(3)

        self.driver.save_screenshot('..\\Screenshots\\SN_Logout.png')


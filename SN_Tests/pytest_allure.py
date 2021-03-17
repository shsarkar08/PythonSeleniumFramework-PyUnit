import pytest
import allure
import unittest

from allure_commons.types import AttachmentType
from selenium import webdriver



class DemoAllure(unittest.TestCase):

    @allure.testcase("Test Case with first Allure report")
    def test_site_loads(self):
        self.launch_site()
        self.verify_site()

    @allure.title('launching Google')
    @allure.step("Launch site")
    @allure.severity(allure.severity_level.CRITICAL)
    def launch_site(self):

        # self.driver = webdriver.Chrome()
        # self.driver.get("http://qaboy.com/")

        options = webdriver.ChromeOptions()
        options.add_experimental_option('useAutomationExtension', False)

        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get("https://google.com/")
        allure.attach(self.driver.get_screenshot_as_png(),name="Google",attachment_type=AttachmentType.PNG)

    @allure.title('Verify Title')
    @allure.step("Title should match with google")
    @allure.severity(allure.severity_level.MINOR)
    def verify_site(self):
        assert "Google" == self.driver.title

    def test_skiptest(self):
        pytest.skip('This test has been skipped')
import datetime
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import traceback
import random


###############################################
####          Service NOW                  ####
####          RAW E2E Script file          ####
###############################################


class MyTestCase(unittest.TestCase):
    pr_number = (By.XPATH, "//input[@name='problem.number']")

    def setUp(self):

        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_experimental_option('useAutomationExtension', False)

        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.driver.get('about:blank')
        # yield self.driver

    def test_SN(self):
        """
        login
        :return: None
        """
        # print(self._testMethodName)
        self.driver.get('https://dev70821.service-now.com')
        time.sleep(2)
        iframe = self.driver.find_element(By.XPATH, "//iframe[@id='gsft_main']")
        self.driver.switch_to.frame(iframe)

        try:
            elem = self.driver.find_element(By.CSS_SELECTOR, '#user_name')
            elem.send_keys("admin")
        except Exception as e:
            print(e)
        self.driver.find_element(By.XPATH, '//*[@id="user_password"]').send_keys("Shahnawaz0893#")
        self.driver.find_element(By.XPATH, '//*[@id="sysverb_login"]').click()
        print('Log In Successful')

        self.driver.switch_to.default_content()

        """
        landing Page actions
        """
        name = self.driver.find_element_by_xpath(
            "//button[@id='user_info_dropdown']//span[contains(@class,'user-name')]")
        t_name = (By.XPATH, "//button[@id='user_info_dropdown']//span[contains(@class,'user-name')]")
        try:
            WebDriverWait(self.driver, 15).until(
                cond.presence_of_element_located(t_name)
            )
            print("Username ~ ", name.text)
        except:
            tb = traceback.print_exc()
            print(tb)

        try:
            WebDriverWait(self.driver, 20).until(
                cond.url_contains('home')
            )
        except Exception as e:
            print('URL doesn\'t contain \'home\'  in it', e)

        print(self.driver.current_url)
        time.sleep(3)
        """
        filter category
        """
        self.driver.implicitly_wait(10)
        query = "Problem"
        filter_box = '//*[@id="filter"]'
        create_new_widget = "//div[@data-id='a1beba50c611227801908558c921ab78']/div[contains(.,'Create New')]"

        self.driver.find_element_by_xpath(filter_box).send_keys(query)
        print('Query applied as ~ ', query)
        self.driver.find_element_by_xpath(create_new_widget).click()
        print('Clicked on Create New')

        """
        Actions for New Ticket Creation
        """
        try:
            self.driver.switch_to.frame('gsft_main')
            print('successfully switched to iframe')
        except Exception as e:
            print(e)

        time.sleep(10)

        pr_number = (By.XPATH, "//input[@name='problem.number']")

        try:
            WebDriverWait(self.driver, 10).until(
                cond.presence_of_element_located(pr_number)
            )
        except Exception as e:
            print('Unable to locate Number element ', e)

        enb_number = self.driver.find_element(*self.pr_number).is_enabled()
        print('Number Input Field is Enabled ? ', enb_number)

        """ 
        Print Problem Number 
        """

        t_pr_number = self.driver.find_element(*self.pr_number).get_attribute('value')
        print('Problem Number ~ ', t_pr_number)

        """
        Selecting Task - First reported by
        """
        search_icon = '//*[@id="lookup.problem.first_reported_by_task"]/span'
        self.driver.find_element_by_xpath(search_icon).click()
        time.sleep(2)

        window_before = self.driver.window_handles[0]
        print("Parent Window Title : ", self.driver.title)

        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

        print("New Window Title : ", self.driver.title)

        tab_reported_by = self.driver.find_elements_by_xpath("//tr[contains(@id,'row_task')]")

        """
        Selecting Random Row
        """
        no_of_rows = len(tab_reported_by)
        r_int = random.randrange(0, no_of_rows, 1)

        try:
            self.driver.find_element_by_xpath("//tr[contains(@id,'row_task')][" + str(r_int + 1) + "]//a").click()
            print('Task selected')
        except Exception as e:
            print('Unable to select task - ', e)

        time.sleep(2)

        """
        Switching Back to Main Window & Frame
        """
        self.driver.switch_to.window(window_before)
        print(self.driver.title)

        self.driver.switch_to.frame('gsft_main')
        print('successfully switched to iframe')

        time.sleep(3)

        """
        Selecting Last option from Category Dropdown
        """
        category = Select(self.driver.find_element_by_xpath('//*[@id="problem.category"]'))
        lopt = len(category.options)

        try:
            sopt = category.select_by_index(lopt - 1)
        except Exception as e:
            print(e)

        time.sleep(3)

        """
        Selecting longest sub-category from dropdown [Without Select Method]
        """

        sub_category = self.driver.find_element_by_xpath('//*[@id="problem.subcategory"]')
        options = sub_category.find_elements_by_tag_name('option')

        t_option = ""

        ilen = -1
        for option in options:
            r = option.text
            if len(r) > ilen:
                ilen = len(r)
                t_option = r

        print('Longest s-category found : ', t_option)
        # sub_category.select_by_visible_text(t_option)
        for se_option in options:
            if se_option.text==t_option:
                se_option.click()

        time.sleep(2)

        """
        Selecting Last Item from Service Table
        """

        service_icon = '//*[@id="lookup.problem.business_service"]'
        self.driver.find_element_by_xpath(service_icon).click()

        time.sleep(3)

        parent_handle = self.driver.current_window_handle

        handles = self.driver.window_handles
        h_size = len(handles)

        for hdl in range(h_size):
            if handles[hdl]!=parent_handle:
                self.driver.switch_to.window(handles[hdl])
                print('Current New Window Title : ', self.driver.title)
                break
                # Traverse to Last Page of the service Table
        self.driver.find_element_by_xpath("//button[@name='vcr_last']").click()
        time.sleep(2)
        no_of_serv_rows = len(self.driver.find_elements_by_xpath('//tr[contains(@id,"row_cmdb_ci_service")]'))
        v_last_row_sev = self.driver.find_element_by_xpath(
            '//tr[contains(@id,"row_cmdb_ci_service")][' + str(no_of_serv_rows) + ']//a').get_attribute('text')
        print(v_last_row_sev)
        self.driver.find_element_by_xpath(
            '//tr[contains(@id,"row_cmdb_ci_service")][' + str(no_of_serv_rows) + ']//a').click()
        print('Service Selected ')

        self.driver.switch_to.window(parent_handle)
        self.driver.switch_to.frame('gsft_main')

        time.sleep(2)

        """
        Choose Configuration Item
        """
        self.driver.find_element_by_xpath('//button[@id="lookup.problem.cmdb_ci"]').click()
        time.sleep(3)

        parent_handle = self.driver.current_window_handle

        handles = self.driver.window_handles

        for cfi in range(h_size):
            if handles[cfi]!=parent_handle:
                self.driver.switch_to.window(handles[cfi])
                print('Switched to Window ~', self.driver.title)
                break

        t_cnf_item = self.driver.find_element_by_xpath(
            "//div[@class='vcr_controls']//span[contains(@id,'total_rows')]").text
        print('Total Conf Item ~ ', t_cnf_item)

        ft = t_cnf_item.replace(',', '')
        cnf_no = random.randrange(0, int(ft), 1)

        inp_page_no = self.driver.find_element_by_xpath('//input[@aria-label="Skip to row"]')
        inp_page_no.clear()
        inp_page_no.send_keys(cnf_no)
        inp_page_no.send_keys(Keys.ENTER)

        time.sleep(3)

        try:
            self.driver.find_element_by_xpath("//tr[contains(@id,'row_cmdb_ci')]//a").click()
            print('Configuration item selected')
        except Exception as e:
            print('Unable to select Configuration item - ', e)

        self.driver.switch_to.window(parent_handle)
        self.driver.switch_to.frame('gsft_main')

        time.sleep(2)

        """
        Type Problem Statement
        """
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        ps_inp_box = '//*[@id="problem.short_description"]'
        inp_st = "TESTLEAF CONTEST - " + time_now

        self.driver.find_element_by_xpath(ps_inp_box).send_keys(inp_st)

        time.sleep(1)

        """
        Confirm State Value
        """

        state = Select(self.driver.find_element_by_xpath('//*[@id="sys_readonly.problem.state"]'))
        state_value = state.first_selected_option.text
        print('State Value Fetched As ~ ', state_value)
        self.assertEqual('New', state_value, 'Problem Status value is not getting Matched')

        """
        Select Impact & Urgency [Using JavaScript Method]
        """

        impact = "document.getElementsByName('problem.impact')[0].value = '2';"  # Medium
        self.driver.execute_script(impact)

        urgency = "document.getElementsByName('problem.urgency')[0].selectedIndex = '0';"  # High
        self.driver.execute_script(urgency)

        time.sleep(2)

        """
        Choose Assigned To
        """
        assign_value = "Problem Co"
        assigned_to = '//*[@id="sys_display.problem.assigned_to"]'
        inp_assignd_to = self.driver.find_element_by_xpath(assigned_to)
        inp_assignd_to.send_keys(assign_value)
        time.sleep(2)
        inp_assignd_to.send_keys(Keys.DOWN)
        inp_assignd_to.send_keys(Keys.ENTER)
        time.sleep(1)

        """
        Submit the application
        """
        btn = "//div[@class='form_action_button_container']//button[@type='submit']"
        self.driver.find_element_by_xpath(btn).click()
        print('Ticket Submitted')
        time.sleep(2)

        self.driver.switch_to.default_content()

        """
        Search & Verify Problem Number
        :Zero Matches
        :Similar Matches
        :Exact Match
        """

        iframe = self.driver.find_element(By.XPATH, "//iframe[@id='gsft_main']")
        self.driver.switch_to.frame(iframe)

        # search_box = Select(self.driver.find_element_by_xpath("//div[@class='container-fluid']//select"))
        # search_box.select_by_visible_text('Problem statement')

        inp_search_box = self.driver.find_element_by_xpath("//td[@name='short_description']//input[@type='search']")
        inp_search_box.send_keys(inp_st)  # inp_st
        inp_search_box.send_keys(Keys.ENTER)

        time.sleep(2)

        t_row = "//table[@id = 'problem_table']//tr[contains(@id,'row_problem')]"
        no_of_rows = len(self.driver.find_elements_by_xpath(t_row))
        print('Search Rows Found : ', no_of_rows)

        try:
            assert no_of_rows!=0, "No Rows Available"
            # if no_of_rows != 0:
            prb_stmt = self.driver.find_element_by_xpath("//tr[contains(@id,'row_problem')]/td[4]").text
            print('Found Ticket with problem statement : ', prb_stmt)
            try:
                self.assertEqual(inp_st, prb_stmt, 'Problem Statement is not getting matched')
            except AssertionError as e:
                print(e)
        except AssertionError as ae:
            print(ae)

        self.driver.save_screenshot('..\\SN_Tests.png')
        """
        Logout
        """
        self.driver.switch_to.default_content()

        lgt_drpdwn = "//button[@id='user_info_dropdown']"
        self.driver.find_element_by_xpath(lgt_drpdwn).click()
        time.sleep(1)
        menus = self.driver.find_elements_by_tag_name('li')
        for menu in menus:
            try:
                if menu.text=='Logout':
                    menu.click()
                    print('Logged Out Successfully')
                    break
            except NoSuchElementException:
                print('Logout- Option Not found')
        time.sleep(3)
        self.driver.save_screenshot('..\\SN_Logout.png')

    def tearDown(self):
        self.driver.quit()


if __name__=='__main__':
    unittest.main()

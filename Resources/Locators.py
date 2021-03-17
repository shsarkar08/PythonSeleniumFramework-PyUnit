from selenium.webdriver.common.by import By


class Locators:
    # --- Loign Page ---

    IFRAME = 'gsft_main'
    USERNAME = '//*[@id="user_name"]'
    PASSWORD = '//*[@id="user_password"]'
    LOGIN_BTN = (By.ID, 'sysverb_login')

    # --- Landing Page ---
    NAME = "//button[@id='user_info_dropdown']//span[contains(@class,'user-name')]"
    FILTER_BOX = '//*[@id="filter"]'
    CREATE_NEW_WIDGET = (By.XPATH, "//div[@data-id='a1beba50c611227801908558c921ab78']/div[contains(.,'Create New')]")

    # --- Frame Elements -- Ticket Creation Page  --
    PROBLEM_NUMBER = "//input[@name='problem.number']"
    TASK_SEARCH_ICON = (By.XPATH,'//*[@id="lookup.problem.first_reported_by_task"]/span')
    TASK_REPORTED_BY = "//tr[contains(@id,'row_task')]"
    CATEGORY = '//*[@id="problem.category"]'
    SUB_CATEGORY = '//*[@id="problem.subcategory"]'
    SERVICE_ICON = (By.XPATH,'//*[@id="lookup.problem.business_service"]')
    NEXT_BUTTON_SERVICE = (By.XPATH,"//button[@name='vcr_last']")
    SERVICES = '//tr[contains(@id,"row_cmdb_ci_service")]'
    CONFIGURATION_SEARCH_ICON = (By.XPATH,'//button[@id="lookup.problem.cmdb_ci"]')
    CONFIGURATION_TOTAL_ROWS = "//div[@class='vcr_controls']//span[contains(@id,'total_rows')]"
    CONFIGURATION_INPUT = '//input[@aria-label="Skip to row"]'
    CONFIGURATION_ITEM_ROW = (By.XPATH,"//tr[contains(@id,'row_cmdb_ci')]//a")
    PROBLEM_STATEMENT = '//*[@id="problem.short_description"]'
    TICKET_STATE = "//*[@id='sys_readonly.problem.state']/option[@selected='SELECTED']"
    ASSIGNED_TO ='//*[@id="sys_display.problem.assigned_to"]'
    SUBMIT_BUTTON = (By.XPATH,"//div[@class='form_action_button_container']//button[@type='submit']")

    # --- All Problems Page ---

    SEARCH_ICON = (By.XPATH,'//*[@id="hdr_problem"]//button')
    SEARCH_ICON_ATTRIBUTE = "return document.getElementsByClassName('icon-search')[0].getAttribute('aria-expanded');"
    SEARCH_BOX = "//td[@name='short_description']//input[@type='search']"
    RESULT_ROW = "//table[@id = 'problem_table']//tr[contains(@id,'row_problem')]"
    RESULT_PRB_STMT = "//tr[contains(@id,'row_problem')]/td[4]"
    USER_DROPDOWN = (By.XPATH,"//button[@id='user_info_dropdown']")

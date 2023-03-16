from pageobj.base_page import BasePage
from selenium.webdriver.common.by import By
import time
import config.config as confi
import pyautogui
class HomePage(BasePage):

    pipline_menu = (By.XPATH, "//span[text()='Pipelines']")
    create_pipeline = (By.XPATH, " //*[text()=' Create Pipeline ']")
    search_source = (By.XPATH, "//input[@placeholder='Search Source Types']")
    source_host=(By.XPATH,"//input[@name='db-host']")
    source_port=(By.XPATH,"//input[@name='db-port']")
    source_Admin=(By.XPATH,"//input[@name='db-admin']")
    source_password=(By.XPATH,"//input[@name='db-password']")
    show_more = (By.XPATH, "//div[text()='Select an Ingestion Mode']/following::button[1]")
    table_radio=(By.XPATH,"//input[@value='table']/..")
    source_database=(By.XPATH,"//input[@name='db-name']")
    test_continue = (By.XPATH, "//button[text()=' Test & Continue ']")
    click_mysql=(By.XPATH, "//div[text()=' MySQL ']")
    #select object in pipline
    continue_object = (By.XPATH, "//button[text() = 'Continue']")
    timestamp_column = (By.XPATH, "//input[@placeholder = 'Timestamp Column']")
    lastmodified = (By.XPATH, "//span[text() = 'last_modified']")
    contains_continue=(By.XPATH, "//button[contains(text(), 'Continue')]")

    dst_search = (By.XPATH, "//input[@class='search-box']")
    select_dist_db = (By.XPATH, "//*[contains(text(),'MySQL Destination')]")
    prefix_locator = (By.XPATH, "//input[@name='destination-prefix']")
    json_continue = (By.XPATH, "//button[@class='submit-btn btn btn-primary']")
    destination_menu = (By.XPATH, "//span[text()='Destinations']")
    open_dest_setup = (
    By.XPATH, "//div[contains(text(),' MySQL Destination ')]/following::div[1][contains(text(),'MySQL')]")
    workbench_locator = (By.XPATH, "//a[@routerlink='./workbench']")
    pre_ele = (By.XPATH, "//pre[@class=' CodeMirror-line ']")
    run_query = (By.XPATH, "//button[contains(text(),' Run Query ')]")
    piplinenew_menu = (By.XPATH, "//span[text()='Pipelines']")
    expand_arrow = (By.XPATH, "//span[text()=' Active ']/../../following::hd-icon[1]")
    threedot = (By.XPATH, "//span[text()=' Active ']/../../following::div[1]/button")
    delete_pip = (By.XPATH, "//*[contains(text(),' Delete')]")
    confirm_delete = (By.XPATH, "//span[text()=' Active ']/../../following::hd-icon[1]")

    def __init__(self, driver):
        super().__init__(driver)


    def configure_source(self):
        self.click(self.pipline_menu)
        self.click(self.create_pipeline)
        self.type(self.search_source,"MySQL")
        self.click(self.click_mysql)
        self.type(self.source_host,confi.host)
        self.type(self.source_port,confi.port)
        self.type(self.source_Admin,confi.ad_username)
        self.type(self.source_password,confi.ad_password)
        time.sleep(3)
        self.javascript_click(self.show_more)
        time.sleep(3)
        self.javascript_click(self.table_radio)
        self.type(self.source_database,confi.database)
        self.click(self.test_continue)
        self.verify_page_should_contain(confi.object_screen)

    def select_object_in_pipline(self):
        self.click(self.continue_object)
        self.click(self.timestamp_column)
        self.click(self.lastmodified)
        self.click(self.contains_continue)
        self.verify_page_should_contain(confi.destination_page)


    def configure_destination(self):
        self.type(self.dst_search,confi.destination_db_name)
        self.click(self.select_dist_db)
        self.type(self.prefix_locator,confi.prefix)
        self.click(self.json_continue)
        time.sleep(15)
        self.verify_page_should_contain(confi.final_screen)

    def fetch_data_from_destination_database(self, name):
        self.click(self.destination_menu)
        self.click(self.open_dest_setup)
        self.click(self.workbench_locator)
        self.click(self.pre_ele)
        time.sleep(5)
        pyautogui.typewrite(confi.db_fetch_query)
        time.sleep(5)
        self.click(self.run_query)
        self.screenshot(name)

    def delete_hevo_pipline(self):
        self.click(self.piplinenew_menu)
        self.click(self.expand_arrow)
        self.click(self.threedot)
        self.click(self.delete_pip)
        self.click(self.confirm_delete)
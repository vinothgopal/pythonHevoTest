from pageobj.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class LoginPage(BasePage):

    USERNAME_FIELD = (By.XPATH, "//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    CLOSE_TOUR=(By.XPATH,"//*[@data-id='product-tour-close-icon-button']")
    accout_dropdown=(By.XPATH,"//*[@name='dropdown-arrow']")
    logout_button=(By.XPATH," //*[contains(text(),'Log out')]")


    def __init__(self, driver):
        super().__init__(driver)


    def login(self, username, password):
        self.type(self.USERNAME_FIELD, username)
        self.click(self.SUBMIT_BUTTON)
        time.sleep(5)
        self.type(self.PASSWORD_FIELD, password)
        self.click(self.SUBMIT_BUTTON)
        time.sleep(5)
        self.click_and_ignore_error(self.CLOSE_TOUR)
        self.verify_page_should_contain(username)

    def logout(self):
        self.click(self.accout_dropdown)
        self.click(self.logout_button)
        self.close_browser()
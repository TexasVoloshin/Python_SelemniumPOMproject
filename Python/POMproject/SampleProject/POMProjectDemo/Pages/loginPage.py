from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from SampleProject.POMProjectDemo.Config.config import TestData
from SampleProject.POMProjectDemo.Pages.basePage import BasePage
from SampleProject.POMProjectDemo.Locators.locators import Locators
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    """Constructo of the page class"""
    url = None
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_id = Locators.login_button_id
        self.invalid_credentials_xpath = "//span[@id='spanMessage']"
        self.forgot_password_link_xpath = "//div/div[@id='forgotPasswordLink']/a[text()='Forgot your password?']"
        self.welcom_menu = Locators.welcome_link_xpath
    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def check_invalid_username_message(self):
        msg = self.driver.find_element_by_xpath(self.invalid_credentials_xpath).text
        return msg

    def go(self):
        self.driver.get(self.url)

    def click_forgot_password_link(self):
        self.driver.find_element_by_xpath(self.forgot_password_link_xpath).click()

    def check_forgot_password_page_open(self):
        fp_url = "https://opensource-demo.orangehrmlive.com/index.php/auth/requestPasswordResetCode"
        return fp_url


    def welcome_menu_exist(self):
        self.driver.find_element_by_xpath(self.welcom_menu).is_displayed()



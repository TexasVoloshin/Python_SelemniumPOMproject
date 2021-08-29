import HtmlTestRunner
import time
import unittest
from SampleProject.POMProjectDemo.Pages.loginPage import LoginPage
from SampleProject.POMProjectDemo.Pages.homePage import HomePage
from SampleProject.POMProjectDemo.Pages.basePage import BasePage
from SampleProject.POMProjectDemo.Config.config import TestData
from SampleProject.POMProjectDemo.Tests.test_base import BaseTest

class TestLogin(BaseTest):

    def test_01_login_valid(self):
        self.login = LoginPage(self.driver)
        self.login.enter_username(TestData.USER_NAME)
        self.login.enter_password(TestData.PASSWORD)
        self.login.click_login()

        self.homePage = HomePage(self.driver)
        self.homePage.click_welcome()
        self.homePage.click_logout()

        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
        # self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text("Logout").click()

    def test_02_login_invalid_password(self):
        self.login = LoginPage(self.driver)
        self.login.enter_username(TestData.USER_NAME)
        self.login.enter_password("admin120")
        self.login.click_login()
        message = self.driver.find_element_by_xpath(self.login.invalid_credentials_xpath).text
        assert message == "Invalid credentials"


    def test_03_forgot_password_link(self):
        fp_url = "https://opensource-demo.orangehrmlive.com/index.php/auth/requestPasswordResetCode"
        self.login = LoginPage(self.driver)
        self.login.click_forgot_password_link()
        current_url = (self.driver.current_url)
        assert current_url == fp_url
        time.sleep(5)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.LoginPage.driver.close()
    #     print("Test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Python/POMproject/reports'))

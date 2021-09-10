from SampleProject.POMProjectDemo.Config.config import TestData
from SampleProject.POMProjectDemo.Pages.forgotYourPasswordPage import ForotYuorPasswordPage
from SampleProject.POMProjectDemo.Tests.test_base import BaseTest
import time

class TestForgotPassword(BaseTest):

    def test_01_input_user_name(self):
        self.forgotPassword = ForotYuorPasswordPage(self.driver)
        self.forgotPassword.enter_username_input.input_text(TestData.USER_NAME)
        self.forgotPassword.reset_password_button.click()
        msg = self.forgotPassword.HR_warning_message()
        assert msg == "There is a password reset request already in the system.\nClose"

    def test_02_input_nonexisitng_user_name(self):
        self.forgotPassword = ForotYuorPasswordPage(self.driver)
        self.forgotPassword.enter_username_input.input_text("Admon33")
        self.forgotPassword.reset_password_button.click()
        msg = self.forgotPassword.HR_warning_message().text
        assert msg == "Please contact HR admin in order to reset the password\nClose"

    def test_03_cancel_reset_password(self):
        home_url = TestData.HOME_URL
        self.forgotPassword = ForotYuorPasswordPage(self.driver)
        self.forgotPassword.cancel_button.click()
        current_url = (self.driver.current_url)
        assert current_url == home_url
        time.sleep(2)






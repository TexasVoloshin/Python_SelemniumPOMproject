
from SampleProject.POMProjectDemo.Config.config import TestData
from SampleProject.POMProjectDemo.Pages.baseElement import BaseElement
from SampleProject.POMProjectDemo.Pages.basePage import BasePage
from SampleProject.POMProjectDemo.Locators.locators import Locator
from SampleProject.POMProjectDemo.Locators.locators import Locators
from selenium.webdriver.common.by import By


class ForotYuorPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.FORGOT_PASSWORD_URL)


    @property
    def enter_username_input(self):
        locator = Locator(By.CSS_SELECTOR, Locators.reset_username_input)
        return BaseElement(self.driver, locator=locator)

    @property
    def reset_password_button(self):
        locator = Locator(By.CSS_SELECTOR, Locators.reset_password_btn_id)
        return BaseElement(self.driver, locator=locator)

    @property
    def cancel_button(self):
        locator = Locator(By.CSS_SELECTOR, Locators.cancel_button_id)
        return BaseElement(self.driver, locator=locator)

    def HR_warning_message(self):
        locator = Locator(By. XPATH, Locators.HR_warning_message)
        return BaseElement(self.driver, locator=locator)



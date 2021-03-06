from selenium.webdriver.common.by import By

from SampleProject.POMProjectDemo.Config.config import TestData
from SampleProject.POMProjectDemo.Locators.locators import Locators
from SampleProject.POMProjectDemo.Locators.locators import Locator

from SampleProject.POMProjectDemo.Pages.baseElement import BaseElement
from SampleProject.POMProjectDemo.Pages.basePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.HOME_URL)

        self.welcome_link_xpath = Locators.welcome_link_xpath
        self.logout_link_xpath = Locators.logout_link_xpath


    def click_welcome(self):
        self.driver.find_element_by_xpath(self.welcome_link_xpath).click()

    def click_logout(self):
        #self.driver.find_element_by_xpath(self.logout_link_xpath).click()
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.logout_link_xpath)))
        self.driver.execute_script("arguments[0].click();", element)






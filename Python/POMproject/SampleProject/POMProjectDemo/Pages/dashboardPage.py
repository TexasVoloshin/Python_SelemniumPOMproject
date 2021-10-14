from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SampleProject.POMProjectDemo.Config.config import TestData
from SampleProject.POMProjectDemo.Pages.baseElement import BaseElement
from SampleProject.POMProjectDemo.Pages.basePage import BasePage
from SampleProject.POMProjectDemo.Locators.locators import Locator
from SampleProject.POMProjectDemo.Locators.locators import Locators
from selenium.webdriver.common.by import By


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.DASHBOARD)

        self.dashboard_title = Locators.dashboard_title_text
        self.dics_values = list(Locators.dashboard_titles_dict)
        self.ql_images = Locators.quick_lounch_image_xpath



    def get_element_text(self,dic_value):
        title = self.dics_values[dic_value]
        locator = Locator(By.XPATH, Locators.dashboard_titles_dict[title])
        return BaseElement(self.driver, locator=locator)

    def get_quick_lounch_table_elements(self):
        locator = Locator(By.CLASS_NAME, 'quickLaungeContainer')
        return BaseElement(self.driver, locator=locator)



    def quick_launch_image_exist(self):
        image_table = self.driver.find_element_by_class_name("quickLaungeContainer")
        table_element = image_table.find_elements_by_class_name('quickLinkText')
        imq_names = []
        for image in table_element:
            el=image.text

        imq_names += el

        return imq_names
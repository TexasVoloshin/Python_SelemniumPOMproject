from SampleProject.POMProjectDemo.Config.config import TestData
from SampleProject.POMProjectDemo.Locators.locators import Locators
from SampleProject.POMProjectDemo.Pages.dashboardPage import DashboardPage
from SampleProject.POMProjectDemo.Pages.homePage import HomePage
from SampleProject.POMProjectDemo.Pages.loginPage import LoginPage
from SampleProject.POMProjectDemo.Tests.test_base import BaseTest
from selenium.webdriver.common.by import By
import pytest
import time

class TestDashboard(BaseTest):


    WELCOME = (By.XPATH,Locators.welcome_link_xpath)
    def test_valid_login_setup(self):
        self.login = LoginPage(self.driver)
        self.login.enter_username(TestData.USER_NAME)
        self.login.enter_password(TestData.PASSWORD)
        self.login.click_login()
        self.login.welcome_menu_exist()

    @pytest.mark.depends(on=['test_valid_login_setup'])
    def test_01_dashboard_title_displayed(self):

         self.dashboardPage = DashboardPage(self.driver)
         h1  = self.dashboardPage.get_element_text(0).text
         assert h1 == "Dashboard"

    @pytest.mark.depends(on=['test_valid_login_setup'])
    def test_02_quicklaunch_title_displayed(self):

         self.dashboardPage = DashboardPage(self.driver)
         h2  = self.dashboardPage.get_element_text(1).text
         assert h2 == "Quick Launch"

    @pytest.mark.depends(on=['test_valid_login_setup'])
    def test_03_quicklaunch_title_displayed(self):
        self.dashboardPage = DashboardPage(self.driver)
        actual_img_list = self.dashboardPage.quick_launch_image_exist()
        expected_img_list = ["Assign Leave","Leave List", "Timesheets", "Apply Leave", "My Leave", "My Timesheet"]
        assert actual_img_list.sort() == expected_img_list.sort()

    @pytest.mark.depends(on=['test_valid_login_setup'])
    def test_04_emp_distribution_by_subunit_title_displayed(self):
        self.dashboardPage = DashboardPage(self.driver)
        h3 = self.dashboardPage.get_element_text(2).text
        assert h3 == "Employee Distribution by Subunit"

    @pytest.mark.depends(on=['test_valid_login_setup'])
    def test_05_legend_title_displayed(self):
        self.dashboardPage = DashboardPage(self.driver)
        h4 = self.dashboardPage.get_element_text(3).text
        assert h4 == "Legend"


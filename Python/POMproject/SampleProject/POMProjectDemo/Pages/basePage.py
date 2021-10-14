import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SampleProject.POMProjectDemo.Locators.locators import Locator
from SampleProject.POMProjectDemo.Locators.locators import Locators
from selenium.webdriver.common.by import By



class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.web_element = None





    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def do_elenment_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).text
        return bool(element)

    def find(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator=self.locator)
        )
        self.web_element = element
        return None


    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))




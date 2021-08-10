from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/training-ground")
button4_xpath_locator="//button[@id='b4']"
button4_elem = browser.find_element_by_xpath(button4_xpath_locator)
alert = Alert(browser)
button4_elem.click()
print("button clicked!!!")
WebDriverWait(browser,5).until(alert_is_present())
print("Alert appeard!!!")
#is_disappeared = WebDriverWait(browser, 30, 1, (ElementNotVisibleException)).\

#            until_not(lambda x: x.find_element(By.ID, "someId").is_displayed())
print(alert.text)
time.sleep(3)
alert.accept()
#time.sleep(5)

sel = browser.find_elements_by_id('sel1')
my_select = Select(sel[0])
options = [elem.text for elem in my_select.options]
print(options)

my_select.select_by_visible_text("Battlestar Galactica")
time.sleep(2)
my_select.select_by_index(0)
time.sleep(5)
my_select.select_by_value('second')
time.sleep(5)
browser.close()


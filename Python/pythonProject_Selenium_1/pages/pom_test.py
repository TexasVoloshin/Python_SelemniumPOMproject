from selenium import webdriver
from pages.training_ground import TrainigGround

#TestSetup
browser = webdriver.Chrome()
test_value = 'it worked'

#Test
trng_page = TrainigGround(driver=browser)
trng_page.go()
#
assert trng_page.button1.text == 'Button1'
trng_page.button1.click()
browser.quit()

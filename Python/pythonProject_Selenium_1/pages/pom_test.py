from selenium import webdriver
from pages.training_ground import TrainigGround

#TestSetup
browser = webdriver.Chrome()
test_value = 'it worked'

#Test
trng_page = TrainigGround(driver=browser)
trng_page.go()
trng_page.button1.click()

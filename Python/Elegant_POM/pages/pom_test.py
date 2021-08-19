from selenium import webdriver

from pages.training_ground import TrainigGround
from pages.trail_page import TrialPage
from selenium import webdriver
from pages.training_ground import TrainigGround

#Test Setup
browser = webdriver.Chrome()

# Trial Page
trial_page = TrialPage(driver=browser)
trial_page.go()
trial_page.stone_input.input_text("rock")
trial_page.stone_button.click()



# Training Grounds
trng_page = TrainigGround(driver=browser)
trng_page.go()
assert trng_page.button1.text == 'Button1', "Unexpected button1 text"
print("All worked")

browser.quit()
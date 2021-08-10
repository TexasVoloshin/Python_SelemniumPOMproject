from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/trial-of-the-stones")

stone_input = browser.find_elements_by_id('r1Input')
stone_btton = browser.find_element_by_css_selector("button#r1Btn")

stone_result = browser.find_element_by_css_selector(
    "div#passwordBanner > h4"
)

secrets_input = browser.find_element_by_css_selector(
    "input[id = 'r2Input']"
)
secrets_anserw_btn = browser.find_element_by_css_selector(
    "button#r2Butn"
)

#
#Simple approach
richest_merchant_name = browser.find_element_by_xpath(
    "//p[text()='3000']/../span"
).text
marchant_input = browser.find_elements_by_id(
    'r3Input'
)
marchant_anserw_butn = browser.find_element_by_css_selector(
    "button#r3Butn"
)
check_butn = browser.find_element_by_css_selector(
    "button[name='checkButn']"
)

complete_mcg = browser.find_element_by_css_selector(
    "div#trialCompleteBanner h4"
)

stone_input[0].send_keys("rock")
stone_btton.click()
secrets_anserw_btn.click()
password = stone_result.text

secrets_input.send_keys(password)
secrets_anserw_btn.click()

marchant_input[0].send_keys(richest_merchant_name)
marchant_anserw_butn.click()
check_butn.click()
print(complete_mcg.text)
assert complete_mcg.text == "Trial Complete"
print("testing successful")
browser.close()

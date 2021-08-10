from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/training-ground")
input2_css_locator = "input[id='ipt2']"
button4_xpath_locator="//button[@id='b4']"
#("//b[text()='Product 2']/../../p")[0].innerHTML

#Assiging elements
input2_element = browser.find_element_by_css_selector(input2_css_locator)
button4_elem = browser.find_element_by_xpath(button4_xpath_locator)

# Manipulation
input2_element.send_keys("Test text")
button4_elem.click()
browser.quit()
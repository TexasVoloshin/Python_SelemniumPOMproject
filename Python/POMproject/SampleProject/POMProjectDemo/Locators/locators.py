from collections import namedtuple

Locator = namedtuple('Locator', ['by', 'value'])



class Locators():
    #Restet password locators

    #login page locators
    username_textbox_id = "txtUsername"
    password_textbox_id = "txtPassword"
    login_button_id = "btnLogin"


    # home page locators
    welcome_link_id = "welcome"
    logout_link_xpath = "//div[@id='welcome-menu']/ul/li/a[text()='Logout']"
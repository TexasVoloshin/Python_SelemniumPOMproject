from collections import namedtuple

Locator = namedtuple('Locator', ['by', 'value'])



class Locators():
    #Restet password locators

    #login page locators
    username_textbox_id = "txtUsername"
    password_textbox_id = "txtPassword"
    login_button_id = "btnLogin"


    # home page locators
    welcome_link_xpath = "//div/a[@id='welcome']"
    logout_link_xpath = "//div[@id='welcome-menu']/ul/li/a[text()='Logout']"

    #forgot password page
    HR_warning_message = "//div[@class='message warning fadable']"
    cancel_button_id ='input#btnCancel'
    reset_password_btn_id = 'input#btnSearchValues'
    reset_username_input = 'input#securityAuthentication_userName'

    #Dashboard page

    dashboard_titles_dict = {
        'dashboard_title_text': '//div/h1[text()="Dashboard"]',
        'quick_launch_title_text': '//div/fieldset/legend[text()="Quick Launch"]',
        'emp_distribution_by_subunit_title': '//div/fieldset/legend[text()="Employee Distribution by Subunit"]',
        'legend_title' :  '//div/fieldset/legend[text()="Legend"]'

    }

    pie_legend_dict = {

        'yellow': 'Not assigned to Subunits',
        'blue' : 'Administration',
        'red': 'Client Services',
        'green' : 'Engineering',
        'purple' : 'Finance',
        'brown': 'Human Resources',
        'navy' : 'Sales & Marketing'
    }

    pie_label_id = "hover_div_graph_display_emp_distribution"
    quick_lounch_image_xpath = "//div/table/"


    dashboard_title_text = "//div/h1[text()='Dashboard']"
    quick_launch_title_text = "//div/fieldset/legend[text()='Quick Launch']"
    # assign_leave_icon =
    # leave_list_icon =
    # tiesheets_icon =
    # apply_leave_icon =
    # my_leave_icon =
    # my_timesheets_icon =

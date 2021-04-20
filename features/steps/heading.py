from selenium import webdriver
from behave import *


@given('Launch chrome browser')
def launch_browser(context):
    context.browser = webdriver.Chrome()


@when('Open Selenium Webdriver Tutorial page')
def open_tutorial_page(context):
    context.browser.get("https://www.techbeamers.com/selenium-webdriver-tutorial")


@then('Verify that the heading is present on page')
def verify_heading(context):
    heading = context.browser.find_element_by_class_name("page-header-title.clr").is_displayed()
    assert heading is True


@then('Close browser')
def close_browser(context):
    context.browser.close()

import sys
import os

from pages.LoginPage import LoginPage

from utils.logger import log_message

from behave import given, when, then
from selenium import webdriver
import allure


@given("the user is on the login page")
def step_user_on_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")
    context.login_page = LoginPage(context.driver)
    log_message("User is on the login page.")

@when("the user enters the valid credentials")
def step_user_enters_credentials(context):
    context.login_page.enter_username("standard_user")
    context.login_page.enter_password("secret_sauce")
    log_message("User entered valid credentials.")

@when("clicks the login button")
def step_user_clicks_login(context):
    context.login_page.click_login()
    log_message("User clicked login button.")

@then("user should be redirected to the Dashboard")
def step_user_redirected_to_dashboard(context):
    assert "inventory.html" in context.driver.current_url
    log_message("User logged in successfully and redirected to inventory.html")

    # Attach screenshot to allure report
    allure.attach(
    context.driver.get_screenshot_as_png(),
    name = "inventory-screenshot",
    attachment_type = allure.attachment_type.PNG
    )
    context.driver.quit()


import utils.test_utils as tu
from behave import *
from selenium.webdriver.common.by import By

@given('the {page} page is open')
def step_impl(context, page):
    url = tu.getUrl(page)
    context.browser.get(url)

@given('the user is not logged in')
def step_impl(context):
    print("WARNING: Implement validation for not logged in")
    pass

@when('the user log in with {credentials}')
def step_impl(context, credentials):
    username, password = tu.getCreds(credentials)
    context.browser.find_element(By.CSS_SELECTOR, "#user-name").send_keys(username)
    context.browser.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
    context.browser.find_element(By.CSS_SELECTOR, "#login-button").click()

@when('the user navigates to {page} page')
def step_impl(context, page):
    context.browser.get(tu.getUrl(page))

@then('the {page} page is shown')
def step_impl(context, page):
    actualResult   = context.browser.current_url 
    expectedResult = tu.getUrl(page)
    try:
        assert tu.match(actualResult, expectedResult)
    except AssertionError:
        raise AssertionError('Actual location "{}" is different from expected location "{}".'.format(actualResult, expectedResult))

@then('an {error} error is shown')
def step_impl(context, error):
    errorMessageContainer = context.browser.find_element(By.CSS_SELECTOR, ".error-message-container")
    actualResult   = errorMessageContainer.text
    expectedResult = tu.getError(error)
    try:
        assert errorMessageContainer.is_displayed()
    except AssertionError:
        raise AssertionError('Error message container is not displayed.')
    
    try:
        assert tu.match(actualResult, expectedResult)
    except AssertionError:
        raise AssertionError('Actual error message "{}" is different from expected error message "{}".'.format(actualResult, expectedResult))

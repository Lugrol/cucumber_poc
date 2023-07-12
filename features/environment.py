from behave import use_fixture
from selenium import webdriver

def launch_firefox(context):
    context.browser = webdriver.Firefox()
    yield context.browser
    context.browser.quit()

fixture_registry={ # Store the strategy definition
        "fixture.lauch.firefox": launch_firefox,
}

def before_tag(context, tag): # Use strategy defined by tag
    if tag.startswith("fixture."):
        return use_fixture(fixture_registry.get(tag), context)

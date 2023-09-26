import pytest
from selene.support.shared import browser


@pytest.fixture
def browser_settings(scope="function"):
    browser.config.window_width = 1920
    browser.config.window_height = 1000
    browser.open('https://google.com')
    yield
    browser.quit()

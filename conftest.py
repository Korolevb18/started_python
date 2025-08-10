import pytest
from selene import browser

@pytest.fixture()
def setting_browser():
    browser.config.window_width = 1200
    browser.config.window_height = 800
    browser.config.timeout = 10

    yield

    browser.quit()
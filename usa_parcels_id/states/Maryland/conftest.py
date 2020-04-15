import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def browser():
    options = Options()
    options.add_argument('--start-maximized')
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    yield browser
    browser.quit()

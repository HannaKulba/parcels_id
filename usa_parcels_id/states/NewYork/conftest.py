import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def browser():
    options = Options()
    options.add_argument('--start-maximized')
    options.add_experimental_option('prefs', {
        'download.default_directory': 'C:\\Users\\user\\Documents\\Python-projects\\python_cources_stepik\\usa_parcels_id\\databases',
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        'safebrowsing.enabled': True
    })
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    yield browser
    browser.quit()

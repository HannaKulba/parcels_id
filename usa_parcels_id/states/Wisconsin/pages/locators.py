from selenium.webdriver.common.by import By


class CountyPageLocators:
    table = (By.ID, 'tbody_downloads')
    table_links = (By.CSS_SELECTOR, 'td:nth-child(2) > a')
    popup = (By.CSS_SELECTOR, '.modal-footer > .btn.btn-primary')

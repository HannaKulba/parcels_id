from selenium.webdriver.common.by import By


class CountyPageLocators:
    pan = (By.CSS_SELECTOR, 'tbody td:nth-child(3)')
    next = (By.CSS_SELECTOR, 'a[aria-label="Next"]')

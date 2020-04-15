from usa_parcels_id.states.Maryland.pages.locators import CountyPageLocators
import time
from bs4 import BeautifulSoup
import requests


class MarylandPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.implicitly_wait(10)

    def open(self):
        state_url = 'https://data.imap.maryland.gov/datasets/maryland-property-data-parcel-points/data'
        self.browser.get(state_url)

    def get_parcel_account_number(self):
        time.sleep(5)
        pan_list = []
        parcels = self.browser.find_elements(*CountyPageLocators.pan)
        for elem in parcels:
            pan_list.append(elem.text)
        if len(parcels) == 10:
            next_button = self.browser.find_element(*CountyPageLocators.next)
            time.sleep(5)
            next_button.click()
        with open('../usa_parcels_id/states/Maryland/parcels/Maryland_parcels.csv', 'a+') as file:
            for p in pan_list:
                file.write(p + '\n')
        self.get_parcel_account_number()

    def write_to_file(self):
        self.get_parcel_account_number()
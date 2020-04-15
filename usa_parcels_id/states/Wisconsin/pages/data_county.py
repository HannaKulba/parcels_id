from usa_parcels_id.states.Wisconsin.pages.locators import CountyPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import usa_parcels_id.base_po.base_page as base
from os import listdir


class DataCounty:
    def __init__(self, browser):
        self.browser = browser
        self.browser.implicitly_wait(10)

    def open(self):
        state_url = 'https://www.sco.wisc.edu/parcels/data-county/#v500'
        self.browser.get(state_url)

    def close_popup(self):
        popup_button = self.browser.find_element(*CountyPageLocators.popup)
        popup_button.click()

    def wait_for_element_appeared(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
            print('Page is ready!')
        except TimeoutException:
            print('Loading took too much time!')

    def download_GIS_data(self):
        download_links = self.get_download_links()
        for elem in download_links:
            elem.click()
            time.sleep(7)

    def get_download_links(self):
        self.open()
        self.wait_for_element_appeared(*CountyPageLocators.popup)
        self.close_popup()
        download_links = self.browser.find_elements(*CountyPageLocators.table_links)
        return download_links

    def write_to_file(self):
        self.download_GIS_data()
        list_zip_files = '../usa_parcels_id/databases'
        zips = listdir(list_zip_files)
        for zip in zips:
            path_ro_zip = list_zip_files + '/' + zip
            county = zip.split('_')[3]
            state = 'Wisconsin'
            parcel_id = 'PARCELID'
            base.write_parcels_to_file(path_ro_zip, parcel_id, state, county)

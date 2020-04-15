from usa_parcels_id.states.Maine.pages.locators import MainePageLocators
import time
import usa_parcels_id.base_po.base_page as base
from os import listdir


class MainePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.implicitly_wait(10)

    def open(self):
        state_url = 'https://www.maine.gov/megis/catalog/parcels_tiles.shtml'
        self.browser.get(state_url)

    def download_GIS_data(self):
        download_links = self.get_download_links()
        for elem in download_links:
            elem.click()
            time.sleep(7)

    def get_download_links(self):
        self.open()
        download_links = self.browser.find_elements(*MainePageLocators.table_links)
        return download_links

    def write_to_file(self):
        self.download_GIS_data()
        list_zip_files = '../usa_parcels_id/databases'
        zips = listdir(list_zip_files)
        for zip in zips:
            path_ro_zip = list_zip_files + '/' + zip
            county = zip.split('_')[1].split('.')[0]
            state = 'Maine'
            parcel_id = 'STATE_ID'
            base.write_parcels_to_file(path_ro_zip, parcel_id, state, county)

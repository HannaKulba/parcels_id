from usa_parcels_id.states.NewYork.pages.locators import CountyPageLocators
import time
import usa_parcels_id.base_po.base_page as base
from os import listdir


class NewYorkPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.implicitly_wait(10)

    def open(self):
        state_url = 'http://gis.ny.gov/gisdata/inventories/details.cfm?DSID=1300'
        self.browser.get(state_url)

    def download_GIS_data(self):
        download_links = self.get_download_links()
        for i in range(2, len(download_links)):
            download_links[i].click()
            time.sleep(15)

    def get_download_links(self):
        self.open()
        download_links = self.browser.find_elements(*CountyPageLocators.table_links)
        return download_links

    def write_to_file(self):
        # self.download_GIS_data()
        list_zip_files = '../usa_parcels_id/databases'
        zips = listdir(list_zip_files)
        for zip in zips:
            path_ro_zip = list_zip_files + '/' + zip
            county = zip.split('.')[0]
            state = 'NewYork'
            swis = 'SWIS'
            print_key = 'PRINT_KEY'
            base.write_parcels_to_file_NY(path_ro_zip, swis, print_key, state, county)

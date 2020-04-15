import requests
from bs4 import BeautifulSoup
from usa_parcels_id.states.Wyoming.pages.counties import counties
import usa_parcels_id.base_po.base_page as base


class BigHornPage:
    def __init__(self):
        pass

    def download_GIS_data(self):
        country = counties['Big Horn']
        big_horn_mapserver_page = requests.get(country)
        soup = BeautifulSoup(big_horn_mapserver_page.text, 'html.parser')
        forms = soup.find_all('form')
        action_download = forms[1].get('action')
        download_GIS_data_page = requests.get(country + action_download)
        soup = BeautifulSoup(download_GIS_data_page.text, 'html.parser')
        page_title = soup.title.string
        path_to_zip = ''
        if page_title == 'Big Horn County, Wyoming GIS Data Download':
            url = country + action_download + 'parcel_ownership.zip'
            response = requests.get(url, allow_redirects=True)
            path_to_zip = '../usa_parcels_id/databases/big_horn_parcels.zip'
            open(path_to_zip, 'wb').write(response.content)
        return path_to_zip

    def write_parcels_to_file(self, county):
        state = 'Wyoming'
        parcel_id = 'pidn'
        path_to_zip = self.download_GIS_data()
        base.write_parcels_to_file(path_to_zip, parcel_id, state, county)

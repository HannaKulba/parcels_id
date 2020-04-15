import requests
from bs4 import BeautifulSoup
from usa_parcels_id.states.Wyoming.pages.counties import counties
import usa_parcels_id.base_po.base_page as base


class HotSpringsPage:
    def __init__(self):
        pass

    def download_GIS_data(self):
        country = counties['Hot Spring']
        hot_springs_mapserver_page = requests.get(country)
        soup = BeautifulSoup(hot_springs_mapserver_page.text, 'html.parser')
        forms = soup.find_all('form')
        action_download = forms[3].get('action')
        download_GIS_data_page = requests.get(country + action_download)
        soup = BeautifulSoup(download_GIS_data_page.text, 'html.parser')
        page_title = soup.title.string
        path_to_zip = ''
        if page_title == 'Hot Springs County Map Server':
            url = country + action_download + 'parcels.zip'
            response = requests.get(url, allow_redirects=True)
            path_to_zip = '../usa_parcels_id/databases/hot_springs_parcels.zip'
            open(path_to_zip, 'wb').write(response.content)
        return path_to_zip

    def write_parcels_to_file(self, county):
        state = 'Wyoming'
        parcel_id = 'pidn'
        path_to_zip = self.download_GIS_data()
        base.write_parcels_to_file(path_to_zip, parcel_id, state, county)

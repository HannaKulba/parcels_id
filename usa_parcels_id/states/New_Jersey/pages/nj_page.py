import usa_parcels_id.base_po.base_page as base
from os import listdir

class NJPage:
    def __init__(self):
        pass

    def write_to_file(self):
        list_zip_files = '../usa_parcels_id/databases'
        zips = listdir(list_zip_files)
        for zip in zips:
            path_ro_zip = list_zip_files + '/' + zip
            county = zip.split('_')[3].split('.')[0]
            state = 'New_Jersey'
            parcel_id = 'GIS_PIN'
            base.write_parcels_to_file(path_ro_zip, parcel_id, state, county)


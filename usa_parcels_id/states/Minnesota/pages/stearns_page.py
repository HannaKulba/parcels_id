import usa_parcels_id.base_po.base_page as base


class StearnsPage():
    def __init__(self):
        pass

    def write_to_file(self):
        path_to_zip = '../usa_parcels_id/databases/parcels.zip'
        parcel_id = 'PARCEL'
        state = 'Minnesota'
        county = 'Stearns'
        base.write_parcels_to_file_2(path_to_zip, parcel_id, state, county)

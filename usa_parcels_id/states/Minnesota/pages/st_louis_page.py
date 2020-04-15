import usa_parcels_id.base_po.base_page as base


class StLouisPage():
    def __init__(self):
        pass

    def write_to_file(self):
        path_to_zip = '../usa_parcels_id/databases/Parcels_Saint_Louis_County_MN.zip'
        parcel_id = 'PRCL_NBR'
        state = 'Minnesota'
        county = 'St. Louis'
        base.write_parcels_to_file(path_to_zip, parcel_id, state, county)

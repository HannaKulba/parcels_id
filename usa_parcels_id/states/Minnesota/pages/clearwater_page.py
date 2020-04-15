import usa_parcels_id.base_po.base_page as base


class ClearWaterPage():
    def __init__(self):
        pass

    def write_to_file(self):
        path_to_zip = '../usa_parcels_id/databases/County_Parcels.zip'
        parcel_id = 'PARCEL_ID'
        state = 'Minnesota'
        county = 'Clearwater'
        base.write_parcels_to_file(path_to_zip, parcel_id, state, county)

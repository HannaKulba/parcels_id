import usa_parcels_id.base_po.base_page as base


class BigStonePage():
    def __init__(self):
        pass

    def write_to_file(self):
        path_to_zip = '../usa_parcels_id/databases/Tax_Parcels.zip'
        parcel_id = 'PARCEL_NUM'
        state = 'Minnesota'
        county = 'Big Stone'
        base.write_parcels_to_file(path_to_zip, parcel_id, state, county)

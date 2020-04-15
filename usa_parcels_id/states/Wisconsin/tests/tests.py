from usa_parcels_id.states.Wisconsin.pages.data_county import DataCounty


def test_country(browser):
    page = DataCounty(browser)
    page.write_to_file()

from usa_parcels_id.states.New_Jersey.pages.nj_page import NJPage


def test_nj_counties():
    page = NJPage()
    page.write_to_file()

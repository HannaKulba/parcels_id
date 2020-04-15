from usa_parcels_id.states.Maine.pages.maine_page import MainePage


def test_country(browser):
    page = MainePage(browser)
    page.write_to_file()

from usa_parcels_id.states.Maryland.pages.maryland_page import MarylandPage


def test_country(browser):
    page = MarylandPage(browser)
    page.open()
    page.get_parcel_account_number()

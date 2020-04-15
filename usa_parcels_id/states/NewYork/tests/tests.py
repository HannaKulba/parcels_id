from usa_parcels_id.states.NewYork.pages.new_york_page import NewYorkPage


def test_country(browser):
    page = NewYorkPage(browser)
    page.write_to_file()

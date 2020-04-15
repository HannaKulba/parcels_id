from usa_parcels_id.states.Wyoming.pages.big_horn_page import BigHornPage
from usa_parcels_id.states.Wyoming.pages.hot_springs_page import HotSpringsPage
from usa_parcels_id.states.Wyoming.pages.converse_page import ConversePage


def test_big_horn():
    BigHornPage().write_parcels_to_file('Big Horn')


def test_hot_springs():
    HotSpringsPage().write_parcels_to_file('Hot Springs')


def test_converse():
    ConversePage().write_parcels_to_file('Converse')

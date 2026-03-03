import pytest
from dash.testing.application_runners import import_app


# --------------------------
# Test 1: Header is present
# --------------------------
def test_header_is_present(dash_duo):
    app = import_app("app")     # import Dash app from app.py
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert "Soul Foods Pink Morsel Sales Visualiser" in header.text


# --------------------------
# Test 2: Graph is present
# --------------------------
def test_graph_is_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-graph")
    assert graph is not None


# --------------------------
# Test 3: Region picker is present
# --------------------------
def test_region_picker_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    radio = dash_duo.find_element("#region-filter")
    assert radio is not None
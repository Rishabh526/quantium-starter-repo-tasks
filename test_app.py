from main import app
from dash import html, dcc


def test_header_present():
    header = app.layout.children[0]

    assert isinstance(header, html.H1)
    assert header.id == "header"


def test_visualization_present():
    graph = app.layout.children[4]

    assert isinstance(graph, dcc.Graph)
    assert graph.id == "sales-graph"


def test_region_picker_present():
    radio = app.layout.children[3]

    assert isinstance(radio, dcc.RadioItems)
    assert radio.id == "region-filter"
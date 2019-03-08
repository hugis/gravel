from datetime import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


ax = [
    datetime(2019, 3, 3, 3, 1, 1),
    datetime(2019, 3, 3, 3, 1, 2),
    datetime(2019, 3, 3, 3, 1, 3),
    datetime(2019, 3, 3, 3, 1, 4),
    datetime(2019, 3, 3, 3, 1, 5),
    datetime(2019, 3, 3, 3, 1, 6),
]

trace1 = go.Scatter(x=ax, y=[4, 1, 2])


app.layout = html.Div(children=[
    html.H1(children="Graviton Elektromer"),
    html.Div(children="Ukážka zobrazenia údajov"),

    dcc.Graph(
        id="example-graph",
        figure={
            "data": [
                {"x": ax, "y": [4, 1, 2, 1, 4], "name": "Fáza 1"},
                {"x": ax, "y": [2, 4, 5, 4, 2], "name": "Fáza 2"},
                {"x": ax, "y": [3, 3, 3, 3, 3], "name": "Fáza 3"},
            ],
            "layout": {
                "title": "Zariadenie 1"
            }
        }
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)

import os
from typing import List

import dash
import dash_core_components as dcc
import dash_html_components as html
import flask

from db import Value, Session


server = flask.Flask(__name__)
server.secret_key = os.environ.get("SECRET_KEY", "5l0Q6fqu")


external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, server=server, external_stylesheets=external_stylesheets)

session = Session()
data: List[Value] = session.query(Value).order_by(Value.timestamp)[1:1000]

ax = [d.timestamp for d in data]


app.layout = html.Div(children=[
    html.H1(children="Graviton Elektromer"),
    html.Div(children="Ukážka zobrazenia údajov"),

    dcc.Graph(
        id="example-graph",
        figure={
            "data": [
                {"x": ax, "y": [d.u_1 for d in data], "name": "Fáza 1"},
                {"x": ax, "y": [d.u_2 for d in data], "name": "Fáza 2"},
                {"x": ax, "y": [d.u_3 for d in data], "name": "Fáza 3"},
            ],
            "layout": {
                "title": "Zariadenie 1"
            }
        }
    )
])

if __name__ == "__main__":
    app.run_server()

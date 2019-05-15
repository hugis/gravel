import os
from typing import List

import dash
import dash_core_components as dcc
import dash_html_components as html
import flask
from sqlalchemy import text

from db import Value, Session


server = flask.Flask(__name__)
server.secret_key = os.environ.get("SECRET_KEY", "5l0Q6fqu")


external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, server=server, external_stylesheets=external_stylesheets)

session = Session()
data: List[Value] = session.query(Value).filter(
    text("val_dev_id = 1 AND val_timestamp > NOW() - INTERVAL '30 minutes'")
).order_by(Value.timestamp)

ax = [d.timestamp for d in data]


app.layout = html.Div(
    children=[
        html.H1(children="Graviton Elektromer"),
        html.Div(children="Ukážka zobrazenia údajov"),
        dcc.Graph(
            id="example-graph",
            figure={
                "data": [
                    {"x": ax, "y": [d.u_1 for d in data], "name": "Fáza 1 - U [V]"},
                    {"x": ax, "y": [d.u_2 for d in data], "name": "Fáza 2 - U [V]"},
                    {"x": ax, "y": [d.u_3 for d in data], "name": "Fáza 3 - U [V]"},
                ],
                "layout": {"title": "Zariadenie 1"},
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server()

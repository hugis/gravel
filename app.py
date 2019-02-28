import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children="Graviton Elektromer"),
    html.Div(children="Ukážka zobrazenia údajov"),

    dcc.Graph(
        id="example-graph",
        figure={
            "data": [
                {"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "Fáza 1"},
                {"x": [1, 2, 3], "y": [2, 4, 5], "type": "bar", "name": "Fáza 2"},
                {"x": [1, 2, 3], "y": [3, 3, 3], "type": "bar", "name": "Fáza 3"},
            ],
            "layout": {
                "title": "Zariadenie 1"
            }
        }
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)

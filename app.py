from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app.layout = [html.Div(children='Hello World')]







#start app
if __name__ == '__main__':
    app.run(debug=True)


# Imports libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import dash
import pandas as pd
import numpy as np
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__)

app.layout = html.Div(html.Img(src=app.get_asset_url('CRIMEPREDICTIONBANNER.png')))
# Import application
from app import app

# Column layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predict Crime in Chicago 
            """
        ),
        # dcc.Link(dbc.Button('Predict Crime', color='primary'), href='/predictions')
    ],
    md=4,
)



column2 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            We have selected this topic to determine what correlation certain weather patterns have on violent crimes committed within Chicago. 
            
            Utilizing advanced machine learning models, let our interactive analysis determine potential crime by Date, Temperature, and Neighborhood within chicago.
            
            Our analysis could be useful for a wide range of purpose; from those seeking potential vacation travel to Chicago, to law 
            enforcement better equipped to forecast violent crime within their precinct. 
            """
        ),
        dcc.Link(dbc.Button('Predict Crime', color='primary'), href='/predictions')
    ],
    md=4,
)


layout = dbc.Row([column1, column2])
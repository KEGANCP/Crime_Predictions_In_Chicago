# Import libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## GitHub
            Get more details from our repo at http://https://github.com/KEGANCP/Crime_Predictions_In_Chicago
            """
        ),

    ],
)

layout = dbc.Row([column1])

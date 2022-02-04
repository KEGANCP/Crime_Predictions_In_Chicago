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
            Get more details on our Crime Prediction process within our GitHub.
            """
        ),

    ],
)

column2 = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span('View our process here!', className='mr-2'), 
                    html.A(html.Button('GitHub', className='three columns'),
                        href='https://github.com/KEGANCP/Crime_Predictions_In_Chicago')
                ], 
                className='row'
               
            )
        )
    )
)

layout = dbc.Row([column1, column2])

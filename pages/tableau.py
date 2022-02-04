## Import libraries
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
        
            ## Tableau
            View our interactive Tableau Dashboard below. 
            """
        ),

    ],
)

column2 = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span('Chicago Crime & Weather Visualizations', className='mr-2'), 
#                     html.A(html.Button('VIEW!', className='three columns'),
#                         href='https://public.tableau.com/views/chicago_crime_story_2/ChicagoCrimeDashboard?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link')
                ], 
                className='lead'
               
            )
        )
    )
)

column3 = html.Div([
    html.A([
            html.Img(
                src='https://i.imgur.com/vt2qfJ4.png',
                style={
                    'height' : '100%',
                    'width' : '100%',
                    'float' : 'center',
                    'position' : 'relative',
                    'padding-top' : 0,
                    'padding-right' : 0
                })
    ], href='https://public.tableau.com/app/profile/austen.marden/viz/chicago_crime_story_2/ChicagoCrimeDashboard')
]) 



layout = dbc.Row([column1, column2, column3])

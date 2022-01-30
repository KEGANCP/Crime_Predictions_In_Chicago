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

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# crime_df = pd.read_csv('merged_data.csv', sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
# crime_df.head()
# s1 = crime_df[crime_df['Violence Status']=='VIOLENT']
# s2 = crime_df[crime_df['Violence Status']=='NON-VIOLENT']


# trace1 = go.Bar(    #setup the chart for VIOLENT records
#     x=s1["District"].unique(), #x for VIOLENT records
#     y=s1.groupby("District")["Violence Status"].value_counts(),#y for VIOLENT records
#     marker_color=px.colors.qualitative.Dark24[0],  #color
#     text=s1.groupby("District")["Violence Status"].value_counts(), #label/text
#     textposition="outside", #text position
#     name="VIOLENT", #legend name
# )
# trace2 = go.Bar(   #setup the chart for NON-VIOLENT records
#     x=s2["District"].unique(),
#     y=s2.groupby("District")["Violence Status"].value_counts(),
#     text=s2.groupby("District")["Violence Status"].value_counts(),
#     marker_color=px.colors.qualitative.Dark24[1],
#     textposition="outside",
#     name="NON-VIOLENT",
# )
# data = [trace1, trace2] #combine two charts/columns
# layout = go.Layout(barmode="group", title="VIOLENT vs NON-VIOLENT") #define how to display the columns
# fig3 = go.Figure(data=data, layout=layout)
# fig3.update_layout(
#     title=dict(x=0.5), #center the title
#     xaxis_title="District",#setup the x-axis title
#     yaxis_title="Violence Status", #setup the x-axis title
#     margin=dict(l=20, r=20, t=60, b=20),#setup the margin
#     paper_bgcolor="aliceblue", #setup the background color
# )
# fig3.update_traces(texttemplate="%{text:.2s}") #text formart

app = dash.Dash(__name__)

app.layout = html.Div(html.Img(src=app.get_asset_url('CRIMEPREDICTIONBANNER.png')))
# Import application
from app import app

# Column layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predict crime in Chicago 
            """
        ),
        # dcc.Link(dbc.Button('Predict Crime', color='primary'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2019"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            We have selected this topic to determine what correlation certain weather patterns have on violent crimes committed within Chicago. 
            Our analysis could be useful for a wide range of purpose; from those seeking potential vacation travel to Chicago, to law 
            enforcement better equipped to forecast violent crime within their precinct. 
            """
        ),
        dcc.Link(dbc.Button('Predict Crime', color='primary'), href='/predictions')
    ],
    md=4,
)


# column3 = dbc.Col( 
#     [
#         dcc.Markdown(
#             """
    
              
            
#             """
            
#         ),
    
#             dcc.Graph(
#                 id = 'bibar',
#                 figure = fig3,
#                 #config={"displayModeBar": False},
#             ),
#             # style={'width': '50%', 'display': 'inline-block'},
#     ],
#     md=4,
# )

layout = dbc.Row([column1, column2,])

# @app.callback(
#     Output("bibar", "figure"),
#     [Input("year-filter", "value")],
# )
# def update_charts(Year):
#     filtered_s1 = s1[s1["Year"] == Year]
#     filtered_s2 = s2[s2["Year"] == Year]
#     trace1 = go.Bar(
#         x=filtered_s1["District"].unique(),
#         y=filtered_s1.groupby("District")["Violence Status"].value_counts(),
#         text=filtered_s1.groupby("District")["Violence Status"].value_counts(),
#         textposition="outside",
#         marker_color=px.colors.qualitative.Dark24[0],
#         name="VIOLENT",
#     )
#     trace2 = go.Bar(
#         x=filtered_s2["District"].unique(),
#         y=filtered_s2.groupby("District")["Violence Status"].value_counts(),
#         text=filtered_s2.groupby("District")["Violence Status"].value_counts(),
#         textposition="outside",
#         marker_color=px.colors.qualitative.Dark24[1],
#         name="NON-VIOLENT",
#     )
#     data = [trace1, trace2]
#     layout = go.Layout(barmode="group", title="VIOLENT VS NON-VIOLENT")
#     bibar = go.Figure(data=data, layout=layout)
#     bibar.update_layout(
#         title=dict(x=0.5),
#         xaxis_title="District",
#         yaxis_title="Violence Status",
#         paper_bgcolor="aliceblue",
#         margin=dict(l=20, r=20, t=60, b=20),
#     )
#     bibar.update_traces(texttemplate="%{text:.2s}")
#     return bibar
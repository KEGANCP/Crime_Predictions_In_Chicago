# Import libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash import html
from dash.dependencies import Input, Output
import dash_daq as daq
import sklearn
import joblib
from joblib import load
# from sklearn.externals import joblib
import pandas as pd
from datetime import datetime as dt



# import pickle as pickle 
# import os
# # model = pickle.load(open('pipeline2.joblib', 'rb'))

# # filename = "pipeline2.joblib"
# # os.makedirs(os.path.dirname(filename), exist_ok=True)
# # predic = 'pipeline2.joblib'
# with open('assets/line2.joblib', 'rb') as f:
#     pipeline = pickle.load(f)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
import joblib
pipeline = joblib.load ('assets/feature_model.joblib')




# Import application
from app import app


markdown_text = '''
### Dash and Markdown



'''
# 2 column layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions
      
            """
        ),
                dcc.Markdown(
            """
    
            Select Date 
            
            """
        ),
            dcc.DatePickerSingle(
                id='date-picker-single',
                date=dt(2019, 1, 1),
                min_date_allowed=dt(2019, 1, 1),
                max_date_allowed=dt(2030, 1, 19),
                with_portal=True
            ),
            html.Br(),
        html.Br(),
        dcc.Markdown(
            """
    
            Select Chicago Neighborhood  
            
            """
            
        ),
        # html.Br(),
        dcc.Markdown(
            """
    
              
            
            """
            
        ),
                dcc.Dropdown(
                id='Community_Area',
                options=[
                    {'label': 'Rogers Park', 'value': '1'},
                    {'label': 'West Ridge', 'value': '2'},
                    {'label': 'Uptown', 'value': '3'},
                    {'label': 'Lincoln Square', 'value': '4'},
                    {'label': 'North Center', 'value': '5'},
                    {'label': 'Lakeview', 'value': '6'},
                    {'label': 'Lincoln Park', 'value': '7'},
                    {'label': 'Near North Side', 'value': '8'},
                    {'label': 'Edison Park', 'value': '9'},
                    {'label': 'Norwood Park', 'value': '10'},
                    {'label': 'Jefferson Park', 'value': '11'},
                    {'label': 'Forest Glen', 'value': '12'},
                    {'label': 'North Park', 'value': '13'},
                    {'label': 'Albany Park', 'value': '14'},
                    {'label': 'Portage Park', 'value': '15'},
                    {'label': 'Irving Park', 'value': '16'},
                    {'label': 'Dunning', 'value': '17'},
                    {'label': 'Montclaire', 'value': '18'},
                    {'label': 'Belmont Cragin', 'value': '19'},
                    {'label': 'Hermosa', 'value': '20'},
                    {'label': 'Avondale', 'value': '21'},
                    {'label': 'Logan Square', 'value': '22'},
                    {'label': 'Humboldt Park', 'value': '23'},
                    {'label': 'West Town', 'value': '24'},
                    {'label': 'Austin', 'value': '25'},
                    {'label': 'West Garfield Park', 'value': '26'},
                    {'label': 'East Garfield Park', 'value': '27'},
                    {'label': 'Near West Side', 'value': '28'},
                    {'label': 'North Lawndale', 'value': '29'},
                    {'label': 'South Lawndale', 'value': '30'},
                    {'label': 'Lower West Side', 'value': '31'},
                    {'label': 'Loop', 'value': '32'},
                    {'label': 'Near South Side', 'value': '33'},
                    {'label': 'Armour Square', 'value': '34'},
                    {'label': 'Douglas', 'value': '35'},
                    {'label': 'Oakland', 'value': '36'},
                    {'label': 'Fuller Park', 'value': '37'},
                    {'label': 'Grand Boulevard', 'value': '38'},
                    {'label': 'Kenwood', 'value': '39'},
                    {'label': 'Washington Park', 'value': '40'},
                    {'label': 'Hyde Park', 'value': '41'},
                    {'label': 'Woodlawn', 'value': '42'},
                    {'label': 'South Shore', 'value': '43'},
                    {'label': 'Chatham', 'value': '44'},
                    {'label': 'Avalon Park', 'value': '45'},
                    {'label': 'South Chicago', 'value': '46'},
                    {'label': 'Burnside', 'value': '47'},
                    {'label': 'Calumet Heights', 'value': '48'},
                    {'label': 'Roseland', 'value': '49'},
                    {'label': 'Pullman', 'value': '50'},
                    {'label': 'South Deering', 'value': '51'},
                    {'label': 'East Side', 'value': '52'},
                    {'label': 'West Pullman', 'value': '53'},
                    {'label': 'Riverdale', 'value': '54'},
                    {'label': 'Hegewisch', 'value': '55'},
                    {'label': 'Archer Heights', 'value': '57'},
                    {'label': 'Brighton Park', 'value': '58'},
                    {'label': 'McKinley Park', 'value': '59'},
                    {'label': 'Bridgeport', 'value': '60'},
                    {'label': 'New City', 'value': '61'},
                    {'label': 'West Elsdon', 'value': '62'},
                    {'label': 'Gage Park', 'value': '63'},
                    {'label': 'Clearing', 'value': '64'},
                    {'label': 'West Lawn', 'value': '65'},
                    {'label': 'Chicago Lawn', 'value': '66'},
                    {'label': 'West Englewood', 'value': '67'},
                    {'label': 'Englewood', 'value': '68'},
                    {'label': 'Greater Grand Crossing', 'value': '69'},
                    {'label': 'Ashburn', 'value': '70'},
                    {'label': 'Auburn Gresham', 'value': '71'},
                    {'label': 'Beverly', 'value': '72'},
                    {'label': 'Washington Height', 'value': '73'},
                    {'label': 'Mount Greenwood', 'value': '74'},
                    {'label': 'Morgan Park', 'value': '75'},
                    {'label': "O'hare", 'value': '76'},
                    {'label': 'Edgewater', 'value': '77'}
                ],
                value='66'
            ), 
            html.Br(), 






   
        dcc.Markdown(
            """
    
            Select temperature 
            
            """
            ),
            html.Br(),
            daq.Slider(
                id='Average_Temperature',
                min=-10,
                max=100,
                value=78,
                size=250,
                handleLabel={"showCurrentValue": True,"label": "Temperature"},
                step=1
            ),
            html.Br(),
    ],
    md=4,
)



column2 = dbc.Col(
    [
        dcc.Markdown(
            """
    
           
            
            """
            
        ),
        html.Br(),
        html.Br(),
    # html.Div(id='prediction-gauge', style={'marginTop': '2.2em'}),

        html.Br(),

    html.Div(id='prediction-label', className='lead mt-5', style={'fontWeight': 'bold', 'fontSize': '1px', 'position': 'relative', 'left': '180px', 'bottom': '82px'})
        
    ]
)

layout = dbc.Row([column1, column2])
@app.callback(
    Output('prediction-label', 'children'),
    [Input('Community_Area', 'value'),
    Input('Average_Temperature', 'value'),
    Input('date-picker-single', 'date')],
)

    
def predict (Community_Area,
             Average_Temperature,
             date_picked):
    # Convert the date from a string to a Timestamp

    assert type(date_picked) == str
    date_picked = pd.to_datetime(date_picked)
    assert type(date_picked) == pd.Timestamp
    # Extract the month, day, weekday
    Month = date_picked.month
    Day = date_picked.day
    Weekday = date_picked.dayofweek     # Construct a dateframe with all features
    df=pd.DataFrame(
        columns = ['Community_Area',
                   'Average_Temperature',
                   'Month',
                   'Day',
                   'Weekday'],
        data =[[Community_Area,
        Average_Temperature,
        Month,
        Day,
        Weekday]]
    )

    y_pred = pipeline.predict(df)[0]

    output1 = f'{y_pred:.0f}'
    
    
    output2 = daq.Gauge(id='my-daq-gauge',
                        showCurrentValue=True,
                        units="Crimes",
                        max=1000,
                        value=y_pred,
                        min=200,
                        color={"gradient":True,"ranges":{"teal":[200,500],"blue":[500,700],"magenta":[700,1000]}},
                        size=600)  
    return output1 , output2
# @app.callback(
#     dash.dependencies.Output('my-daq-gauge', 'value'),
#     [dash.dependencies.Input('prediction-content','children')]
# )
def update_output(value):
    return value

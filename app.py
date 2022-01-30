import dash
import dash_bootstrap_components as dbc


# Set theme. (We can change this) bootswatch.com to preview
external_stylesheets = [
    dbc.themes.SOLAR, # theme
]

meta_tags=[
    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)
app.config.suppress_callback_exceptions = True 
app.title = 'Crime Predictions in Chicago' # Browser Title
server = app.server
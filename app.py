"""
Web application initialization script
"""
import dash
import dash_bootstrap_components as dbc


# Insert your specified theme
external_stylesheets = [dbc.themes.LUX]

# Creating login credentials
#valid_login = {
#    str(os.environ.get('USER')): str(os.environ.get('PASS'))
#}

# Instantiate dash application
app = dash.Dash(
    __name__, external_stylesheets=external_stylesheets,
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1"
        }
    ]
)

# Implement authentication framework
#auth = da.BasicAuth(
#    app, valid_login
#)

server = app.server

# Application Title
app.title = 'APPLICATION TITLE'
app.config.suppress_callback_exceptions=True

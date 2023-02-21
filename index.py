"""
INDEX PAGE SCRIPT
"""
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from app import server
from app import app
from apps import explore
from dash.dependencies import Input, Output, State

LOGO_PATH = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

# building the navigation bar

nav_menu = dbc.Row(
    [
        dbc.Col(
        dbc.NavItem(
            dbc.NavLink(
                "Home", href='#', target='_blank',
                style={
                    'font-weight': 'bold', 'font-variant': 'small-caps',
                }
            )
        )),
        dbc.Col(
        dbc.NavItem(
            dbc.NavLink(
                "Explore", href='#', target='_blank',
                style={
                    'font-weight': 'bold', 'font-variant': 'small-caps',
                }
            )
        )),
        dbc.Col(dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem(
                    'ITEM 1', href='#',
                    target='_blank', style={
                        'font-weight': 'bold', 'font-variant': 'small-caps'
                    }
                ),
                dbc.DropdownMenuItem(
                    'ITEM 2', href='#',
                    target='_blank', style={
                        'font-weight': 'bold', 'font-variant': 'small-caps'
                    }
                )
            ],
            nav=True,
            in_navbar=True,
            label='Useful Links',
            style={
                'font-weight': 'bold', 'font-variant': 'small-caps'
            }
        )),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=LOGO_PATH, height="48px")),
                        dbc.Col(dbc.NavbarBrand("PAGE TITLE", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="#",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                nav_menu,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="primary",
    dark=True,
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)
# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname): 
    return explore.layout

if __name__ == "__main__":
    app.run_server(debug=True)


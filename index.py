
from dash import dcc
from dash import html
from dash.dependencies import Input, Output


# Connect to main app.py file
from app import app
import os

# Connect to your app pages
import dashboard


app.layout = html.Div([
    dcc.Location(id='url', refresh=False, pathname = '/apps/sales-dashboard'),
    html.Div([
        dcc.Link('Sales Dashboard|', href='/apps/sales-dashboard'),
        dcc.Link('Inventory Dashboard  |  ', href='/apps/inventory-dashboard'),
        dcc.Link('Upload Data', href='/apps/upload'),
        
    ], className="row"),
    html.Div(id='page-content', children=[])
])

app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 3000)))

@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/sales-dashboard':
        return dashboard.layout
    if pathname == '/apps/inventory-dashboard':
        return dashboard.layout2
    if pathname == '/apps/upload':
        return dashboard.layout3

    else:
        return "404 Page Error! Please choose a link"
    

if __name__ == '__main__':
    app.run_server(debug=False)
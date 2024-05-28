
from dash import dcc
from dash import html
from dash.dependencies import Input, Output


# Connect to main app.py file
from app import app
import os

# Connect to your app pages
from dashboard import( layout1, layout2, layout3
                                    )

# define tab styles
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}

# Create layout

layout_index = html.Div([
    
                html.Div([
                    
                html.Img(id="logo", src=app.get_asset_url("logo.png")),
                
                    html.Div([
                        html.H1('Kidsmart Sales and Inventory Monitoring Dashboard'),
                        html.P(
                            id="description",
                            children="† Please select dashboard from the tabs below. \
                            ",
                        ),
                                                
                    ],style={'display':'inline-block','margin-left':50}),
                            
                        ],
                        style={}),

    html.Div([
        dcc.Tabs(id='tabs', value='sales-dash', children=[
        dcc.Tab(label='Sales Dashboard', value='sales-dash',style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Inventory Dashboard', value='inventory-dash',style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Upload Data', value='upload-data',style=tab_style, selected_style=tab_selected_style),

        ]),
    
    ], style={}),
    html.Div(id='tabs-content', style={}),

])

url_bar_and_content_div = html.Div([
    
    dcc.Location(id='url', refresh=False),
    layout_index,
    html.Div(id='page-content')
])


app.layout = url_bar_and_content_div

app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 3000)))


# Tab callbacks
@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'sales-dash':
        return layout1
    elif tab == 'inventory-dash':
        return layout2
    elif tab == 'upload-data':   
        return layout3


if __name__ == '__main__':
    app.run_server(debug=False)
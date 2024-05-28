
from dash import dcc
from dash import html
from dash.dependencies import Input, Output


# Connect to main app.py file
from app import app
import os

# Connect to your app pages
import dashboard

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
# Create Pages
layout1 = html.Div(
    id="root",
    children=[
        html.Div(
            id="header",
            children=[
                
                html.H4(children="Sales Performance Dashboard"),
                html.P(
                    id="description",
                    children="† Retail Sales from inventory data by year, buyer region, and product type \
                    ",
                ),
            ],
        ),
        html.Div(
            id="app-container",
            children=[
                
                # start second graph
                html.Div(
                    id="graph-container",
                    children=[
                        
                        html.Div(
                            id="slider-container",
                            children=[
                                html.P(
                                    id="slider-text",
                                    children="Drag the slider to change the year:",
                                ),
                                dcc.Slider(
                                    id="years-slider",
                                    min=min(YEARS_INVENTORY),
                                    max=max(YEARS_INVENTORY),
                                    value=min(YEARS_INVENTORY),
                                    marks={
                                        str(year): {
                                            "label": str(year),
                                            "style": {"color": "#7fafdf"},
                                        }
                                        for year in YEARS_INVENTORY
                                    },
                                ),
                            ],
                        ),
                        
                        html.P(id="chart-selector",children="Select chart:"),
                        dcc.Dropdown(
                            options = [
                                {
                                    "label": "Total Sales",
                                    "value":"total_sales"
                                },
 
                                {
                                    "label": "Average Sales",
                                    "value":"avg_sales",
                                },

                                {
                                    "label": "Top Performers",
                                    "value":"top_performers",
                                },
                                {
                                    "label": "Bottom Performers",
                                    "value":"bottom_performers",
                                },

                                {
                                    "label": "Top Net Profit",
                                    "value":"top_avg_net_profit",
                                },
                                {
                                    "label": "Bottom Net Profit",
                                    "value":"bottom_avg_net_profit",
                                },
                                

                            ],
                            value = "total_sales",
                            id="chart-dropdown",
                            multi = False
                        ), # End Dropdown
                
                html.Div(className="row",
                    children=[
                    # Start changing graph
                        dcc.Graph(className="six columns",
                            id="selected-data",
                            figure = dict(
                                data=[dict(x=0, y=0)],
                                layout=dict(
                                    paper_bgcolor="#1f2630",
                                    plot_bgcolor="#1f2630",
                                    autofill=True,
                                    #margin=dict(t=75, r=50, b=100, l=50),
                                )
                            )

                        ), # end changing graph
                        
                # Start changing graph 2                      
                        dcc.Graph(className="six columns",
                            id="selected-data2",
                            figure = dict(
                                data=[dict(x=0, y=0)],
                                layout=dict(
                                    paper_bgcolor="#1f2630",
                                    plot_bgcolor="#1f2630",
                                    autofill=True,
                                    #margin=dict(t=75, r=50, b=100, l=50),
                                )
                            ) 

                        ) # end changing graph2
                        
                        ]
                        
                        ), # end div of graph1 and graph2
                
                # Start changing graph3
                        dcc.Graph(id="selected-data3",
                            figure = dict(
                                data=[dict(x=0, y=0)],
                                layout=dict(
                                    paper_bgcolor="#1f2630",
                                    plot_bgcolor="#1f2630",
                                    autofill=True,
                                    #margin=dict(t=75, r=50, b=100, l=50),
                                )
                            )

                        ), # end changing graph3
                    ],

                ),
                # end second graph

            ],
        ),
        
    ],
)


layout2 = html.Div(
    id="root",
    children=[
        html.Div(
            id="header",
            children=[
                html.Img(id="logo", src=app.get_asset_url("logo.png")),
                html.H4(children="Inventory Monitoring Dashboard"),
                html.P(
                    id="description",
                    children="† Inventory data and turnover rates based on sales data \
                    ",
                ),
            ],
        ),
            html.Div(
                            id="slider-container",
                            children=[
                                html.P(
                                    id="slider-text",
                                    children="Drag the slider to change the year:",
                                ),
                                dcc.Slider(
                                    id="years-slider",
                                    min=min(YEARS_INVENTORY),
                                    max=max(YEARS_INVENTORY),
                                    value=min(YEARS_INVENTORY),
                                    marks={
                                        str(year): {
                                            "label": str(year),
                                            "style": {"color": "#7fafdf"},
                                        }
                                        for year in YEARS_INVENTORY
                                    },
                                ),
                            ],
                        ),
        
        # START BOTTOM DIV 1 
        html.Div(
            id="app-container-2",
            children=[
                html.Div(
                    children=[
                        html.P(id="brands-radio-text",
                        children="Choose Category: "),
                        dcc.RadioItems(
                            id="brands-radio",
                            options=[{'label': j, 'value':k} for j,k in zip(ALL_CAT,ALL_TEXT)],
                            value='All',
                            labelStyle={'display': 'inline-block'},                           
                        ),

                    ],className='three columns',
                ),
                html.Div(
                    children=[
                        html.P(id="product-dropdown-text",
                        children="Choose Product: "),
                        dcc.Dropdown(
                            id="product-dropdown",
                            options = [],   
                            value=[],
                            multi= True ,                           
                        ),

                    ],className='three columns',
                ),

                html.Div(
                    children=[
                        html.P(id="regions-dropdown-text",
                        children="Choose Region: "),
                        dcc.Dropdown(
                            id="region-dropdown",
                            #options=[{'label': k, 'value':k} for k in ALL_REGIONS],
                            value=[],
                            multi= True ,                           
                        ),

                    ],className='three columns',
                ),
                html.Div(
                    children=[
                        html.P(id="shoe-sizes-dropdown-text",
                        children="Choose Size: "),
                        dcc.Dropdown(
                            id="shoe-size-dropdown",
                            options=[], 
                            value=[],
                            multi= True ,                           
                        ),

                    ],className='three columns',
                ),

            ],className='row'

        ), # end bottom div 1

        # START BOTTOM DIV 2
        html.Div(
            id="app-container-3",
            children=[
                html.Div(
                    children=[
                        html.P(id="inventory-table-title",
                        children=["Inventory Management Table"],
                        ),
                        dash_table.DataTable(
                            id='inventory-table',
                            columns=[{"name": i, "id": i} for i in INVENTORY_TABLE_COLUMNS],
                            style_header={
                                'backgroundColor': 'rgb(30, 30, 30)',
                                'fontWeight': 'bold',
                                'textAlign': 'left',
                                'font_size': '16px',
                                'border': '1px solid black',

                                },

                            style_data_conditional=[
                                {
                                    'if': {'row_index': 'odd'},
                                    'backgroundColor': '#1f2630',
                                    'border': '1px solid grey' ,
                                },
                            ],

                            style_cell={
                                'backgroundColor': "#7fafdf",
                                'color': 'white',
                                'font_size': '15px',
                                'minWidth': '120px', 'width': '120px', 'maxWidth': '180px',
                                'whiteSpace': 'normal',
                            },
                            page_size=18,
                            style_table={'overflowX': '120px', 'overflowY':'auto'},
                            editable=True,
                            filter_action="native",
                            sort_action="native",
                            sort_mode="multi",
                            #column_selectable="single",
                            #row_selectable="multi",
                            
                        ),

                    ], className='six columns',

                ),

                html.Div(
                    id = "no-id",
                    children=[
                        html.P(id="inventory-gauage-title",
                        children=["Current Inventory"],
                        ),
                        html.Div(
                            id='curr-inventory-gauage-container',
                            children=[
                                daq.GraduatedBar(
                                    id="curr-inventory-gauage",
                                    color={
                                        "gradient":True,
                                        "ranges":{"green":[20,50],"yellow":[5,19],"red":[0,4]}
                                        },
                                    min = 0,
                                    max=50,
                                    step=1,
                                    labelPosition= 'bottom',
                                    showCurrentValue=True,
                                    size=800,
                                    value=15,
                                    vertical=False,
                                    theme={
                                        'dark': True,
                                    },
                                    
                                ), 

                            ],className='row'

                            
                        ),
                        html.Div(
                            id='curr-inventory-gauage-2-container',
                            children=[
                                daq.GraduatedBar(
                                    id ='curr-inventory-gauage-2',
                                    color={
                                        "gradient":True,
                                        "ranges":{"green":[20,50],"yellow":[5,19],"red":[0,4]}
                                        },
                                    min = 0,
                                    max=50,
                                    step=1,
                                    labelPosition= 'bottom',
                                    showCurrentValue=True,
                                    size=800,
                                    #value=15,
                                    vertical=False,
                                    theme={
                                        'dark': True,
                                    },
                                    
                                ), 

                            ],className='row'

                            
                        ),
                        html.Br(),
                        html.Br(),
                        html.Div(
                            id='current-inventory-led-container',
                            children=[
                                html.P(
                                    id='inventory-current-led-header',
                                    children=["Current Inventory"]
                                ),

                            ],className='row',
                        ),
                        daq.LEDDisplay(
                            id="inventory-current-led",
                            label="Total Inventory Available",
                            #value=5,
                            #backgroundColor="#FF5E5E",
                            size=90,
                        ), 
                
                        html.Br(),
                        html.Br(),
                        html.Div(
                            id='turnover-led-container',
                            children=[
                                html.P(
                                    id='inventory-turnover-led-header',
                                    children=["Inventory Turnover"]
                                ),

                            ],className='row',
                        ),

                        daq.LEDDisplay(
                            id="inventory-turnover-led",
                            label="Average Inventory Turnover ( in days )",
                            #value=5,
                            backgroundColor="#FF5E5E",
                            size=90,
                        ), 
                        html.Br(),
                        html.Br(),
                        dcc.Graph(
                            id="best-turnover-graph",
                            figure = dict(
                                data=[dict(x=0, y=0)],
                                layout=dict(
                                    paper_bgcolor="#1f2630",
                                    plot_bgcolor="#1f2630",
                                    autofill=True,
                                    margin=dict(t=75, r=50, b=100, l=50),
                                ),
                            ),

                        ), # end area graph

                        html.Br(),
                        html.Br(),
                        dcc.Graph(
                            id="worse-turnover-graph",
                            figure = dict(
                                data=[dict(x=0, y=0)],
                                layout=dict(
                                    paper_bgcolor="#1f2630",
                                    plot_bgcolor="#1f2630",
                                    autofill=True,
                                    margin=dict(t=75, r=50, b=100, l=50),
                                ),
                            ),

                        ), # end area graph                            

                    ], className='six columns',

                ),

            ],className='row'

        ), # end bottom div 2


    ],
)

layout3 = html.Div([    html.Div(' ',
        style={'backgroundColor':'rgb(0,123,255)','height':42}),
        html.Div([
            html.H2('Upload Data',
                    style={'color':'rgb(0,123,255)'}),
            
            html.Div([
                html.Div([html.Label('Orders:',
                       style={'font-weight':'bold'}),
                         html.Br(),html.Br(),
                         html.Label('Products:',
                       style={'font-weight':'bold'}),
                         html.Br(),html.Br(),
                        html.Label('Categories:',
                       style={'font-weight':'bold'}),
                        html.Br(),html.Br(),
                       ],

                        style={'float':'left','display': 'inline-block'}),
                
                html.Div([
                    dcc.Input(id='orders-file',value='orders.csv', type='text'),
                    html.Br(),html.Br(),
                    dcc.Input(id='products-file',value='products.csv', type='text'),
                    html.Br(),html.Br(),    
                    dcc.Input(id='categories-file',value='categories.csv', type='text'),
                    html.Br(),html.Br(), 
                    
                html.Button(
                id='submit-button',
                n_clicks=0,
                children='Submit',
                style={'fontSize':18,
                       'color':'rgb(255,255,255)',
                       'backgroundColor':'rgb(0,123,255)',
                       'borderRadius':5,
                       'height':42})],
                    style={'float':'left','display':'inline-block',
                           'margin-left':20}
                     )],
            style={'float':'left','display':'inline-block'}
            )],
                    style={'float':'left','display': 'inline-block',
                           'margin-left':50})
            ])
# end create pages

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
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 16:45:03 2021

@author: yegfa
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go

app = dash.Dash()
app.layout = html.Div([
    html.Div([    html.Div(' ',
        style={'backgroundColor':'rgb(0,123,255)','height':42}),
        html.Div([
            html.H2('Return of Investment Inputs',
                    style={'color':'rgb(0,123,255)'}),
            
            html.Div([
                html.Div([html.Label('Total Hits:',
                       style={'font-weight':'bold'}),
                         html.Br(),html.Br(),
                         html.Label('Conversion Rate:',
                       style={'font-weight':'bold'}),
                         html.Br(),html.Br(),
                        html.Label('Revenue Per Purchase (PhP):',
                       style={'font-weight':'bold'}),
                        html.Br(),html.Br(),
                        html.Label('Number of Times of Purchase per',
                       style={'font-weight':'bold'}),
                        html.Br(),
                        html.Label('Converted User per Year:',
                       style={'font-weight':'bold'}),
                        html.Br(),html.Br(),
                        html.Label('Total Cost of Sampling (PhP):',
                       style={'font-weight':'bold'}),
                        html.Br(),html.Br(),
                        html.Label('% of Potential Revenue You Are',
                       style={'font-weight':'bold'}),
                        html.Br(),
                        html.Label('Willing to Allocate for Sampling:',
                       style={'font-weight':'bold'})],
                        style={'float':'left','display': 'inline-block'}),
                
                html.Div([
                    dcc.Input(id='hits',value=1000000, type='text'),
                    html.Br(),html.Br(),
                    dcc.Input(id='conversion',value=60, type='text'),
                    html.Br(),html.Br(),    
                    dcc.Input(id='revenue',value=50, type='text'),
                    html.Br(),html.Br(), 
                    dcc.Input(id='times',value=2, type='text'),
                    html.Br(),html.Br(),
                    dcc.Input(id='sample',value=25000000, type='text'),
                    html.Br(),html.Br(),
                    dcc.Input(id='percent',value=50, type='text'),
                    html.Br(),html.Br(),
                html.Button(
                id='submit-button',
                n_clicks=0,
                children='Calculate ROI',
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
                    style={'float':'left','display': 'inline-block'})
            ]),
                
         
        
    html.Div([
    
    html.H2('Investment/Income Breakdown',
            style={'color':'rgb(0,123,255)','textAlign':'center'}),
    html.Div(
    dcc.Graph(id="pie-chart",style={'height':220})),

    html.H2('ROI Parameters Computed',
            style={'color':'rgb(0,123,255)','textAlign':'center'}),
    
    html.Div(
        html.Label('Total Potential Annual Revenue: '),
        style={'border':'2px black solid',
        'padding':5, 'width':300,'display': 'inline-block',
        'textAlign':'left','float':'left'}
    ),
    html.Div(
        html.Label(id='potential'),
        style={'border':'2px black solid',
        'padding':5, 'width':300, 'display': 'inline-block',
        'textAlign':'right','float':'left'}
    ),
    html.Br(), 
    html.Div(
    html.Label('Unconverted Opportunity Revenue: '),
    style={'border':'2px black solid',
        'padding':5, 'width':300, 'display': 'inline-block',
        'textAlign':'left','float':'left'}
    ),
    html.Div(
    html.Label(id='unconverted'),
    style={'border':'2px black solid',
        'padding':5, 'width':300, 'display': 'inline-block',
        'textAlign':'right','float':'left'}),
    html.Br(), 
    html.Div(
    html.Label('Converted Revenue: '),
    style={'border':'2px black solid',
        'padding':5, 'width':300,'display': 'inline-block',
        'textAlign':'left','float':'left'}
    ),
    html.Div(    
    html.Label(id='converted'),
    style={'border':'2px black solid',
        'padding':5, 'width':300, 'display': 'inline-block',
        'textAlign':'right','float':'left'}),
    html.Div(
    html.Label('Maximum Allowable Spend: '),
    style={'border':'2px black solid',
        'padding':5, 'width':300,'display': 'inline-block',
        'textAlign':'left','float':'left'}
    ),
    html.Div(
    html.Label(id='maxallow'),
        style={'border':'2px black solid',
        'padding':5, 'width':300, 'display': 'inline-block',
        'textAlign':'right','float':'left'}),
    html.Br(), 
    html.Div(
    html.Label('Maximum Spend per Hit: '),
    style={'border':'2px black solid',
        'padding':5, 'width':300, 'display': 'inline-block',
        'textAlign':'left','float':'left'}
    ),
    html.Div(    
    html.Label(id='maxperhit'),
        style={'border':'2px black solid',
        'padding':5, 'width':300, 'display': 'inline-block','float':'left'}
        ),
    html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),
    html.H2('Estimated Net Profit from Sampling',
            style={'color':'rgb(0,123,255)','textAlign':'center'}),
    
    html.Div([
        html.Div(
    html.Label('Net Profit: '),
    style={'border':'2px black solid',
        'padding':5, 'width':300, 'display': 'inline-block',
        'textAlign':'left','float':'left'}
    ),
    html.Div(
    html.Label(id='profit'),
        style={'border':'2px black solid',
        'padding':5, 'width':300, 'display': 'inline-block','float':'left'}),    
    ])
    ],style={'width': '50%','float': 'left','display': 'inline-block',
             'textAlign':'right'})
            ],
    
        style={'display':'inline-block'})
      
             

@app.callback(
    Output('potential', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('hits', 'value'),
     State('conversion','value'),
     State('revenue','value'),
     State('times','value'),
     State('sample','value'),
     State('percent','value')])
def output1(n_clicks, hits, conversion, revenue, times, sample, percent):
    number = int(hits)*int(revenue)*int(times)
    return "Php{:,.2f}".format(number)

@app.callback(
    Output('unconverted', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('hits', 'value'),
     State('conversion','value'),
     State('revenue','value'),
     State('times','value'),
     State('sample','value'),
     State('percent','value')])
def output2(n_clicks, hits, conversion, revenue, times, sample, percent):
    number = (100-float(conversion))/100*int(hits)*int(revenue)*int(times)
    return "Php{:,.2f}".format(number)

@app.callback(
    Output('converted', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('hits', 'value'),
     State('conversion','value'),
     State('revenue','value'),
     State('times','value'),
     State('sample','value'),
     State('percent','value')])
def output3(n_clicks, hits, conversion, revenue, times, sample, percent):
    number = float(conversion)/100*int(hits)*int(revenue)*int(times)
    return "Php{:,.2f}".format(number)

@app.callback(
    Output('maxallow', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('hits', 'value'),
     State('conversion','value'),
     State('revenue','value'),
     State('times','value'),
     State('sample','value'),
     State('percent','value')])
def output4(n_clicks, hits, conversion, revenue, times, sample, percent):
    profit = float(conversion)/100*int(hits)*int(revenue)*int(times)-int(sample)
    maxallow = float(profit)*(float(percent)/100)
    return "Php{:,.2f}".format(maxallow)

@app.callback(
    Output('maxperhit', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('hits', 'value'),
     State('conversion','value'),
     State('revenue','value'),
     State('times','value'),
     State('sample','value'),
     State('percent','value')])
def output5(n_clicks, hits, conversion, revenue, times, sample, percent):
    profit = float(conversion)/100*int(hits)*int(revenue)*int(times)-int(sample)
    maxallow = float(profit)*(float(percent)/100)
    maxperhit = maxallow/hits
    return "Php{:,.2f}".format(maxperhit)

@app.callback(
    Output('profit', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('hits', 'value'),
     State('conversion','value'),
     State('revenue','value'),
     State('times','value'),
     State('sample','value'),
     State('percent','value')])
def output6(n_clicks, hits, conversion, revenue, times, sample, percent):
    number = (float(conversion)/100*int(hits)*int(revenue)*int(times))-int(sample)
    return "Php{:,.2f}".format(number)

@app.callback(
    Output("pie-chart", "figure"), 
    [Input('submit-button', 'n_clicks')],
    [State('hits', 'value'),
     State('conversion','value'),
     State('revenue','value'),
     State('times','value'),
     State('sample','value'),
     State('percent','value')])
def generate_chart(n_clicks, hits, conversion, revenue, times, sample, percent):
    
    unconverted = (100-float(conversion))/100*int(hits)*int(revenue)*int(times)
    profit = float(conversion)/100*int(hits)*int(revenue)*int(times)-int(sample)
    maxallow = float(profit)*(float(percent)/100)
    notsample = (100-float(percent))/100*profit
    
    labels = ['Sampling Cost, Php','Unconverted Revenue, Php','Max Allowable Spend, Php','Net Profit Not from Sampling, Php']
    values = [sample, unconverted, maxallow, notsample]
    colors = ['rgb(44,82,103)','rgb(242,217,187)','rgb(134,169,189)','rgb(255,59,60)']
    
    fig = go.Figure(data=[go.Pie(labels=labels, values=values,
                                marker=dict(colors=colors,
                                line=dict(color='#000000', width=2)),hole=0.3,
                                showlegend=False)])
    fig.update_traces(textposition='outside', textinfo='value+label'),
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))                  
    return fig

if __name__ == '__main__':
    app.run_server()

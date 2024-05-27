  
import dash
import os

external_stylesheets = [ 'https://codepen.io/chriddyp/pen/bWLwgP.css']

# meta_tags are required for the app layout to be mobile responsive
app = dash.Dash(__name__, 
                suppress_callback_exceptions=True,
                external_stylesheets=external_stylesheets,
                #url_base_pathname='/dashboard/',
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
app.title = 'Sales and Inventory Dashboard'

app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 3000)))

server = app.server
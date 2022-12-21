import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from views.header import make_header
from views.form import make_form
from views.table import make_table
from src.predict import predict
import src.config as cfg
import views.constants as cons

# Inicializamos la app usando un css de bootstrap externo
app = dash.Dash(__name__, external_stylesheets=[cons.BOOTSTRAP_CSS])
app.title = cons.APP_TITLE

# Layout de la aplicación
app.layout =dbc.Container(html.Div([
            # header
            make_header(),

            # Tabla de datos
            html.Div([
                html.H1(cons.TABLE_TITLE, className='display-3'),
                html.Hr(className='my-2'),
                
                html.Div(children=make_table()),
            ]),

            # Prueba predictiva usando el modelo
            html.Div([
                html.H1(cons.TEST_TITLE, className='display-3'),
                html.P(cons.TEST_DESC),
                html.Hr(className='my-2'),
                
                html.Div(children=make_form()),

            
                html.Button(cons.TEST_BUTTON,className = 'btn btn-primary btn-lg', id='submit-val', n_clicks=0),
                html.Br(),
                html.Br(),
                html.Div(id='container-button-basic',className='alert alert-primary'),
            ], className='jumbotron'),
        ],
        id="layout",
    ))

# =======================================================================================================
# CALLBACKS
# =======================================================================================================

# Procesa el formulario para hacer la predicción
@app.callback(
    [Output('container-button-basic', 'children'),
    Output('container-button-basic', 'className'), ],
    Input('submit-val', 'n_clicks'),
    [State('input-on-submit-1', 'value'),
    State('input-on-submit-2', 'value'),
    State('input-on-submit-3', 'value'),
    State('input-on-submit-4', 'value'),
    State('input-on-submit-5', 'value'),
    State('input-on-submit-6', 'value'),
    State('input-on-submit-7', 'value'),
    State('input-on-submit-8', 'value'),
    State('input-on-submit-9', 'value'),
    State('input-on-submit-10', 'value'),
    State('input-on-submit-11', 'value')
    ]
)
def update_output(n_clicks, value1,value2, value3,value4, value5,value6, value7,value8, value9,value10, value11):
    # Todos los campos deben tener valor
    message, style = cons.TEST_FILL_FIELDS , 'alert alert-primary'
    if n_clicks:
        if None in locals().values() : return message,style
        # Input del modelo
        x = [[value1,value2, value3,value4, value5,value6, value7,value8, value9,value10, value11]]
        # Predicción del modelo
        y = predict(x)

        # Mensaje y estilo del mismo
        message = cons.TEST_POSITIVE if y else cons.TEST_NEGATIVE
        style = 'alert alert-danger' if y else 'alert alert-success'
    return message, style
        
if __name__ == '__main__':
    if cfg.ENV_LOCAL:
        app.run_server(debug=cfg.DEBUG_SERVER, port = cfg.PORT)
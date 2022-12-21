from dash import html, dcc
import dash_bootstrap_components as dbc

import views.constants as cons


def make_form():
    return dbc.Form([age_input,
                    sex_input,
                    smoking_input,
                    anaemia_input,
                    diabetes_input,
                    pressure_input,
                    cpk_input,
                    eyec_input,
                    platelet_input,
                    creatinine_input,
                    sodium_input,
                    ]),
    
age_input = html.Div(
    [
        dbc.Label(cons.FORM_AGE_LABEL),
        dbc.Input(id='input-on-submit-1', type='number',placeholder=cons.FORM_AGE_INPUT_PLACEHOLDER,autocomplete="off"),
        dbc.FormText(
            cons.FORM_AGE_DESC,
            color="primary",
        ),
    ],
    className="form-group",
)
cpk_input = html.Div(
    [
        dbc.Label(cons.FORM_CPK_LABEL),
        dbc.Input(id='input-on-submit-3', type='number', placeholder=cons.FORM_CPK_INPUT_PLACEHOLDER,autocomplete="off"),
        dbc.FormText(
           cons.FORM_CPK_DESC,
            color="primary",
        ),
    ],
    className="form-group",
)

eyec_input = html.Div(
    [
        dbc.Label(cons.FORM_EYECC_LABEL),
        dbc.Input(id='input-on-submit-5', type='number', placeholder =cons.FORM_EYECC_INPUT_PLACEHOLDER,autocomplete="off" ),
        dbc.FormText(
            cons.FORM_EYECC_DESC,
            color="primary",
        ),
    ],
    className="form-group",
)
platelet_input = html.Div(
    [
        dbc.Label(cons.FORM_PLAT_LABEL),
        dbc.Input(id='input-on-submit-7', type='number', placeholder=cons.FORM_PLAT_INPUT_PLACEHOLDER,autocomplete="off"),
        dbc.FormText(
            cons.FORM_PLAT_DESC,
            color="primary",
        ),
    ],
    className="form-group",
)
creatinine_input = html.Div(
    [
        dbc.Label(cons.FORM_CREAT_LABEL),
        dbc.Input(id='input-on-submit-8', type='number', placeholder=cons.FORM_CREAT_INPUT_PLACEHOLDER,autocomplete="off"),
        dbc.FormText(
            cons.FORM_CREAT_DESC,
            color="primary",
        ),
    ],
    className="form-group",
)
sodium_input = html.Div(
    [
        dbc.Label(cons.FORM_SOD_LABEL),
        dbc.Input(id='input-on-submit-9', type='number', placeholder=cons.FORM_SOD_INPUT_PLACEHOLDER,autocomplete="off"),
        dbc.FormText(
            cons.FORM_SOD_DESC,
            color="primary",
        ),
    ],
    className="form-group",
)

anaemia_input = html.Div([
    dbc.Label(cons.FORM_ANAEM_LABEL),
    dcc.Dropdown(
        options=[
            {'label': 'Sí', 'value': 1},
            {'label': 'No', 'value': 0},
        ],
        placeholder=cons.FORM_ANAEM_INPUT_PLACEHOLDER,
        id="input-on-submit-2"
    ),
    dbc.FormText(
            cons.FORM_ANAEM_DESC,
            color="primary",
        ),
], className="form-group",)

diabetes_input = html.Div([
    dbc.Label(cons.FORM_DIAB_LABEL),
    dcc.Dropdown(
        options=[
            {'label': 'Sí', 'value': 1},
            {'label': 'No', 'value': 0},
        ],
        placeholder=cons.FORM_DIAB_INPUT_PLACEHOLDER,
        id="input-on-submit-4"
    ),
    dbc.FormText(
            cons.FORM_DIAB_DESC,
            color="primary",
        ),
], className="form-group",)

pressure_input =  html.Div([
    dbc.Label(cons.FORM_PRESS_LABEL),
    dcc.Dropdown(
        options=[
            {'label': 'Sí', 'value': 1},
            {'label': 'No', 'value': 0},
        ],
        placeholder=cons.FORM_PRESS_INPUT_PLACEHOLDER,
        id="input-on-submit-6"
    ),    
    dbc.FormText(
            cons.FORM_PRESS_DESC,
            color="primary",
        ),
], className="form-group",)

sex_input = html.Div([
    dbc.Label(cons.FORM_SEX_LABEL),
    dcc.Dropdown(
        options=[
            {'label': 'Hombre', 'value': 1},
            {'label': 'Mujer', 'value': 0},
        ],
        placeholder=cons.FORM_SEX_INPUT_PLACEHOLDER,
        id="input-on-submit-10"
    ),    
    dbc.FormText(
            cons.FORM_SEX_DESC,
            color="primary",
        ),
], className="form-group",)

smoking_input =  html.Div([
    dbc.Label(cons.FORM_SMOKE_LABEL),
    dcc.Dropdown(
        options=[
            {'label': 'Sí', 'value': 1},
            {'label': 'No', 'value': 0},
        ],
        placeholder=cons.FORM_SMOKE_INPUT_PLACEHOLDER,
        id="input-on-submit-11"
    ),    
    dbc.FormText(
            cons.FORM_SMOKE_DESC,
            color="primary",
        ),
], className="form-group",)


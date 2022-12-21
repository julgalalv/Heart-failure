# APP
APP_TITLE = 'HF App'
BOOTSTRAP_CSS = 'https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/cerulean/bootstrap.min.css'

# HEADER

HEADER_TITLE = "Aplicación de fallo cardíaco"
HEADER_BY = "Por Julián Galindo Álvarez."
HEADER_DESC = """
    Esta aplicación permite explorar los datos del archivo heart_failure.csv y realizar una predicción en base al 
    modelo determinado en el notebook.

    En la tabla se puede ordenar y filtrar usando la sintaxis descrita en:
"""

HEADER_DASH_DOC = 'Documentación oficial de Dash'
HEADER_DASH_HREF = "https://dash.plotly.com/datatable/filtering"

# BODY
# TABLE
TABLE_TITLE = "Datos"
TABLE_HEADERS  = [
        'Edad',
        'Sexo',
        'Fumador',
        'Anemia',
        'Diabetes',
        'Hipertensión',
        'CPK(UI/L)',
        'Eyecc.(%)',
        'Plaquetas(1/mcL)',
        'Creatinina(mg/dL)',
        'Sodio(mEq/L)',
        'Tiempo(d)',
        'Deceso'
]

# PREDICTIVE TEST
TEST_TITLE = "Prueba predictiva"
TEST_DESC = 'Para realizar una predicción es necesario indicar todos los datos del siguiente formulario.'
TEST_BUTTON = 'Calcular'

TEST_FILL_FIELDS = "Indica todos los campos"
TEST_POSITIVE = 'Peligro potencial'
TEST_NEGATIVE = 'No hay problema aparente'

# FORM

FORM_AGE_LABEL = "Edad"
FORM_AGE_INPUT_PLACEHOLDER = 'Edad'
FORM_AGE_DESC = "Edad del paciente"

FORM_CPK_LABEL = 'CPK en sangre (UI/L)'
FORM_CPK_INPUT_PLACEHOLDER = 'CPK'
FORM_CPK_DESC =  "Cantidad de creatina fosfoquinasa (CPK) en sangre del paciente. Referencia normal: 52 - 336"

FORM_EYECC_LABEL = "Fracción de eyección (%)"
FORM_EYECC_INPUT_PLACEHOLDER = 'Eyección'
FORM_EYECC_DESC = "Fracción de eyección del paciente en tanto por ciento. Referencia normal: 50 - 75"

FORM_PLAT_LABEL = "Plaquetas (1/mcL)"
FORM_PLAT_INPUT_PLACEHOLDER ='Plaquetas'
FORM_PLAT_DESC = "Cantidad de plaquetas en sangre del paciente por microlitro. Referencia normal: 150000 - 450000"

FORM_CREAT_LABEL = "Creatinina (mg/dL)"
FORM_CREAT_INPUT_PLACEHOLDER = 'Creatinina'
FORM_CREAT_DESC = "Cantidad de creatinina en suero del paciente en mg/dL. Referencia normal: 0,6 - 1,3"

FORM_SOD_LABEL = "Sodio en sangre (mEq/L)"
FORM_SOD_INPUT_PLACEHOLDER = 'Sodio'
FORM_SOD_DESC = "Cantidad de sodio en suero del paciente en mEq/L. Referencia normal: 130 - 145"

FORM_ANAEM_LABEL ='Anemia'
FORM_ANAEM_INPUT_PLACEHOLDER ='Anemia'
FORM_ANAEM_DESC = "Indica si el paciente tiene anemia"

FORM_DIAB_LABEL ='Diabetes'
FORM_DIAB_INPUT_PLACEHOLDER ='Diabetes'
FORM_DIAB_DESC = "Indica si el paciente tiene diabetes"

FORM_PRESS_LABEL ='Hipertensión'
FORM_PRESS_INPUT_PLACEHOLDER ='Hipertensión'
FORM_PRESS_DESC =  "Indica si el paciente tiene hipertensión"

FORM_SEX_LABEL ='Sexo'
FORM_SEX_INPUT_PLACEHOLDER ='Sexo'
FORM_SEX_DESC = "Sexo del paciente"

FORM_SMOKE_LABEL ='Fumador'
FORM_SMOKE_INPUT_PLACEHOLDER ='Fumador'
FORM_SMOKE_DESC = "Indica si el paciente es fumador"



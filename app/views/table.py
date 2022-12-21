import dash
from dash import html, dcc,dash_table
import dash_bootstrap_components as dbc

from src.load import refactored_df
import src.config as cfg
import views.constants as cons

df = refactored_df

# Tabla con los datos. Filtrable y ordenable
def make_table():
    table = dash_table.DataTable(
                id="datatable-interactivity",
                columns=[{"name": j, "id": i} for (i,j) in zip(df.columns,cons.TABLE_HEADERS)],
                data=df.to_dict("records"),
                style_as_list_view=True,
                editable=False,
                filter_action="native",
                sort_action="native",
                sort_mode="multi",
                column_selectable="single",
                row_selectable=False,
                row_deletable=False,
                page_action="native",
                page_current= 0,
                page_size= 10,
            )
    return table
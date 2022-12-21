from dash import html
import views.constants as cons



def make_header():
    header = html.Div(
        [
            html.H1(cons.HEADER_TITLE, className="display-2"),
            html.Div(
                [
                    html.P(cons.HEADER_BY, className="subtitle"),
                    html.P(cons.HEADER_DESC, className="description"),
                    html.A(cons.HEADER_DASH_DOC, href=cons.HEADER_DASH_HREF, target="_blank")
                ]
            ),
        ],
        id="header",
    )

    return header

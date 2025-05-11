from dash import Output, Input, State, dcc, ctx  

from dash.exceptions import PreventUpdate

def register_analysis_suggestions_callbacks(app):
    @app.callback(
        Output("offcanvas-analysis-suggestions", "is_open"),
        [Input("open-suggestions-offcanvas", "n_clicks"),
         Input("close-suggestions-offcanvas", "n_clicks")],
        prevent_initial_call=True
    )
    def toggle_offcanvas(open_click, close_click):
        if ctx.triggered_id == "open-suggestions-offcanvas":
            return True
        elif ctx.triggered_id == "close-suggestions-offcanvas":
            return False
        return False

from dash import Output, Input, State, ctx
from dash.exceptions import PreventUpdate

def register_analysis_suggestions_callbacks(app):
    @app.callback(
        Output("offcanvas-analysis-suggestions", "is_open"),
        [Input("open-suggestions-offcanvas", "n_clicks"),
         Input("close-suggestions-offcanvas", "n_clicks")],
        [State("offcanvas-analysis-suggestions", "is_open")],
        prevent_initial_call=True
    )
    def toggle_offcanvas(open_click, close_click, is_open):
        if ctx.triggered_id in ["open-suggestions-offcanvas", "close-suggestions-offcanvas"]:
            return not is_open
        raise PreventUpdate

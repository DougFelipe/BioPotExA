from dash import Input, Output, State, ctx

def register_analysis_suggestions_callbacks(app):
    @app.callback(
        Output("modal-analysis-suggestions", "is_open"),
        [Input("open-suggestions-modal", "n_clicks"),
         Input("close-suggestions-modal", "n_clicks")],
        [State("modal-analysis-suggestions", "is_open")]
    )
    def toggle_modal(open_click, close_click, is_open):
        if ctx.triggered_id in ["open-suggestions-modal", "close-suggestions-modal"]:
            return not is_open
        return is_open

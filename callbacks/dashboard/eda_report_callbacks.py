import pandas as pd
import io
from dash import callback, Output, Input, State, dcc, html
from dash.exceptions import PreventUpdate
from ydata_profiling import ProfileReport
from utils.data_processing import merge_input_with_database
import dash


@callback(
    Output("download-eda-report", "data"),
    Input("download-eda-btn", "n_clicks"),
    State("stored-data", "data"),
    prevent_initial_call=True
)
def generate_eda_report(n_clicks, stored_data):
    if not stored_data:
        raise PreventUpdate

    try:
        df_input = pd.DataFrame(stored_data)
        df_merged = merge_input_with_database(df_input)
        profile = ProfileReport(df_merged, minimal=True, explorative=True)
        html_str = profile.to_html()
        return dcc.send_string(html_str, filename="EDA_Report_BioRemPP.html")
    except Exception as e:
        print(f"[ERROR] Failed to generate EDA report: {str(e)}")
        raise PreventUpdate


# ✅ NOVO: alerta controlado por um único callback
@callback(
    Output("eda-alert", "children"),
    Output("eda-alert", "style"),
    Output("eda-alert-interval", "disabled"),
    Input("download-eda-btn", "n_clicks"),
    Input("eda-alert-interval", "n_intervals"),
    prevent_initial_call=True
)
def toggle_eda_alert(n_clicks, n_intervals):
    ctx = dash.callback_context

    if not ctx.triggered:
        raise PreventUpdate

    trigger_id = ctx.triggered_id

    if trigger_id == "download-eda-btn":
        # Mostrar alerta ao clicar no botão
        alert = html.Div("✅ EDA report is being generated and will download shortly...", className="alert alert-success text-center")
        return alert, {"display": "block"}, False

    elif trigger_id == "eda-alert-interval":
        # Esconder alerta após timeout
        return dash.no_update, {"display": "none"}, True

    raise PreventUpdate

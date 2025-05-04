# callbacks/core/merge_feedback_callbacks.py

import dash,html
from dash import callback, Output, Input, State
from dash.exceptions import PreventUpdate
import pandas as pd

# Importando o pipeline de merge e o gerador de alertas
from callbacks.core.merge_pipeline import merge_and_time
from callbacks.core.feedback_alerts import create_alert

@callback(
    [
        Output('stored-merged-results', 'data'),
        Output('merge-timings', 'data'),
        Output('alert-container', 'children'),
        Output('process-data', 'disabled'),
        Output('view-results', 'style'),
        Output('process-data', 'style'),
        Output('page-state', 'data', allow_duplicate=True)
    ],
    Input('process-data', 'n_clicks'),
    State('stored-data', 'data'),
    prevent_initial_call=True
)
def handle_merge_and_feedback(n_clicks, stored_data):
    """
    Performs the merging steps, measures execution time, and gives user feedback.

    Parameters:
    - n_clicks (int): Number of times the "process-data" button was clicked.
    - stored_data (dict): Data previously uploaded or loaded.

    Returns:
    - Merged results to be stored
    - Execution times for each merge
    - Alert message
    - Button states and visibility
    """
    if n_clicks is None or stored_data is None:
        raise PreventUpdate

    try:
        input_df = pd.DataFrame(stored_data)

        # Executar os merges e medir os tempos
        merged_results, timings = merge_and_time(input_df)

        # Construir mensagem de tempos
        time_messages = [
            html.P(f"Tempo de merge com Database: {timings['database_merge']:.2f} segundos"),
            html.P(f"Tempo de merge com HADEG: {timings['hadeg_merge']:.2f} segundos"),
            html.P(f"Tempo de merge com ToxCSM: {timings['toxcsm_merge']:.2f} segundos")
        ]

        alert = create_alert(
            [
                html.H5("Merge realizado com sucesso! 🚀"),
                html.Hr(),
                *time_messages
            ],
            color='success'
        )

        return (
            {key: df.to_dict('records') for key, df in merged_results.items()},
            timings,
            alert,
            True,  # Desabilita botão "Processar"
            {'display': 'inline-block'},  # Mostra botão "Ver Resultados"
            {'display': 'none'},  # Esconde botão "Processar"
            'processed'
        )

    except Exception as e:
        alert = create_alert(f"Erro durante o processamento: {str(e)}", color='danger')
        return dash.no_update, dash.no_update, alert, False, dash.no_update, dash.no_update, dash.no_update

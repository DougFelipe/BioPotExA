# callbacks/core/merge_feedback_callbacks.py

import time
import logging
import pandas as pd
import dash_bootstrap_components as dbc
from dash import callback_context, html
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State

from app import app
from utils.core.data_processing import (
    merge_input_with_database,
    merge_input_with_database_hadegDB,
    merge_with_toxcsm,
    merge_with_kegg
)
from utils.core.feedback_alerts import create_alert

# Setup logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@app.callback(  
    [  
        Output('merge-status', 'data'),  
        Output('page-state', 'data', allow_duplicate=True),  
        Output('alert-container', 'children'),  
        # NOVOS OUTPUTS PARA OS STORES ESPECÍFICOS  
        Output('biorempp-merged-data', 'data'),  
        Output('kegg-merged-data', 'data'),  
        Output('hadeg-merged-data', 'data'),  
        Output('toxcsm-merged-data', 'data')  
    ],  
    [Input('process-data', 'n_clicks')],  
    [State('stored-data', 'data')],  
    prevent_initial_call=True  
)  
def handle_merge_and_feedback(n_clicks, stored_data):  
    """  
    Handles the sequential merging of input data with multiple databases,  
    measuring execution time and storing results in dedicated stores.  
    """  
    if n_clicks is None or not stored_data:  
        raise PreventUpdate  
  
    input_df = pd.DataFrame(stored_data)  
    merge_times = {}  
    errors = []  
      
    # Inicializar variáveis para armazenar dados processados  
    merged_biorempp_data = None  
    merged_kegg_data = None  
    merged_hadeg_data = None  
    merged_toxcsm_data = None  
  
    # MERGE 1: BioRemPP  
    try:  
        logger.info("Starting merge with BioRemPP...")  
        start = time.time()  
        merged_biorempp = merge_input_with_database(input_df.copy())  
        merge_times['BioRemPP'] = round(time.time() - start, 2)  
        logger.info("BioRemPP merge completed in %.2fs", merge_times['BioRemPP'])  
        # ARMAZENAR DADOS PROCESSADOS  
        merged_biorempp_data = merged_biorempp.to_dict('records') if merged_biorempp is not None else None  
    except Exception as e:  
        error_msg = f"BioRemPP merge failed: {str(e)}"  
        logger.error(error_msg)  
        errors.append(error_msg)  
        merged_biorempp = None  
  
    # MERGE 2: KEGG (requires BioRemPP merge)  
    if merged_biorempp is not None:  
        try:  
            logger.info("Starting merge with KEGG...")  
            start = time.time()  
            merged_kegg = merge_with_kegg(merged_biorempp.copy())  
            merge_times['KEGG'] = round(time.time() - start, 2)  
            logger.info("KEGG merge completed in %.2fs", merge_times['KEGG'])  
            # ARMAZENAR DADOS PROCESSADOS  
            merged_kegg_data = merged_kegg.to_dict('records') if merged_kegg is not None else None  
        except Exception as e:  
            error_msg = f"KEGG merge failed: {str(e)}"  
            logger.error(error_msg)  
            errors.append(error_msg)  
    else:  
        msg = "KEGG merge skipped due to BioRemPP merge failure."  
        logger.warning(msg)  
        errors.append(msg)  
  
    # MERGE 3: HADEG  
    try:  
        logger.info("Starting merge with HADEG...")  
        start = time.time()  
        merged_hadeg = merge_input_with_database_hadegDB(input_df.copy())  
        merge_times['HADEG'] = round(time.time() - start, 2)  
        logger.info("HADEG merge completed in %.2fs", merge_times['HADEG'])  
        # ARMAZENAR DADOS PROCESSADOS  
        merged_hadeg_data = merged_hadeg.to_dict('records') if merged_hadeg is not None else None  
    except Exception as e:  
        error_msg = f"HADEG merge failed: {str(e)}"  
        logger.error(error_msg)  
        errors.append(error_msg)  
  
    # MERGE 4: ToxCSM (requires BioRemPP merge)  
    if merged_biorempp is not None:  
        try:  
            logger.info("Starting merge with ToxCSM...")  
            start = time.time()  
            merged_toxcsm = merge_with_toxcsm(merged_biorempp.copy())  
            merge_times['ToxCSM'] = round(time.time() - start, 2)  
            logger.info("ToxCSM merge completed in %.2fs", merge_times['ToxCSM'])  
            # ARMAZENAR DADOS PROCESSADOS  
            merged_toxcsm_data = merged_toxcsm.to_dict('records') if merged_toxcsm is not None else None  
        except Exception as e:  
            error_msg = f"ToxCSM merge failed: {str(e)}"  
            logger.error(error_msg)  
            errors.append(error_msg)  
    else:  
        msg = "ToxCSM merge skipped due to BioRemPP merge failure."  
        logger.warning(msg)  
        errors.append(msg)  
  
    # UI Feedback (mesmo código existente)  
    if errors:  
        alert = create_alert([  
            "❌ One or more merges failed:",  
            html.Ul([html.Li(err) for err in errors])  
        ], color='danger')  
        return (  
            {'status': 'failed', 'merge_times': merge_times},   
            'initial',   
            alert,  
            merged_biorempp_data,  
            merged_kegg_data,  
            merged_hadeg_data,  
            merged_toxcsm_data  
        )  
  
    alert_msg = html.Div([  
        html.P("✅ All merges completed successfully.", style={'marginBottom': '5px'}),  
        html.Ul([  
            html.Li(f"BioRemPP: {merge_times.get('BioRemPP', '-'):.2f}s"),  
            html.Li(f"KEGG: {merge_times.get('KEGG', '-'):.2f}s"),  
            html.Li(f"HADEG: {merge_times.get('HADEG', '-'):.2f}s"),  
            html.Li([  
                f"ToxCSM: {merge_times.get('ToxCSM', '-'):.2f}s",  
                html.Br(),  
                dbc.Spinner(size="sm", color="success", type="border", spinner_style={"marginRight": "6px"}),  
                html.Span("Generating output"),  
                html.Br(),  
                html.Span("Click the "),  
                html.Strong("View Results", style={"color": "red", "fontWeight": "bold"}),  
                html.Span(" button when it becomes available.")  
            ])  
        ], style={'paddingLeft': '20px', 'margin': 0})  
    ])  
  
    alert = create_alert(alert_msg, color='success')  
      
    # RETORNAR TODOS OS DADOS PROCESSADOS  
    return (  
        {'status': 'done', 'merge_times': merge_times},   
        'processed',   
        alert,  
        merged_biorempp_data,  
        merged_kegg_data,  
        merged_hadeg_data,  
        merged_toxcsm_data  
    )

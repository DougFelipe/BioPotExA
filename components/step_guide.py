# my_dash_app/components/step_guide.py

from dash import html

# Lista de passos para o guia
step_guide_list = [
    {"step_number": "Step 1", "title": "Upload Data", "description": "Upload your data files for analysis."},
    {"step_number": "Step 2", "title": "Process Data", "description": "Process the uploaded data to extract insights."},
    {"step_number": "Step 3", "title": "View Results", "description": "View the analysis results and download reports."}
]

# Função para criar um card de passo a passo
def create_step_card(step_number, title, description):
    return html.Div(
        className='step-card',
        children=[
            html.Div(
                className='box',
                children=[
                    html.Div(
                        className='content',
                        children=[
                            html.H2(step_number),
                            html.H3(title),
                            html.P(description)
                        ]
                    )
                ]
            )
        ]
    )

# Função para criar todos os cards de passos
def create_step_guide():
    return html.Div(
        className='step-cards-container',
        children=[create_step_card(step['step_number'], step['title'], step['description']) for step in step_guide_list]
    )

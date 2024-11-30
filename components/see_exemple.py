# components/see_example.py
from dash import html

def get_see_example_layout():
    """
    Define e retorna o layout para a página "See Example".

    Este layout inclui um título e um texto de exemplo, seguindo o estilo da página "About".
    """
    return html.Div(
        className='see-example-container', 
        children=[
            html.Div(
                className='see-example-content-container',
                children=[
                    html.Div(
                        className='see-example-text-container',
                        children=[
                            html.H3('See Example', className='see-example-title'),  # Título principal
                            html.Hr(className="my-2"),  # Linha horizontal para separação
                            html.P(
                                """
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque rutrum accumsan 
                                nisi, eu malesuada lacus hendrerit quis. Suspendisse potenti. Nam ut ex at urna 
                                fermentum luctus. Vestibulum at lacus vitae felis sodales dignissim. 
                                """,
                                className='see-example-content'
                            ),
                            html.P(
                                """
                                Integer molestie euismod elit, a efficitur ipsum ultricies nec. Ut ornare massa non 
                                nisi elementum, et tincidunt felis luctus. Praesent feugiat ultrices ligula, sed 
                                rhoncus arcu vehicula ut. Curabitur posuere nunc id risus pulvinar, non suscipit 
                                ligula gravida.
                                """,
                                className='see-example-content'
                            )
                        ]
                    )
                ]
            )
        ]
    )

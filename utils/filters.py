# utils/filters.py

from dash import dcc

def create_range_slider(slider_id):
    """
    Cria e retorna um componente RangeSlider do Dash com configurações iniciais.

    :param slider_id: ID do componente RangeSlider.
    :return: Componente dcc.RangeSlider com configurações iniciais.
    """
    return dcc.RangeSlider(
        id=slider_id,
        min=0,  # Valor mínimo inicial
        max=10,  # Valor máximo inicial - será ajustado dinamicamente
        value=[0, 10],  # Valor inicial - será ajustado dinamicamente
        marks={i: str(i) for i in range(11)},  # Marcas iniciais - serão ajustadas dinamicamente
        className='range-slider'
    )

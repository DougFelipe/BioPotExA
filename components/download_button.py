from dash import html

def get_sample_data_button():
    """
    Gera um botão para fazer o download do arquivo sample_data.txt.

    :return: Um componente HTML do botão configurado para download.
    """
    return html.A(
        "Download Example Data",  # Texto do botão
        id="download-sample-data-button",  # ID para CSS e testes
        href="/assets/biorempp_sample_data.txt",  # Caminho para o arquivo de exemplo
        download="biorempp_sample_data.txt",  # Configuração de download
        className="download-button"  # Classe para estilização
    )

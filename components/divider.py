from dash import html

def NeonDivider(className="my-2", style=None):
    base_style = {
        "borderColor": "#39ff14",
        "borderWidth": "2px",
        "borderStyle": "solid",
        "boxShadow": "0 0 10px #39ff14",
        "width": "100%"
    }

    # Permite que o usuário sobrescreva ou adicione estilos
    if style:
        base_style.update(style)

    return html.Hr(className=className, style=base_style)

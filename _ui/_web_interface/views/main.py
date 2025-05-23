import dash_core_components as dcc
import dash_html_components as html
from variables import tak_folder_exists

layout = html.Div(
    [
        dcc.Location(id="url", children="/config", refresh=True),
        html.Div(
            [
                html.Img(
                    src="../assets/kraken_interface_bw.png",
                    style={"display": "block", "marginLeft": "auto", "marginRight": "auto", "height": "60px"},
                )
            ]
        ),
        html.Div(
            [
                html.A("Configuracion", className="header_active", id="header_config", href="/config"),
                html.A("Espectro", className="header_inactive", id="header_spectrum", href="/spectrum"),
                html.A("DoA Estimation", className="header_inactive", id="header_doa", href="/doa"),
                html.Div(
                    [
                        html.A("TAK", className="header_inactive", id="header_tak", href="#", n_clicks=0),
                    ],
                    id="tak_container",
                    style={"display": "inline-block"} if tak_folder_exists else {"display": "none"},
                ),
                html.Div(id="header_tak_dummy", style={"display": "none"}),  # Hidden div for callback output
            ],
            className="header",
        ),
        dcc.Interval(id="settings-refresh-timer", interval=500, n_intervals=0),
        html.Div(id="placeholder_start", style={"display": "none"}),
        html.Div(id="placeholder_stop", style={"display": "none"}),
        html.Div(id="placeholder_save", style={"display": "none"}),
        html.Div(id="placeholder_update_rx", style={"display": "none"}),
        html.Div(id="placeholder_recofnig_daq", style={"display": "none"}),
        html.Div(id="placeholder_update_daq_ini_params", style={"display": "none"}),
        html.Div(id="placeholder_update_freq", style={"display": "none"}),
        html.Div(id="placeholder_update_dsp", style={"display": "none"}),
        html.Div(id="placeholder_config_page_upd", style={"display": "none"}),
        html.Div(id="placeholder_spectrum_page_upd", style={"display": "none"}),
        html.Div(id="placeholder_doa_page_upd", style={"display": "none"}),
        html.Div(id="dummy_output", style={"display": "none"}),
        html.Div(id="page-content"),
    ]
)

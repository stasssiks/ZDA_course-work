import os

from dash import html, dcc, register_page, callback, Output, Input, State
from dash import dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import dash
from flask import send_file
import pdfkit

register_page(
    __name__,
    name='Data',
    top_nav=True,
    path='/data'
)


def load_data(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    grandparent_dir = os.path.abspath(os.path.join(script_dir, os.pardir, os.pardir))  # Go to the grandparent directory
    file_path = os.path.join(grandparent_dir, filename)
    return pd.read_csv(file_path)


raw_data = load_data('crashes-raw.csv')
processed_data = load_data('crashes-processed.csv')


def layout():
    return html.Div([
        dbc.ButtonGroup(
            [
                dbc.Button("Raw Data", id="raw-button", n_clicks=0),
                dbc.Button("Processed Data", id="processed-button", n_clicks=0)
            ],
            style={'margin': '20px'}
        ),
        html.Div(id='data-table-container'),
        html.Div([
            dbc.Button("Export to CSV", id="export-csv-button", className="mr-2"),
            dbc.Button("Export to PDF", id="export-pdf-button")
        ], style={'margin': '20px'})
    ])


@callback(
    Output('data-table-container', 'children'),
    Output('raw-button', 'style'),
    Output('processed-button', 'style'),
    State('data-table-container', 'data-last'),
    [Input('raw-button', 'n_clicks'),
     Input('processed-button', 'n_clicks')]
)
def update_table_and_buttons(raw_clicks, processed_clicks, last_data):
    triggered = [t['prop_id'] for t in dash.callback_context.triggered]
    data = raw_data if 'raw-button.n_clicks' in triggered else processed_data
    style = {'background-color': 'lightblue'} if 'raw-button.n_clicks' in triggered else {
        'background-color': 'darkgrey'}
    other_style = {'background-color': 'darkgrey'} if 'raw-button.n_clicks' in triggered else {
        'background-color': 'lightblue'}
    return dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in data.columns],
        data=data.to_dict('records'),
        page_size=20,
        style_table={'height': '700px', 'overflowY': 'auto'},
        filter_action='native',
        sort_action='native',
        sort_mode='multi',
        page_action='native',
        style_cell={'textAlign': 'left', 'minWidth': '100px', 'width': '150px', 'maxWidth': '200px'},
        style_header={'backgroundColor': 'white', 'fontWeight': 'bold'}
    ), style, other_style


@callback(
    Output('export-csv-button', 'n_clicks'),
    [Input('export-csv-button', 'n_clicks')],
    prevent_initial_call=True
)
def export_csv(n_clicks):
    if n_clicks:
        data = processed_data if 'processed-button.n_clicks' > 'raw-button.n_clicks' else raw_data
        data.to_csv('exported_data.csv', index=False)
        return send_file('exported_data.csv', as_attachment=True)


@callback(
    Output('export-pdf-button', 'n_clicks'),
    [Input('export-pdf-button', 'n_clicks')],
    prevent_initial_call=True
)
def export_pdf(n_clicks):
    if n_clicks:
        data = processed_data if 'processed-button.n_clicks' > 'raw-button.n_clicks' else raw_data
        data.to_html('temp.html')
        pdfkit.from_file('temp.html', 'exported_data.pdf')
        return send_file('exported_data.pdf', as_attachment=True)

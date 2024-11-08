from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import dash_ag_grid as dag
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/US-Exports/2011_us_ag_exports.csv')

app = Dash(__name__)
server = app.server
app.layout = html.Div([
   html.Div(id="my-title", children="Us Agricultural Exports in 2011"),
   dcc.Dropdown(id="state-dropdown", options=df.state.unique(), value=["Alabama","Arkansas"], multi=True),
   html.Button(children='Submit', id='state-btn'),
   dcc.Graph(id="graph1"),
])

@app.callback(
   Output(component_id='graph1', component_property='figure'),
   State(component_id='state-dropdown', component_property='value'),
   Input('state-btn', 'n_clicks'),
   # prevent_initial_call=True
)
def update_graph(states_selected, click):
    print(type(click))
    df_states = df[df.state.isin(states_selected)]
    fig1 = px.bar(data_frame=df_states, x='state', y=['beef','pork','fruits fresh'])
    return fig1


if __name__ == '__main__':
  app.run(debug=True, port=8007)

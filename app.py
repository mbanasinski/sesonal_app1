import pandas
import Probability_sesonal_pattern as probanility
import Cumulative_Sesonal_pattern as cumulative
import dash
from dash import dcc
from dash import html
from  dash import Input
from dash import Output
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd
import data_managment_functions as data_managment
''' 
df = pd.read_pickle("dafr.pkl")
fig = px.line(df, x='Data', y='Close' ,title='Stock chart')
plotly.offline.plot(fig, filename='fig.html')
'''

instrument = 'Gold'
app = dash.Dash()
Years = [10 , 30]
df = pandas.DataFrame(Years, columns=['Years'])
app.layout = html.Div([
    html.H1(children="MARKET SESONALITY", id='header'),
    html.Label("Select an instrument"),
    html.Div(
        dcc.Dropdown(
            options= data_managment.list_of_instruments,
            id='Instrument_Dropdown'
        )
    )    ,
    html.Div(
            children=html.Div([
            html.Div(dcc.Graph(figure=data_managment.fig_cumulative_10(instrument)), id='aaa' ),
            html.Div(dcc.Graph(figure=data_managment.fig_cumulative_30(instrument) )),
            html.Div(dcc.Graph(figure=data_managment.fig_probability_20(instrument))),
            html.Div(dcc.Graph(figure=data_managment.fig_probability_60(instrument))),
       ])
    , id='charts')




])



#def update_figure():


@app.callback(
    Output(component_id='charts', component_property='children'),
    Input(component_id='Instrument_Dropdown', component_property='value'))



def update_charts(value):
    children =html.Div([
            html.Div(dcc.Graph(figure=data_managment.fig_cumulative_10(str(value)))),
            html.Div(dcc.Graph(figure=data_managment.fig_cumulative_30(str(value)))),
            html.Div(dcc.Graph(figure=data_managment.fig_probability_20(str(value)))),
            html.Div(dcc.Graph(figure=data_managment.fig_probability_60(str(value))))
       ])
    return children

if __name__=="__main__":
    #from waitress import serve
    #serve(app, host='0.0.0.0', port=8080)
    app.run_server()





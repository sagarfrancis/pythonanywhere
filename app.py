#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('bmh')
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#server=app.server


data11=pd.read_csv("/home/sagar/pythonanywhere/data1.csv")
sensordata1_daily = data11.set_index('GMTDATE_GMTTIME')

temp_Kitchen=(sensordata1_daily[sensordata1_daily["LOCATION"]=="Kitchen"].loc['2020-10-14 00:00:00':'2020-10-31 23:59:59', 'TEMPR']).copy()
temp_Office=(sensordata1_daily[sensordata1_daily["LOCATION"]=="Office"].loc['2020-10-14 00:00:00':'2020-10-31 23:59:59', 'TEMPR']).copy()
temp_Laundry_Room=(sensordata1_daily[sensordata1_daily["LOCATION"]=="Laundry Room"].loc['2020-10-14 00:00:00':'2020-10-31 23:59:59', 'TEMPR']).copy()
temp_Living_Room=(sensordata1_daily[sensordata1_daily["LOCATION"]=="Living Room"].loc['2020-10-14 00:00:00':'2020-10-31 23:59:59', 'TEMPR']).copy()
temp_Main_Washroom=(sensordata1_daily[sensordata1_daily["LOCATION"]=="Main Washroom"].loc['2020-10-14 00:00:00':'2020-10-31 23:59:59', 'TEMPR']).copy()
temp_Master_Bedroom=(sensordata1_daily[sensordata1_daily["LOCATION"]=="Master Bedroom"].loc['2020-10-14 00:00:00':'2020-10-31 23:59:59', 'TEMPR']).copy()
temp_Master_Bedroom_Ensuite=(sensordata1_daily[sensordata1_daily["LOCATION"]=="Master Bedroom Ensuite"].loc['2020-10-14 00:00:00':'2020-10-31 23:59:59', 'TEMPR']).copy()

humid_Kitchen=(sensordata1_daily[sensordata1_daily["LOCATION"]=="Kitchen"].loc['2020-10-14 00:00:00':'2020-10-31 23:59:59', 'HUMID'])
humid_Office=(sensordata1_daily[sensordata1_daily["LOCATION"]=="Office"].loc['2020-10-14 00:00:00':'2020-10-31 23:59:59', 'HUMID'])
humid_Laundry_Room=(sensordata1_daily[sensordata1_daily["LOCATION"]=="Laundry Room"].loc['2020-10-14 00:00:00':'2020-10-31 23:59:59', 'HUMID'])
humid_Living_Room=(sensordata1_daily[sensordata1_daily["LOCATION"]=="Living Room"].loc['2020-10-14 00:00:00':'2020-10-31 23:59:59', 'HUMID'])
humid_Main_Washroom=(sensordata1_daily[sensordata1_daily["LOCATION"]=="Main Washroom"].loc['2020-10-14 00:00:00':'2020-10-31 23:59:59', 'HUMID'])
humid_Master_Bedroom=(sensordata1_daily[sensordata1_daily["LOCATION"]=="Master Bedroom"].loc['2020-10-14 00:00:00':'2020-10-31 23:59:59', 'HUMID'])
humid_Master_Bedroom_Ensuite=(sensordata1_daily[sensordata1_daily["LOCATION"]=="Master Bedroom Ensuite"].loc['2020-10-14 00:00:00':'2020-10-31 23:59:59', 'HUMID'])


humid_Kitchen = go.Scatter(x=humid_Kitchen.index,y=humid_Kitchen.values,opacity=0.8,name='humid_Kitchen',yaxis='y2',line=go.scatter.Line(color='blue'))
humid_Office = go.Scatter(x=humid_Office.index,y=humid_Office.values,opacity=0.8,name='humid_Office',yaxis='y2',line=go.scatter.Line(color='red'))
humid_Laundry_Room = go.Scatter(x=humid_Laundry_Room.index,y=humid_Laundry_Room.values,opacity=0.8,name='humid_Laundry_Room',yaxis='y2',line=go.scatter.Line(color='black'))
humid_Living_Room = go.Scatter(x=humid_Living_Room.index,y=humid_Living_Room.values,opacity=0.8,name='humid_Living_Room',yaxis='y2',line=go.scatter.Line(color='yellow'))
humid_Main_Washroom = go.Scatter(x=humid_Main_Washroom.index,y=humid_Main_Washroom.values,opacity=0.8,name='humid_Main_Washroom',yaxis='y2',line=go.scatter.Line(color='green'))
humid_Master_Bedroom = go.Scatter(x=humid_Master_Bedroom.index,y=humid_Master_Bedroom.values,opacity=0.8,name='humid_Master_Bedroom',yaxis='y2',line=go.scatter.Line(color='pink'))
humid_Master_Bedroom_Ensuite = go.Scatter(x=humid_Master_Bedroom_Ensuite.index,y=humid_Master_Bedroom_Ensuite.values,opacity=0.8,name='humid_Master_Bedroom_Ensuite',yaxis='y2',line=go.scatter.Line(color='orange'))

# Create the same data object
temp_Kitchen = go.Scatter(x=temp_Kitchen.index,
                        y=temp_Kitchen.values,
                        line=go.scatter.Line(color='blue', width = 0.6),
                           opacity=0.8,
                           name='temp_Kitchen',
                           )
temp_Office = go.Scatter(x=temp_Office.index,
                        y=temp_Office.values,
                       line=go.scatter.Line(color='red', width = 0.6),opacity=1,name='temp_Office',)
temp_Laundry_Room = go.Scatter(x=temp_Laundry_Room.index,
                        y=temp_Laundry_Room.values,
                       line=go.scatter.Line(color='black', width = 0.6),opacity=1,name='temp_Laundry_Room',)
temp_Living_Room = go.Scatter(x=temp_Living_Room.index,
                        y=temp_Living_Room.values,
                       line=go.scatter.Line(color='yellow', width = 0.6),opacity=1,name='temp_Living_Room',)
temp_Main_Washroom = go.Scatter(x=temp_Main_Washroom.index,
                        y=temp_Main_Washroom.values,
                       line=go.scatter.Line(color='green', width = 0.6),opacity=1,name='temp_Main_Washroom',)
temp_Master_Bedroom = go.Scatter(x=temp_Master_Bedroom.index,
                        y=temp_Master_Bedroom.values,
                       line=go.scatter.Line(color='pink', width = 0.6),opacity=1,name='temp_Master_Bedroom',)
temp_Master_Bedroom_Ensuite = go.Scatter(x=temp_Master_Bedroom_Ensuite.index,
                        y=temp_Master_Bedroom_Ensuite.values,
                       line=go.scatter.Line(color='orange', width = 0.6),opacity=1,name='temp_Master_Bedroom_Ensuite',)

# Create a layout with a rangeselector and rangeslider on the xaxis
layout = go.Layout(height=1400, width=1600, font=dict(size=15),
                   title='Temparature and Humidity Plots with Range Selection',
                   xaxis=dict(title='Date',
                                        # Range selector with buttons
                                         rangeselector=dict(
                                             # Buttons for selecting time scale
                                             buttons=list([
                                                 # 1 month
                                                 dict(count=1,
                                                      label='1m',
                                                      step='month',
                                                      stepmode='backward'),
                                                 # 1 week
                                                 dict(count=7,
                                                      label='1w',
                                                      step='day',
                                                      stepmode='todate'),
                                                 # 1 day
                                                 dict(count=1,
                                                      label='1d',
                                                      step='day',
                                                      stepmode='todate'),
                                                 # 12 hours
                                                 dict(count=12,
                                                      label='12h',
                                                      step='hour',
                                                      stepmode='backward'),
                                                 # 4 hours
                                                 dict(count=4,
                                                      label='4h',
                                                      step='hour',
                                                      stepmode='backward'),
                                                 dict(count=1,
                                                     label='1h',
                                                     step='hour',
                                                     stepmode='backward'),
                                                 # Entire scale
                                                 dict(step='all')
                                             ])
                                         ),
                                         # Sliding for selecting time window
                                         rangeslider=dict(visible=True),
                                         # Type of xaxis
                                         type='date'),
                   # yaxis is unchanged
                   yaxis=dict(title='Temp'),
                   # Add a second yaxis to the right of the plot
                   yaxis2=dict(title='Humidity', color='blue',
                                          overlaying='y',
                                          side='right')
                   )

# Create the figure and display
fig = go.Figure(data=[temp_Kitchen,humid_Kitchen,temp_Office,humid_Office,temp_Laundry_Room,temp_Living_Room,humid_Laundry_Room,humid_Living_Room,
                      temp_Main_Washroom,humid_Main_Washroom,
                     temp_Master_Bedroom,humid_Master_Bedroom,temp_Master_Bedroom_Ensuite,humid_Master_Bedroom_Ensuite], layout=layout)


app.layout = html.Div(children=[
    html.H1(children='Temperature Plot'),

    html.Div(children='''
        Dash: All categories.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)




# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:44:07 2019

@author: YP
"""

from pandas_datareader import data
from datetime import datetime
from bokeh.io import output_file, show
from bokeh.plotting import figure


df = data.DataReader(name='AMZN',data_source='stooq')

df = df.head(75)

def inc_dec(c,o):
    if c > o:
        value = "Increase"
    elif o > c:
        value = "Decrease"
    else:
        value = "Equal"
    return value

df['Status'] = [inc_dec(c,o) for c,o in zip(df.Close,df.Open)]
df["Middle"] = (df.Close + df.Open)/2
df["Height"] = abs(df.Close - df.Open)
print(df)



f = figure(x_axis_type='datetime', width=1000,height=500)

hours_12 = 12*60*60*1000
f.title.text = "Stock Price Chart"

f.segment(df.index,df.High,df.index,df.Low,color='Black')

f.rect(df.index[df.Status == 'Increase'],df.Middle[df.Status == 'Increase'],hours_12,df.Height[df.Status == 'Increase'],
               fill_color="Gray",line_color='Black')

f.rect(df.index[df.Status == 'Decrease'],df.Middle[df.Status == 'Decrease'],hours_12,df.Height[df.Status == 'Decrease'],
               fill_color = "Orange",line_color = 'Black')



output_file("StockPrice.html")


show(f)



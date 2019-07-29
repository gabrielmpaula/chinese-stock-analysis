# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 01:29:22 2017

@author: Gabriel
"""

import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, ColumnDataSource
from bokeh.models import Range1d, HoverTool
from bokeh.io import output_notebook
output_notebook()

intCodes = np.genfromtxt('codes.csv',delimiter=';',dtype=str)

i = 76
fData = pd.read_csv(intCodes[i],delimiter='\t')
fData['Stock'] = intCodes[i].astype(str)
fData['Index'] = i
fData = fData.iloc[::-1,:]
fData = fData.set_index("date")
fData['ma5-ma20'] = fData['ma5'] - fData['ma20']
fData["Regime"] = np.where(fData['ma5-ma20'] > 0, 1, 0)
fData["Regime"] = np.where(fData['ma5-ma20'] < 0, -1, fData["Regime"])
fData["Signal"] = np.sign(fData["Regime"] - fData["Regime"].shift(1))
Stock_Info = fData.loc[(fData['Signal'] == 1) | (fData['Signal'] == -1) ]
Stock_Info = {'Signal': Stock_Info['Signal'], 'Stock':Stock_Info['Stock'], 'Index':Stock_Info['Index']}
Stock_Info = pd.DataFrame(Stock_Info)

fData.loc[:,"ma5"].plot(ylim = (10,12)).axhline(y = 0, color = "black", lw = 2)
fData.loc[:,"ma20"].plot().axhline(y = 0, color = "black", lw = 2)

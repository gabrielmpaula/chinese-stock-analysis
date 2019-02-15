# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 14:19:47 2017

@author: Gabriel
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

intCodes = np.genfromtxt('codes.csv',delimiter=';',dtype=str)

i = 0


col_to_use = ['open','close','high','low','date','ma5','ma10','ma20']

for i in range(0,3162):
    fData = pd.read_csv(intCodes[i]+".txt",delimiter='\t',usecols = col_to_use)
    fData['Stock'] = intCodes[i].astype(str)
    fData['Index'] = i
    fData = fData.iloc[::-1,:]
    fData = fData.tail(15)
    fData = fData.set_index("date")
    fData['ma5-ma20'] = fData['ma5'] - fData['ma20']
    
    fData['ma5 variation'] = (fData['ma5'] - fData['ma5'].shift(-1))/fData['ma5'].shift(-1)
    fData['ma20 variation'] = (fData['ma20'] - fData['ma20'].shift(-1))/fData['ma20'].shift(-1)

    fData["Regime"] = np.where(fData['ma5-ma20'] > 0, 1, 0)
    fData["Regime"] = np.where(fData['ma5-ma20'] < 0, -1, fData["Regime"])
    fData["Regime"].plot(ylim = (-2,2)).axhline(y = 0, color = "black", lw = 2)
    fData["Signal"] = np.sign(fData["Regime"] - fData["Regime"].shift(1))
    fData["Signal"].plot(ylim = (-2,2)).axhline(y = 0, color = "black", lw = 2)
    """
    Stock_Buy = fData.loc[fData['Signal'] == 1]
    Stock_Sell = fData.loc[fData['Signal'] == -1]
    
    Stock_Buy = {'Signal': Stock_Buy['Signal'], 'Stock':Stock_Buy['Stock'], 'Index':Stock_Buy['Index']}
    Stock_Sell = {'Signal': Stock_Sell['Signal'], 'Stock':Stock_Sell['Stock'], 'Index':Stock_Sell['Index']}
    
    Stock_Buy = pd.DataFrame(Stock_Buy)
    Stock_Sell = pd.DataFrame(Stock_Sell)
    """
    
    if i == 0:
        Stock_Data = fData
        """"
        Bull_Dates = Stock_Buy
        Bear_Dates = Stock_Sell
        """
    else:
        Stock_Data = Stock_Data.append(fData)
        """
        Bull_Dates = Bull_Dates.append(Stock_Buy)
        Bear_Dates = Bear_Dates.append(Stock_Sell)
        """

Stock_Data.to_csv("Stock_Data.txt",sep="\t")

"""        
Bull_Dates.to_csv('Stock_Bull_Dates.txt',sep='\t')
Bear_Dates.to_csv('Stock_Bear_Dates.txt',sep='\t')

fData.loc[:,"ma"].plot(ylim = (-1,1)).axhline(y = 0, color = "black", lw = 2)
intSize = len(fData["Regime"]) -1 
regime_orig = fData.ix[intSize, "Regime"]
fData.ix[intSize, "Regime"] = 0
fData.ix[0, "Regime"] = regime_orig
"""



# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 23:56:59 2017

@author: Gabriel
"""

import numpy as np
import pandas as pd

intCodes = np.genfromtxt('codes.csv',delimiter=';',dtype=str)
i=0

"""
import datetime
"""
df = []
for i in range (0,3162):
    
    fData = pd.read_csv(intCodes[i]+".txt",delimiter='\t')
    if fData.empty:
        continue
    """
    fData['Year'] = fData['date'].str[:4].astype(int)
    fData['Month'] = fData['date'].str[5:7].astype(int)
    fData['Day'] = fData['date'].str[8:10].astype(int)
    """
    
    fData['date'] = fData['date'] = pd.to_datetime(fData['date'])
    fData['week'] = fData['date'].dt.week
    fData['weekday'] = fData['date'].dt.weekday
    
    fData['variation'] = (fData['high'] - fData['low'])/fData['low']
    Stock_Variation = fData.groupby('week', as_index=True)['variation'].std()
    Stock_Variation = pd.Series.to_frame(Stock_Variation)
    Stock_Variation['stocks'] = intCodes[i]
    
    Stock_Variation['maximum'] = fData.groupby('week', as_index=True)['high'].max()
    Stock_Variation['minimum'] = fData.groupby('week', as_index=True)['low'].min()

    Stock_Variation['open'] = fData.groupby('week', as_index=True)['open'].mean()
    Stock_Variation['close'] = fData.groupby('week', as_index=True)['close'].mean()
    Stock_Variation['high'] = fData.groupby('week', as_index=True)['high'].mean()
    Stock_Variation['low'] = fData.groupby('week', as_index=True)['low'].mean()

    
    
    Friday_Closing = fData.loc[fData['weekday'] == 4]
    Friday_Closing = Friday_Closing.set_index('week')
    Stock_Variation['closing'] = Friday_Closing['close']
    Stock_Variation['price variation %'] = (Stock_Variation['maximum'] - Stock_Variation['closing'].shift(1))/Stock_Variation['closing'].shift(1)

    """
    mean = fData['close'].mean()
    std = fData['close'].std()
    roi = (fData['close']+1).prod()-1
    df.append({'Stock': intCodes[i], 'Mean': mean, 'Std': std, 'Roi': roi})
    
    stats = pd.DataFrame(df)
    stats = stats.set_index('Stock')

    extremes = pd.concat((stats.idxmax(),stats.max()),axis=1)
    extremes.columns = ['Maximizer','Maximum']
    extremes
    print(mean)
    print(std)
    print(roi)
    """
    
    if i == 0:
        Stock_Info = Stock_Variation
    else:
        Stock_Info = Stock_Info.append(Stock_Variation)
        
Stock_Info.to_csv('Stock_Information.txt',sep='\t')

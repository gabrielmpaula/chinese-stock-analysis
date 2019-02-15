# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 14:39:40 2017

@author: Gabriel
"""

import numpy as np
import pandas as pd
import tushare as ts

code = '300231'

Stock = ts.get_hist_data(code,start='2017-12-07',end='2017-12-07)
i = 0
intStockCodes = []

intCodes = np.genfromtxt('codes.csv',delimiter=';',dtype=str)

for i in range(0,3549):
    fData = pd.read_csv(intCodes[i],delimiter='\t')
    if fData.empty:
        continue
    else:
        intStockCodes.append(intCodes[i])

intStockCodes = pd.DataFrame(intStockCodes)
intStockCodes.columns = ['codes']

intStockCodes.to_csv('New_Codes.txt',sep='\t')

"""
Created on Fri Dec 15 22:52:24 2017

@author: Gabriel
"""


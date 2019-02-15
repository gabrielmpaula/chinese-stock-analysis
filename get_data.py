# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import tushare as ts
import numpy as np
import time

sCodes = np.genfromtxt('codes.csv',delimiter=';',dtype=str)

"""
ts.get_industry_classified()
ts.get_k_data('600103', start='2015-07-11', end='2015-12-11',index='true') 
"""

intRange = len(sCodes) - 1

i = 0

for i in range(3162,intRange):
    
    if i == 1360:
        print(1)
    else:
        s = ts.get_hist_data(sCodes[i], start='2017-07-15', end='2017-12-22')     
        s.to_csv(sCodes[i]+".txt", sep='\t')
        time.sleep(8)

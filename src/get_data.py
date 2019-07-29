import tushare as ts
import numpy as np
import time

stock_codes = np.genfromtxt('..\data\codes.csv',delimiter=';',dtype=str)
total_codes = len(stock_codes)
i = 0
for code in stock_codes:
    i += 1
    print('Downloading stock "{}" data. {} out of {}'.format(code, i, total_codes)) 
    try:
    	s = ts.get_hist_data(code, start='2017-07-15', end='2017-12-22')     
    	s.to_csv('../data/stock-data/'+ code + '.csv', sep='\t')
    except:
        print('Code {} not found'.format(code))
    time.sleep(8)

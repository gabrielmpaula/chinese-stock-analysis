import numpy as np
import pandas as pd

stock_codes = pd.read_csv('../data/codes.csv', header=0, squeeze=True, dtype=str)
working_codes = []

for code in stock_codes:
    fData = pd.read_csv(code + '.csv')
    if fData.empty:
        continue
    else:
        working_codes.append(code)

working_codes = pd.DataFrame({'codes': working_codes})
working_codes.to_csv('..data/new_codes.csv')

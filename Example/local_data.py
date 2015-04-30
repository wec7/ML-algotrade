"""
Copyright: Copyright (C) 2015 Baruch College - MTH 9899 Machine Learning
Description: Example code to access data
"""

# QSTK Imports

import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

# Third Party Imports

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

def main():
    ''' Main Function'''

    # read data parameters
    ls_symbols = ["AAPL", "GLD", "GOOG", "$SPX", "XOM"]
    dt_start = dt.datetime(2006, 1, 1)
    dt_end = dt.datetime(2010, 12, 31)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))
    c_dataobj = da.DataAccess('Yahoo')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    # Reading the data, now d_data is a dictionary with the keys above.
    # Timestamps and symbols are the ones that were specified before.

    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))

    # Getting the numpy ndarray of close prices.
    
    na_price = d_data['close'].values

    # Plotting the prices with x-axis=timestamps

    plt.clf()
    plt.plot(ldt_timestamps, na_price)
    plt.legend(ls_symbols)
    plt.ylabel('Adjusted Close')
    plt.xlabel('Date')
    plt.savefig('adjustedclose.pdf', format='pdf')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:11:32 2020

ctypecodes@gmail.com
"""

import senator_trading as st

#%% initialize trades object
trades_obj = st.Trades()

#%% load the publicly available data from the internet
all_trades_list = trades_obj.load_trades()

#%% build trades DataFrame...required for plotting
all_trades_df = trades_obj.build_trade_df(all_trades_list)

#%% sample plot of the data
fig, ax = trades_obj.plot_trade_vol()


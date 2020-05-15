#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 16:30:20 2020

ctypecodes@gmail.com
"""

import requests
import datetime
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt


#%% Define classes

class Trade:
    def __init__(self, stock, date, senator, action, amount, party):
        self.stock = stock
        self.date = date
        self.senator = senator
        self.action = action
        self.amount = amount
        self.party = party


class Trades:
    
    def build_trade_df(self, trades_list):
        """
        build pandas data frame of trades
        """
        df = pd.DataFrame(data=[],columns=['date', 'stock', 'senator', 'action', 'amount', 'party'])
        
        for i, trade in enumerate(trades_list):
            df_curr = pd.DataFrame(data=[[trade.date, trade.stock, trade.senator, trade.action, trade.amount, trade.party]], columns=['date', 'stock', 'senator', 'action', 'amount', 'party'])
            df = pd.concat([df, df_curr], ignore_index = True)
            
        self.trades_df = df
        
        return df
    
    def load_trades(self):
        """
        Loads raw data from website and returns a list of Trade objects
        """
        site_url = 'https://www.quiverquant.com/sources/senatetrading'
        site_raw = requests.get(site_url)
        site_lines = site_raw.text.splitlines()
        
        trade_start_lines = []
        for i, line in enumerate(site_lines):
            found = line.find('<tr class="">')
            if found > 0:
                trade_start_lines.append(i)
                
        trade_end_lines = []
        for i, line in enumerate(site_lines):
            found = line.find('</tr>')
            if found > 0:
                trade_end_lines.append(i)

        self.trades_list = []
        
        for trade_block in trade_start_lines:
            #stock
            line = site_lines[trade_block+1]
            lstart = line.find(';">')
            lstart = lstart + 3
            lstop = line.find('</td>')
            stock = line[lstart:lstop]
            #date
            line = site_lines[trade_block+2]
            lstart = line.find('</p>')
            lstart = lstart + 4
            lstop = line.find('</td>')
            date_str = line[lstart:lstop]
            date = datetime.datetime.strptime(date_str, '%m/%d/%Y')
            #senator
            line = site_lines[trade_block+3]
            lstart = line.find(';">')
            lstart = lstart + 3
            lstop = line.find('</td>')
            senator = line[lstart:lstop]
            #action
            line = site_lines[trade_block+4]
            lstart = line.find(';">')
            lstart = lstart + 3
            lstop = line.find('</td>')
            action_str = line[lstart:lstop]
            if action_str == 'Purchase':
                action = 'P'
            else:
                action = 'S'
            #amount
            line = site_lines[trade_block+5]
            lstart = line.find(';">')
            lstart = lstart + 3
            lstop = line.find('</td>')
            amount_str = line[lstart:lstop]
            amount_str_split = amount_str.split('-')
            low_amount_str = amount_str_split[0][1:]
            low_amount_str_stripped = low_amount_str.strip()
            low_amount = float(low_amount_str_stripped.replace(',',''))
            high_amount_str_stripped = amount_str_split[-1].strip()
            high_amount_str = high_amount_str_stripped[1:]
            high_amount = float(high_amount_str.replace(',',''))
            amount = 0.5 * (low_amount + high_amount)
            #party
            line = site_lines[trade_block+6]
            lstart = line.find(';">')
            lstart = lstart + 3
            lstop = line.find('</td>')
            party = line[lstart:lstop]
            
            self.trades_list.append(Trade(stock, date, senator, action, amount, party))
            
        return self.trades_list
    
        
    


#%% plotting functions
        
    def plot_trade_vol(self):
        df = self.trades_df
        trading_dates = df['date'].unique()
        
        day_amounts = np.zeros(len(trading_dates))
        
        for i, date in enumerate(trading_dates):
            df_amount = df['amount'][df['date']==date]
            day_amounts[i] = df_amount.sum()
        
        fig, ax = plt.subplots()
        ax.bar(trading_dates, day_amounts)
        ax.set_yscale('log')
        ax.grid('True')
        
        ax.set_title('Trading Volume Over Time')
        ax.set_xlabel('Dates')
        ax.set_ylabel('Trading Volume [$]')
        plt.show()
        return [fig, ax]



##%% trades last month
#
#today = datetime.datetime.now()
#days_30 = datetime.timedelta(days=30)
#last_month = today - days_30
#
#df_last_month = df[df['date']>=last_month]
#
#traded_stocks = df_last_month['stock'].unique()
#
#col_names = ['stock', 'amount', 'action', 'n_senator']
#df_stocks_sorted = pd.DataFrame(data=np.zeros((len(traded_stocks), len(col_names))),columns=col_names)
#
#for i, stock in enumerate(traded_stocks):
#    df_stock = df_last_month[df_last_month['stock']==stock]
#    df_interim = pd.DataFrame(data=[stock, df_stock['amount'].sum(), 0, len(df_stock['senator'].unique())], columns=col_names)
#    df_stocks_sorted = pd.concat([df_stocks_sorted, df_interim])

senator_trading
-----

Reads in publicly available information on stock trading activity of US senators.

Can be installed via pip:
pip install senator_trading

To use, do (or run sample_script.py):
import senator_trading as st
trades_obj = st.Trades()
all_trades_list = trades_obj.load_trades()
all_trades_df = trades_obj.build_trade_df(all_trades_list)
fig, ax = trades_obj.plot_trade_vol()



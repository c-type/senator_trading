# senator_trading

## What it does
Reads in publicly available information on stock trading activity of US senators.

## How to Install
Can be installed via pip:
```
pip install senator_trading
```

## How to run
To use, do (or run sample_script.py) in python:

```
import senator_trading as st

trades_obj = st.Trades()

all_trades_list = trades_obj.load_trades()

all_trades_df = trades_obj.build_trade_df(all_trades_list)

fig, ax = trades_obj.plot_trade_vol()

```

## Example Output
![Alt text](trading_volume.png?raw=true "Title")

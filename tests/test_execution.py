from unittest import TestCase

import senator_trading as st

class TestSenatorTrading(TestCase):
    def test_successful_data_loading(self):
        return_value = 0
        #%% initialize trades object
        trades_obj = st.Trades()
        #%% load the publicly available data from the internet
        all_trades_list = trades_obj.load_trades()
        return_value = len(all_trades_list)
        self.assertTrue(return_value > 0)

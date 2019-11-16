import numpy as np
import pandas as pd
df=pd.read_csv('market_data.csv', sep=',',header=None)
# df.values
# my_data = np.genfromtxt('market_data.csv', delimiter=',', dtype=None)

data = df.values[1:]

esx_data = data[data[:,1]=='ESX-FUTURE']
esx_bid_price = np.asarray(list(map(float, esx_data[:,2])))
esx_bid_vol = np.asarray(list(map(float, esx_data[:,3])))
esx_ask_price = np.asarray(list(map(float, esx_data[:,4])))
esx_ask_vol = np.asarray(list(map(float, esx_data[:,5])))

sp_data = data[data[:,1]=='SP-FUTURE']
sp_bid_price = np.asarray(list(map(float, sp_data[:,2])))
sp_bid_vol = np.asarray(list(map(float, sp_data[:,3])))
sp_ask_price = np.asarray(list(map(float, sp_data[:,4])))
sp_ask_vol = np.asarray(list(map(float, sp_data[:,5])))

# not for time adjusted correlation is 0.664 .. not that high

corr = np.corrcoef(esx_bid_price[:11000], sp_bid_price[:11000])
print(corr)

# sp price: ~3360
# esx price: ~2910
def act_on_between_stock_correlation():
    while True:
        if esx_went_up_for_three_ticks and sp_did_not_go_up:
            buy_sp()
        elif sp_went_up_for_three_ticks and esx_did_not_go_up:
            buy_esx()
        elif esx_went_down_for_three_ticks and sp_did_not_go_down:
            sell_sp()
        elif sp_went_down_for_three_ticks and esx_did_not_go_down:
            sell_esx()







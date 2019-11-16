import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

plt.figure()
norm_esx_bid = esx_bid_price / np.linalg.norm(esx_bid_price)
norm_sp_bid = sp_bid_price / np.linalg.norm(sp_bid_price)

x_ticks_esx = np.arange(len(esx_bid_price))
x_ticks_sp = np.arange(len(sp_bid_price))
plt.title('normalized bid prices')
plt.plot(x_ticks_esx, norm_esx_bid)
plt.plot(x_ticks_sp, norm_sp_bid)
plt.bar(x_ticks_esx, esx_bid_vol)
plt.bar(x_ticks_sp, sp_bid_vol)
plt.show()

# plt.title('unnormalized bid prices')
# plt.plot(np.arange(len(esx_bid_price)), esx_bid_price)
# plt.plot(np.arange(len(sp_bid_price)), sp_bid_price)
# plt.show()
# not for time adjusted correlation is 0.664 .. not that high

# n = 10
# for i in range(int(len(esx_bid_price))):
#     corr = np.corrcoef(esx_bid_price[i:i+10], sp_bid_price[1:11000])
#     print(corr)


corr = np.corrcoef(esx_bid_price[:11000], sp_bid_price[:11000])

# def time_stamp_to_seconds(string, offset=0):
#     strArray = string.split(':')
#     floatArray = [float(x) for x in strArray]
#     seconds = float(floatArray[2]+60*(time))

# # sp price: ~3360
# # esx price: ~2910
# def act_on_between_stock_correlation():
#     while True:
#         if esx_went_up_for_three_ticks and sp_did_not_go_up:
#             buy_sp()
#         elif sp_went_up_for_three_ticks and esx_did_not_go_up:
#             buy_esx()
#         elif esx_went_down_for_three_ticks and sp_did_not_go_down:
#             sell_sp()
#         elif sp_went_down_for_three_ticks and esx_did_not_go_down:
#             sell_esx()







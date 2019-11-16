import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def time_stamp_to_seconds(string, offset=0):
    strArray = string.split(':')
    floatArray = [float(x) for x in strArray]
    seconds = float(floatArray[2] + 60 * ( floatArray[1] + 60 * floatArray[0]) - offset)
    return seconds

df=pd.read_csv('market_data.csv', sep=',',header=None)
df2=pd.read_csv('trades.csv', sep=',',header=None)
# df.values
# my_data = np.genfromtxt('market_data.csv', delimiter=',', dtype=None)

data = df.values[1:]
data2 =  df2.values[1:]

timeOffset = time_stamp_to_seconds(data[0][0])
data[:,0] = [time_stamp_to_seconds(x, offset=timeOffset) for x in data[:,0]]
data2[:,0] = [time_stamp_to_seconds(x, offset=timeOffset) for x in data2[:,0]]

esx_data = data[data[:,1]=='ESX-FUTURE']
esx_bid_price = np.asarray(list(map(float, esx_data[:,2])))
esx_bid_vol = np.asarray(list(map(float, esx_data[:,3])))
esx_ask_price = np.asarray(list(map(float, esx_data[:,4])))
esx_ask_vol = np.asarray(list(map(float, esx_data[:,5])))
esx_time_secs = np.asarray(esx_data[:,0])

sp_data = data[data[:,1]=='SP-FUTURE']
sp_bid_price = np.asarray(list(map(float, sp_data[:,2])))
sp_bid_vol = np.asarray(list(map(float, sp_data[:,3])))
sp_ask_price = np.asarray(list(map(float, sp_data[:,4])))
sp_ask_vol = np.asarray(list(map(float, sp_data[:,5])))
sp_time_secs = np.asarray(sp_data[:,0])

norm_esx_bid = esx_bid_price / np.linalg.norm(esx_bid_price)
norm_sp_bid = sp_bid_price / np.linalg.norm(sp_bid_price)

esx_bid_trades = [x for x in data2 if x[1]=='ESX-FUTURE' and x[2]=='BID']
esx_ask_trades = [x for x in data2 if x[1]=='ESX-FUTURE' and x[2]=='ASK']
sp_bid_trades = [x for x in data2 if x[1]=='SP-FUTURE' and x[2]=='BID']
sp_ask_trades = [x for x in data2 if x[1]=='SP-FUTURE' and x[2]=='ASK']

esx_bid_trades[:,3] = [float(x) for x in esx_bid_trades[:,3]]
esx_ask_trades[:,3] = [float(x) for x in esx_ask_trades[:,3]]
sp_bid_trades[:,3] = [float(x) for x in sp_bid_trades[:,3]]
sp_ask_trades[:,3] = [float(x) for x in sp_ask_trades[:,3]]

plt.figure()
plt.plot(sp_time_secs, norm_sp_bid, label="SP")
plt.plot(esx_time_secs, norm_esx_bid, label="ESX")
plt.plot(esx_bid_trades[0], esx_bid_trades[3], label="ESX bid trades")
plt.plot(sp_bid_trades[0], sp_bid_trades[3], label="SP bid trades")
plt.legend()
plt.show()

'''plt.figure()
norm_esx_bid = esx_bid_price / np.linalg.norm(esx_bid_price)
norm_sp_bid = sp_bid_price / np.linalg.norm(sp_bid_price)

norm_esx_bid_vol = esx_bid_vol / np.linalg.norm(esx_bid_vol)
norm_sp_bid_vol = sp_bid_vol / np.linalg.norm(sp_bid_vol)

x_ticks_esx = np.arange(len(esx_bid_price))
x_ticks_sp = np.arange(len(sp_bid_price))
plt.title('normalized bid prices')
plt.plot(x_ticks_esx, norm_esx_bid)
plt.plot(x_ticks_sp, norm_sp_bid)
plt.bar(x_ticks_esx, esx_bid_vol)
plt.bar(x_ticks_sp, sp_bid_vol)
plt.show()'''

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







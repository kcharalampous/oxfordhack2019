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


# bidPrices['ESX-FUTURE'] = data[data[:,1]=='ESX-FUTURE']
#     # [float(x[2]) for x in data if x[1] == 'ESX-FUTURE']
# bidPrices['SP-FUTURE'] = [float(x[2]) for x in data if x[1] == 'SP-FUTURE']
# askPrices['ESX-FUTURE'] = [float(x[4]) for x in data if x[1] == 'ESX-FUTURE']

# print(my_data[0])

indices = np.arange(len(data))

# plt.figure()
# plt.title("Bid Price against Time")
# plt.plot(np.arange(len(bidPrices['ESX-FUTURE'])), bidPrices['ESX-FUTURE'], label="ESX-FUTURE")
# plt.plot(np.arange(len(bidPrices['SP-FUTURE'])), bidPrices['SP-FUTURE'], label="SP-FUTURE")
# plt.legend()
# plt.show()
#
# plt.figure()
# plt.title("Bid price vs ask price for ESX")
# plt.plot(np.arange(len(bidPrices['ESX-FUTURE'])), bidPrices['ESX-FUTURE'], label="Bid")
# plt.plot(np.arange(len(bidPrices['ESX-FUTURE'])), askPrices['ESX-FUTURE'], label="Ask")
# plt.legend()
# plt.show()



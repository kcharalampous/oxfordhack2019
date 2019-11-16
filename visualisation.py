import numpy as np
import matplotlib.pyplot as plt

my_data = np.genfromtxt('market_data.csv', delimiter=',', dtype=None)

my_data = my_data[1:]

bidPrices = {}
askPrices = {}
bidPrices['ESX-FUTURE'] = [float(x[2]) for x in my_data if x[1]=='ESX-FUTURE']
bidPrices['SP-FUTURE'] = [float(x[2]) for x in my_data if x[1]=='SP-FUTURE']
askPrices['ESX-FUTURE'] = [float(x[4]) for x in my_data if x[1]=='ESX-FUTURE']

print(my_data[0])

indices = np.arange(len(my_data))

plt.figure()
plt.title("Bid Price against Time")
plt.plot(np.arange(len(bidPrices['ESX-FUTURE'])), bidPrices['ESX-FUTURE'], label="ESX-FUTURE")
plt.plot(np.arange(len(bidPrices['SP-FUTURE'])), bidPrices['SP-FUTURE'], label="SP-FUTURE")
plt.legend()
plt.show()

plt.figure()
plt.title("Bid price vs ask price for ESX")
plt.plot(np.arange(len(bidPrices['ESX-FUTURE'])), bidPrices['ESX-FUTURE'], label="Bid")
plt.plot(np.arange(len(bidPrices['ESX-FUTURE'])), askPrices['ESX-FUTURE'], label="Ask")
plt.legend()
plt.show()

import csv
#import matplotlib

wallet= 20000.0
esxPreviousOne= False
esxPreviousTwo= False
esxPreviousPrice= 0
esxBoughtPrice= 0
esxOpenPosition= False
esxStepAmount= 3.0

prev_esx_bids, prev_sp_bids = [], []

def start_autotrader():
    read_csv()

def read_csv():
    """
    Wait for messages from the exchange and
    call handle_message on each of them.
    """
    with open("market_data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        next(csv_reader,None)
        line_count = 0
        for row in csv_reader:
            handle_message_market(row)


# sp price: ~3360
# esx price: ~2910
def act_on_between_stock_correlation():
    while True:
        if prices_went_up_for_last_n_ticks(exs) and sp_did_not_go_up:
            buy_sp()
        elif sp_went_up_for_three_ticks and esx_did_not_go_up:
            buy_esx()
        elif esx_went_down_for_three_ticks and sp_did_not_go_down:
            sell_sp()
        elif sp_went_down_for_three_ticks and esx_did_not_go_down:
            sell_esx()


def prices_went_up_for_last_n_ticks(stock_prices):
    # number of ticks that you want to look at
    n = min(len(stock_prices), 3)
    went_up = False
    went_down = False
    if stock_prices[:-n] > stock_prices[:-n+1]:
        went_down = True
    elif stock_prices[:-n] <= stock_prices[:n+1]:
        went_up = True
    if went_down:
        for i in range(n+1, 1, -1):
            if not stock_prices[:-i] < stock_prices[:-i+1]:
                return False
        return True

    if went_up:
        for i in range(n+1, 1, -1):
            if not stock_prices[:-i] > stock_prices[:-i+1]:
                return False
        return True



def handle_message_market(message):
    global wallet, esxPreviousOne, esxPreviousTwo, esxPreviousPrice, esxBoughtPrice, esxOpenPosition
    comps = message

    if len(comps) == 0:
        print(f"Invalid message received: {message}")
        return

    type = comps[0]

    feedcode = comps[1]
    bid_price = float(comps[2])
    bid_volume = int(comps[3])
    ask_price = float(comps[4])
    ask_volume = int(comps[5])

    if (wallet < 0):
        print ("wallet: ", wallet)
        print ("Bankrupt")
        exit()

    if (feedcode== "ESX-FUTURE"):
        if (esxOpenPosition== False and esxPreviousPrice> ask_price and esxPreviousOne== False and esxPreviousTwo== False):
            wallet-= ask_price*esxStepAmount
            esxOpenPosition= True
            esxBoughtPrice= ask_price
            print ("wallet: ", wallet)

        if (esxOpenPosition== True and bid_price> (esxBoughtPrice+3)):
            wallet+= bid_price*esxStepAmount
            esxOpenPosition= False
            print ("wallet: ", wallet)

        esxPreviousTwo= esxPreviousOne
        if (esxPreviousPrice> ask_price):
            esxPreviousOne= False
        else:
            esxPreviousOne= True

        esxPreviousPrice= ask_price

    #print(f"[PRICE] product: {feedcode} bid: {bid_volume}@{bid_price} ask: {ask_volume}@{ask_price}")

def handle_message_trades(message):
    comps = message

    if len(comps) == 0:
        print(f"Invalid message received: {message}")
        return

    type = comps[0]

    feedcode = comps[1]
    side = comps[2]
    traded_price = float(comps[3])
    traded_volume = int(comps[4])

    print(f"[TRADE] product: {feedcode} side: {side} price: {traded_price} volume: {traded_volume}")

    if type == "TYPE=TRADE":

        feedcode = comps[1].split("=")[1]
        side = comps[2].split("=")[1]
        traded_price = float(comps[3].split("=")[1])
        traded_volume = int(comps[4].split("=")[1])

        print(f"[TRADE] product: {feedcode} side: {side} price: {traded_price} volume: {traded_volume}")


# -------------------------------------
# Main
# -------------------------------------

if __name__ == "__main__":
    start_autotrader()
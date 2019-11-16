import csv
#import matplotlib

wallet= 20000.0
esxPreviousOne= False
esxPreviousTwo= False
esxPreviousPrice= 0
esxBoughtPrice= 0
esxOpenPosition= False
esxStepAmount= 3.0

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
#!/usr/bin/env python
from Bittrex_price_caller import bittrex

try:
    from Tkinter import *
except ImportError:
    from tkinter import *


class BittrexGUI:
    def __init__(self, master):
        self.master = master
        master.title("Bittrex Price Checker")

        self.label = Label(master, text="Enter the ticker for any coin and click Show Price")
        self.label.pack()

        self.pricelabel = Label(self.master)
        self.pricelabel.pack()

        self.e = Entry(self.master)
        self.e.pack()

        self.show_button = Button(
            master, text="Show Price", command=self.update_price)
        self.show_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def update_price(self):
        api = bittrex()
        trade = 'BTC'
        if self.e.get() == "":
            coincurrency = 'OMG'
        else:
            coincurrency = self.e.get()
        market = '{0}-{1}'.format(trade, coincurrency)
        omgsummary = api.getmarketsummary(market)
        omgprice = omgsummary[0]['Last']
        # print 'The price for {0} is {1:.8f} {2}.'.format(currency, omgprice, trade)

        trade = 'USDT'
        currency = 'BTC'
        market = '{0}-{1}'.format(trade, currency)
        btcsummary = api.getmarketsummary(market)
        btcprice = btcsummary[0]['Last']
        # print 'The price for {0} is {1:.8f} {2}.'.format(coincurrency, btcprice, trade)
        dollaPrice = omgprice * btcprice
        # print 'The $ price for OMG is {0:2.3f}'.format(dollaPrice)
        self.pricelabel.config(
            text="The $ price for {0} is {1:2.3f}".format(coincurrency, dollaPrice))
        # self.pricelabel.pack()
        self.master.after(300000, self.update_price)  # 300000, update_price)


root = Tk()
my_gui = BittrexGUI(root)
my_gui.update_price()
root.mainloop()

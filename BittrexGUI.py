#!/usr/bin/env python
from Bittrex_price_caller import bittrex
from Tkinter import Tk, Label, Button


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(
            master, text="Greet", command=self.showPrice)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

    def showPrice(self):
        api = bittrex()
        trade = 'BTC'
        currency = 'OMG'
        market = '{0}-{1}'.format(trade, currency)
        omgsummary = api.getmarketsummary(market)
        omgprice = omgsummary[0]['Last']
        # print 'The price for {0} is {1:.8f} {2}.'.format(currency, omgprice, trade)

        trade = 'USDT'
        currency = 'BTC'
        market = '{0}-{1}'.format(trade, currency)
        btcsummary = api.getmarketsummary(market)
        btcprice = btcsummary[0]['Last']
        # print 'The price for {0} is {1:.8f} {2}.'.format(currency, btcprice, trade)
        dollaPrice = omgprice * btcprice
        # print 'The $ price for OMG is {0:2.3f}'.format(dollaPrice)
        self.label = Label(
            self.master, text="The $ price for OMG is {0:2.3f}".format(dollaPrice))
        self.label.pack()


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

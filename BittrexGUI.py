#!/usr/bin/env python
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import matplotlib.animation as animation
import matplotlib
# from matplotlib import style as style
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

from Bittrex_price_caller import bittrex

# style.use("ggplot")


class BittrexGUI:
    def __init__(self, master):
        self.master = master
        master.title("Bittrex Price Checker")

        self.label = Label(
            master, text="Enter the ticker for any coin and click Show Price")
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
            coincurrency = 'ETH'
        else:
            coincurrency = self.e.get()
        market = '{0}-{1}'.format(trade, coincurrency)
        coinsummary = api.getmarketsummary(market)
        coinprice = coinsummary[0]['Last']
        # print 'The price for {0} is {1:.8f} {2}.'.format(currency, omgprice, trade)

        trade = 'USDT'
        currency = 'BTC'
        market = '{0}-{1}'.format(trade, currency)
        btcsummary = api.getmarketsummary(market)
        btcprice = btcsummary[0]['Last']
        # print 'The price for {0} is {1:.8f} {2}.'.format(coincurrency, btcprice, trade)
        dollaPrice = coinprice * btcprice
        # print 'The $ price for OMG is {0:2.3f}'.format(dollaPrice)
        self.pricelabel.config(
            text="The $ price for {0} is {1:2.3f}".format(coincurrency, dollaPrice))
        # self.pricelabel.pack()

        self.f = Figure(figsize=(5, 5), dpi=100)
        self.a = self.f.add_subplot(111)
        # a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

        self.canvas = FigureCanvasTkAgg(self.f, self.master)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(expand=True)
        self.canvas._tkcanvas.pack()

        self.ani = animation.FuncAnimation(
            my_gui.f, my_gui.animate, interval=100)
        # self.master.after(300000, self.update_price)  # 300000, update_price)

    def animate(self, i):
        api = bittrex()
        trade = 'BTC'
        if self.e.get() == "":
            coincurrency = 'ETH'
        else:
            coincurrency = self.e.get()
        market = '{0}-{1}'.format(trade, coincurrency)
        coinsummary = api.getmarketsummary(market)
        coinprice = coinsummary[0]['Last']

        self.a.clear()

        self.a.plot(coinprice)


root = Tk()
my_gui = BittrexGUI(root)
my_gui.update_price()
root.mainloop()

#!/usr/bin/env python
import sys
from Bittrex_price_caller import bittrex

api = bittrex()
trade = 'BTC'
if len(sys.argv) == 1:
    coincurrency = 'ETH'
else:
    coincurrency = sys.argv[1]
market = '{0}-{1}'.format(trade, coincurrency)
coinsummary = api.getmarketsummary(market)
coinprice = coinsummary[0]['Last']
print('The price for {0} is {1:.8f} {2}.'.format(
    coincurrency, coinprice, trade))

trade = 'USDT'
currency = 'BTC'
market = '{0}-{1}'.format(trade, currency)
btcsummary = api.getmarketsummary(market)
btcprice = btcsummary[0]['Last']
# print(btcsummary)
# print(btcsummary[0]['Last'])
# print ("The price for {0} is {1:.2f} {2}.".format(currency, btcprice, trade))
dollaPrice = coinprice * btcprice
print ('The $ price for {0} is {1:2.3f}'.format(coincurrency, dollaPrice))

trade = 'BTC'
market = '{0}-{1}'.format(trade, coincurrency)
btcsummary = api.getmarkethistory(market)
x = 0
for x in(range(5)):
    coinprice = btcsummary[x]['Price']
    dollaPrice = coinprice * btcprice
    print('{0:.4f}'.format(dollaPrice))

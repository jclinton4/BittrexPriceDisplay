#!/usr/bin/env python
import sys
from Bittrex_price_caller import bittrex

api = bittrex()
trade = 'BTC'
currency = sys.argv[1]
market = '{0}-{1}'.format(trade, currency)
omgsummary = api.getmarketsummary(market)
omgprice = omgsummary[0]['Last']
print ('The price for {0} is {1:.8f} {2}.'.format(currency, omgprice, trade))

trade = 'USDT'
currency = 'BTC'
market = '{0}-{1}'.format(trade, currency)
btcsummary = api.getmarketsummary(market)
btcprice = btcsummary[0]['Last']
print ("The price for {0} is {1:.8f} {2}.".format(currency, btcprice, trade))
dollaPrice = omgprice * btcprice
print ('The $ price for OMG is {0:2.3f}'.format(dollaPrice))

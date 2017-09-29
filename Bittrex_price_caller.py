#!/usr/bin/env python
import json
try:
    import urllib
    from urllib2 import urlopen
except ImportError:
    from urllib.parse import urlencode
    import urllib.request as xyz

class bittrex(object):

    def __init__(self):
        self.public = ['getmarkets', 'getcurrencies', 'getticker',
                       'getmarketsummaries', 'getmarketsummary', 'getorderbook', 'getmarkethistory']

    def query(self, method, values={}):
        if method in self.public:
            url = 'https://bittrex.com/api/v1.1/public/'
        else:
            print ('Something went wrong, sorry.')

        url += method + '?' + urlencode(values)
        headers = {}

        req = xyz.Request(url, headers=headers)
        response = json.loads(xyz.urlopen(req).read())
        # print response

    # if response["result"]:
        return response["result"]
    # else:
    # return response["message"]

    def getmarkets(self):
        return self.query('getmarkets')

    def getcurrencies(self):
        return self.query('getcurrencies')

    def getticker(self, market):
        return self.query('getticker', {'market': market})

    def getmarketsummaries(self):
        return self.query('getmarketsummaries')

    def getmarketsummary(self, market):
        return self.query('getmarketsummary', {'market': market})

    def getorderbook(self, market, type, depth=20):
        return self.query('getorderbook', {'market': market, 'type': type, 'depth': depth})

    def getmarkethistory(self, market, count=20):
        return self.query('getmarkethistory', {'market': market, 'count': count})

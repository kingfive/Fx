import sys
sys.path.append('../')

import os
from datetime import datetime
from currency import Currency
import calendar

class SplitFile():
    def __init__(self):
        self.AUDJPY = Currency('AUDJPY.txt')
        self.AUDUSD = Currency('AUDUSD.txt')
        self.CHFJPY = Currency('CHFJPY.txt')
        self.EURCAD = Currency('EURCAD.txt')
        self.EURCHF = Currency('EURCHF.txt')
        self.EURGBP = Currency('EURGBP.txt')
        self.EURJPY = Currency('EURJPY.txt')
        self.EURUSD = Currency('EURUSD.txt')
        self.GBPCHF = Currency('GBPCHF.txt')
        self.GBPJPY = Currency('GBPJPY.txt')
        self.GBPUSD = Currency('GBPUSD.txt')
        self.NZDJPY = Currency('NZDJPY.txt')
        self.NZDUSD = Currency('NZDUSD.txt')
        self.USDCAD = Currency('USDCAD.txt')
        self.USDCHF = Currency('USDCHF.txt')
        self.USDJPY = Currency('USDJPY.txt')
        self.XAGUSD = Currency('XAGUSD.txt')
        self.XAUUSD = Currency('XAUUSD.txt')
        try:
            os.mkdir('AUDJPY')
        except OSError:
            pass
        try:
            os.mkdir('AUDUSD')
        except OSError:
            pass
        try:
            os.mkdir('CHFJPY')
        except OSError:
            pass
        try:
            os.mkdir('EURCAD')
        except OSError:
            pass
        try:
            os.mkdir('EURCHF')
        except OSError:
            pass
        try:
            os.mkdir('EURGBP')
        except OSError:
            pass
        try:
            os.mkdir('EURJPY')
        except OSError:
            pass
        try:
            os.mkdir('EURUSD')
        except OSError:
            pass
        try:
            os.mkdir('GBPCHF')
        except OSError:
            pass
        try:
            os.mkdir('GBPJPY')
        except OSError:
            pass
        try:
            os.mkdir('GBPUSD')
        except OSError:
            pass
        try:
            os.mkdir('NZDJPY')
        except OSError:
            pass
        try:
            os.mkdir('NZDUSD')
        except OSError:
            pass
        try:
            os.mkdir('USDCAD')
        except OSError:
            pass
        try:
            os.mkdir('USDCHF')
        except OSError:
            pass
        try:
            os.mkdir('USDJPY')
        except OSError:
            pass
        try:
            os.mkdir('XAGUSD')
        except OSError:
            pass
        try:
            os.mkdir('XAUUSD')
        except OSError:
            pass
        self.check_time('AUDJPY',self.AUDJPY)
        self.check_time('AUDUSD',self.AUDUSD)
        self.check_time('CHFJPY',self.CHFJPY)
        self.check_time('EURCAD',self.EURCAD)
        self.check_time('EURCHF',self.EURCHF)
        self.check_time('EURGBP',self.EURGBP)
        self.check_time('EURJPY',self.EURJPY)
        self.check_time('EURUSD',self.EURUSD)
        self.check_time('GBPCHF',self.GBPCHF)
        self.check_time('GBPJPY',self.GBPJPY)
        self.check_time('GBPUSD',self.GBPUSD)
        self.check_time('NZDJPY',self.NZDJPY)
        self.check_time('NZDUSD',self.NZDUSD)
        self.check_time('USDCAD',self.USDCAD)
        self.check_time('USDCHF',self.USDCHF)
        self.check_time('USDJPY',self.USDJPY)
        self.check_time('XAGUSD',self.XAGUSD)
        self.check_time('XAUUSD',self.XAUUSD)

    def check_time(self,currency_string,currency):
        data = currency.get_data()
        month = data.date_time.month
        while True:
            month = data.date_time.month
            self.File = open(  currency_string + '/' +
                               str( data.date_time.year ) + '-' +
                               str(data.date_time.month)
                               ,'wt')
            while data.date_time.month == month:
                month = data.date_time.month
                print(
                              data.currency ,
                              ',' ,
                              data.date_time.year ,
                              '%.2d'% (data.date_time.month) ,
                              '%.2d'% (data.date_time.day) ,
                              ',' ,
                              '%.2d'% (data.date_time.hour),
                              '%.2d'% (data.date_time.minute),
                              '%.2d'% (data.date_time.second),
                              ',' ,
                              '%.4f'% (data.open) ,
                              ',' ,
                              '%.4f'% (data.high) ,
                              ',' ,
                              '%.4f'% (data.low) ,
                              ',' ,
                              '%.4f'% (data.close) ,
                              file = self.File , sep = ''
                     )
                data = currency.get_data()
                if data == False:
                    return

s = SplitFile()

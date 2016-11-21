import sys
sys.path.append('../')

import os
from datetime import datetime
from currency import Currency
import calendar

class SplitFile():
    def __init__(self):
        try:
            self.AUDJPY = Currency('AUDJPY.txt')
        except FileNotFoundError:
            self.AUDJPY = None
        try:
            self.AUDUSD = Currency('AUDUSD.txt')
        except FileNotFoundError:
            self.AUDUSD = None
        try:
            self.CHFJPY = Currency('CHFJPY.txt')
        except FileNotFoundError:
            self.CHFJPY = None
        try:
            self.EURCAD = Currency('EURCAD.txt')
        except FileNotFoundError:
            self.EURCAD = None
        try:
            self.EURCHF = Currency('EURCHF.txt')
        except FileNotFoundError:
            self.EURCHF = None
        try:
            self.EURGBP = Currency('EURGBP.txt')
        except FileNotFoundError:
            self.EURGBP = None
        try:
            self.EURJPY = Currency('EURJPY.txt')
        except FileNotFoundError:
            self.EURJPY = None
        try:
            self.EURUSD = Currency('EURUSD.txt')
        except FileNotFoundError:
            self.EURUSD = None
        try:
            self.GBPCHF = Currency('GBPCHF.txt')
        except FileNotFoundError:
            self.GBPCHF = None
        try:
            self.GBPJPY = Currency('GBPJPY.txt')
        except FileNotFoundError:
            self.GBPJPY = None
        try:
            self.GBPUSD = Currency('GBPUSD.txt')
        except FileNotFoundError:
            self.GBPUSD = None
        try:
            self.NZDJPY = Currency('NZDJPY.txt')
        except FileNotFoundError:
            self.NZDJPY = None
        try:
            self.NZDUSD = Currency('NZDUSD.txt')
        except FileNotFoundError:
            self.NZDUSD = None
        try:
            self.USDCAD = Currency('USDCAD.txt')
        except FileNotFoundError:
            self.USDCAD = None
        try:
            self.USDCHF = Currency('USDCHF.txt')
        except FileNotFoundError:
            self.USDCHF = None
        try:
            self.USDJPY = Currency('USDJPY.txt')
        except FileNotFoundError:
            self.USDJPY = None
        try:
            self.XAGUSD = Currency('XAGUSD.txt')
        except FileNotFoundError:
            self.XAGUSD = None
        try:
            self.XAUUSD = Currency('XAUUSD.txt')
        except FileNotFoundError:
            self.XAUUSD = None


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
        if self.AUDJPY:
            self.check_time('AUDJPY',self.AUDJPY)
        if self.AUDUSD:
            self.check_time('AUDUSD',self.AUDUSD)
        if self.CHFJPY:
            self.check_time('CHFJPY',self.CHFJPY)
        if self.EURCAD:
            self.check_time('EURCAD',self.EURCAD)
        if self.EURCHF:
            self.check_time('EURCHF',self.EURCHF)
        if self.EURGBP:
            self.check_time('EURGBP',self.EURGBP)
        if self.EURJPY:
            self.check_time('EURJPY',self.EURJPY)
        if self.EURUSD:
            self.check_time('EURUSD',self.EURUSD)
        if self.GBPCHF:
            self.check_time('GBPCHF',self.GBPCHF)
        if self.GBPJPY:
            self.check_time('GBPJPY',self.GBPJPY)
        if self.GBPUSD:
            self.check_time('GBPUSD',self.GBPUSD)
        if self.NZDJPY:
            self.check_time('NZDJPY',self.NZDJPY)
        if self.NZDUSD:
            self.check_time('NZDUSD',self.NZDUSD)
        if self.USDCAD:
            self.check_time('USDCAD',self.USDCAD)
        if self.USDCHF:
            self.check_time('USDCHF',self.USDCHF)
        if self.USDJPY:
            self.check_time('USDJPY',self.USDJPY)
        if self.XAGUSD:
            self.check_time('XAGUSD',self.XAGUSD)
        if self.XAUUSD:
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

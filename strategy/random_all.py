import sys
sys.path.append('../')
import random
from account import Account
from currency import Currency
from form import Data , Earn , Order
import time

class strategy_random():
    def __init__(self):
        self.money = 100000
        self.account = Account( self.money )
        self.account.set_stop_multiple(0.01,0)
        self.multiple = 1
        self.first_year = 2005
        self.last_year = 2005
        self.now_year = self.first_year
        self.now_month = 1
        self.minute = 240
        self.currency = None # save Currency object
        self.currency_string = 'AUDUSD'
        self.mode = self.change_month
        self.main()
        self.print_earn()
        print('reversal_time :', self.account.reversal_time)


    def main(self):
        '''
        進場random  出場停損停利
        '''
        while self.mode( self.currency_string ):
            data = self.random_get_data( self.minute )
            while data:
                ran = self.one_or_minus()
                self.account.trade_multiple( self.currency_string , ran * self.multiple )
                data = self.random_get_data( self.minute )

    def one_or_minus(self):
        l = [-1,1]
        ans = random.choice(l)
        return ans

    def random_get_data(self,time):
        ran = random.randint(int(time*0.5) , time)
        for i in range(ran):
            data = self.currency.get_data()
            self.account.update( data )
        return data

    def print_earn(self):
        positive = 0
        negative = 0
        bull = 0
        bear = 0
        for i in self.account.AUDUSD_order_history:
            if i.volume > 0:
                positive += 1
            else:
                negative += 1

        for i in self.account.earn[0:10]:
            if i.bull_or_bear == 'bull':
                bull += 1
            else:
                bear += 1
            print(i)
        print('positive = ',positive)
        print('negative = ',negative)
        print('bull = ',bull)
        print('bear = ',bear)
        i = self.account.earn[-1]
        print(str(i.buy.data.date_time) ,' money = ', i.money)


    def change_year(self,currency_string):
        if self.now_year != self.last_year+1:
            str_now = str(self.now_year)
            if self.now_year != 2016:
                self.currency = Currency(currency_string , str_now + '-1' , str_now + '-12')
            else:
                self.currency = Currency(currency_string , str_now + '-1' , str_now + '-7')

            self.now_year += 1
            return True
        else:
            return False

    def change_month(self,currency_string):
        if (self.now_year == 2016 and self.now_month == 8):
            return False
        if (self.now_year < self.last_year or
            self.now_year == self.last_year and self.now_month < 13):
            str_now_year = str(self.now_year)
            str_now_month = str(self.now_month)
            time = str_now_year + '-' + str_now_month
            self.currency = Currency( currency_string , time , time)
            self.now_month += 1
            if self.now_month > 12 : # 進位
                self.now_year += 1 # carry
                self.now_month = 1 # initial
            return True
        else:
            return False

s = strategy_random()

import sys
sys.path.append('../')
import random
from account import Account
from currency import Currency
from form import Data , Earn , Order

class strategy_random():
    def __init__(self,money,minute):
        self.money = money
        self.account = Account(money)
        self.account.set_stop_multiple(0.02,0.07)
        self.first_year = 2001
        self.last_year = 2016
        self.now_year = self.first_year
        self.now_month = 1
        self.minute = minute
        self.main()
        print('reversal_time :', self.account.reversal_time)

    def main(self):
        '''
        進場random  出場停損停利
        '''
        while self.change_year():
            self.account = Account(self.money)
            self.account.set_stop_multiple(0.015,0.07)
            while (True):
                ran = self.one_or_minus()
                data = self.random_get_data('EURUSD',int(self.minute*0.5),self.minute)
                if data == False:
                    break
                self.account.trade_multiple('EURUSD',ran * 3)
            self.print_earn()
            
    def one_or_minus(self):
        l = [-1,1]
        ans = random.choice(l)
        return ans

    def random_get_data(self,currency,first,last):
        if currency == 'EURUSD':
            get = self.EURUSD.get_data
        ran = random.randint(first,last)
        for i in range(ran):
            data = get()
            if data == False:
                return False
            self.account.update(data)
        return data

    def print_earn(self):
        i = self.account.earn[-1]
        print(str(i.buy.data.date_time) ,' money = ', i.money)

    def change_year(self):
        if self.now_year != self.last_year+1:
            str_now = str(self.now_year)
            if self.now_year != 2016:
                self.EURUSD = Currency('EURUSD' , str_now + '-1' , str_now + '-12')
            else:
                self.EURUSD = Currency('EURUSD' , str_now + '-1' , str_now + '-7')

            self.now_year += 1
            return True
        else:
            return False

    def change_month(self):
        if self.now_year == 2016 and self.now_month == 8:
            return False
        if (self.now_year < self.last_year or
            self.now_year == self.last_year and self.now_month < 12):
            str_now_year = str(self.now_year)
            str_now_month = str(self.now_month)
            time = str_now_year + '-' + str_now_month
            self.EURUSD = Currency('EURUSD' , time , time)
            self.now_month += 1
            if self.now_month > 12 : # 進位
                self.now_year += 1 # carry
                self.now_month = 1 # initial
        return True

s = strategy_random(100000,240)

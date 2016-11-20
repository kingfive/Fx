import sys
sys.path.append('../')
import random
from account import Account
from currency import Currency
from form import Data , Earn , Order


class random_origin():
    def __init__(self):
        self.money = 100000
        self.account = Account( self.money )
        self.currency_string = 'EURUSD'
        self.currency = Currency( self.currency_string , '2001-1' , '2001-2' )
        self.minute = 240
        self.multiple = 3
        self.main()
        self.print_hold_record()
        self.print_order()
        self.print_earn()

    def main(self):

        data = self.random_get_data( self.currency_string , self.minute )
        while data:
            ran = self.one_or_minus()
            self.account.trade_multiple( self.currency_string , ran * self.multiple )
            #self.account.trade_money( self.currency_string , ran * self.money )
            data = self.random_get_data( self.currency_string , self.minute )

    def one_or_minus(self):
        l = [-1,1]
        ans = random.choice(l)
        return ans

    def random_get_data(self,currency_string,time):
        ran = random.randint(int(time*0.5) , time)
        for i in range(ran):
            data = self.currency.get_data()
            if data == False:
                return False
            self.account.update( data )
        return data

    def print_earn(self):
        bull = 0
        bear = 0
        for i in self.account.earn:
            if i.bull_or_bear == 'bull':
                bull += 1
            else:
                bear += 1
        print(self.account.earn[-1])
        print('bull = ',bull)
        print('bear = ',bear)

    def print_order(self):
        positive = 0
        negative = 0
        for i in self.account.EURUSD_order_history:
            if i.volume > 0:
                positive += 1
            else:
                negative += 1
            #print(i)
        print('positive = ',positive)
        print('negative = ',negative)

    def print_hold_record(self):
        hold_positive = 0
        hold_negative = 0
        for i in self.account.EURUSD_hold_record:
            if i.volume > 0:
                hold_positive += 1
            else:
                hold_negative += 1
            print(i)
        print('hold_positive = ',hold_positive)
        print('hold_negative = ',hold_negative)
s = random_origin()

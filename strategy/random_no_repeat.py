import sys
sys.path.append('../')
import random
from account import Account
from currency import Currency
from form import Data , Earn , Order
from RandomTrade import get , one_or_minus , random_update , print_earn

class random_no_repeat():
    def __init__(self):
        self.money = 100000
        self.account = Account( self.money )
        self.account.set_stop(1000,3000)
        self.currency_string = 'EURUSD'
        self.currency = Currency( self.currency_string , '2015-1' , '2015-12' )
        self.multiple = 3
        self.main()
        print_earn( self.account )

    def main(self):
        data = get( self.currency )
        while data:
            self.account.update( data )
            if len(self.account.EURUSD_hold) == 0:
                ran = one_or_minus()
                self.account.trade_money( self.currency_string , ran * self.money * self.multiple  )
            data = get( self.currency )


for i in range(30):
    s = random_no_repeat()

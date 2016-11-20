import sys
sys.path.append('../')
sys.path.append('../graph')

import random
from account import Account
from currency import Currency
from form import Data , Earn , Order
from RandomTrade import get , one_or_minus , random_update , print_earn
from graph_earn import graph_earn
from GraphAll import GraphAll

class random_no_repeat():
    def __init__(self):
        self.money = 100000
        self.account = Account( self.money )
        self.account.set_stop(0,10000)
        self.currency_string = 'EURUSD'
        self.currency = Currency( self.currency_string , '2015-1' , '2015-2' )
        self.multiple = 10
        self.main()
        print_earn( self.account )

    def main(self):
        data = get( self.currency )
        while data:
            ran = one_or_minus()
            data = random_update(self.account,self.currency,120)
            self.account.trade_money( self.currency_string , ran * self.money * self.multiple  )

        GraphAll( self.account )
s = random_no_repeat()

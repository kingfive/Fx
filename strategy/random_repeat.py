import sys
sys.path.append('../')
sys.path.append('../graph')
import random
from account import Account
from currency import Currency
from form import Data , Earn , Order
from RandomTrade import get , one_or_minus , random_update , print_earn
from graph_earn import graph_earn
from graph_hold_record import graph_hold_record
from GraphAll import GraphAll

class random_repeat():
    def __init__(self):
        self.money = 100000
        self.account = Account( self.money )
        self.account.set_stop(2000,10000)
        self.currency_string = 'EURUSD'
        self.currency = Currency( self.currency_string , '2015-1' , '2016-3' )
        self.multiple = 3
        self.minute = 600
        self.main()
        print_earn( self.account )

    def main(self):
        data = get( self.currency )
        while data:
            random_update( self.account , self.currency , self.minute )
            ran = one_or_minus()
            self.account.trade_money( self.currency_string , ran * self.money * self.multiple  )
            data = get( self.currency )
        GraphAll( self.account )

for i in range(1):
    s = random_repeat()

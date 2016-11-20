import sys
sys.path.append('../')
sys.path.append('../graph')

from account import Account
from currency import Currency
from form import Data , Earn , Order
from RandomTrade import get , one_or_minus , random_update , print_earn
from graph_data import graph_data
from graph_earn import graph_earn
from graph_hold_record import graph_hold_record
from GraphAll import GraphAll

class checker():
    def __init__(self):
        self.money = 100000
        self.account = Account( self.money )
        self.currency_string = 'EURUSD'
        self.currency = Currency( self.currency_string , '2001-1' , '2016-3')
        self.main()

    def main(self):
        self.update()
        self.account.trade_money("EURUSD", -100000)
        for i in range(1000):
            self.update()
        self.account.trade_money("EURUSD", 200000)
        GraphAll( self.account )

    def update(self):
        data = self.currency.get_data()
        self.account.update( data )
        graph_data().add_data( data )
        return data

c = checker()

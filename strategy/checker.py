import sys
sys.path.append('../')
from account import Account
from currency import Currency
from form import Data , Earn , Order
from RandomTrade import get , one_or_minus , random_update , print_earn

class checker():
    def __init__(self):
        self.money = 100000
        self.account = Account( self.money )
        self.currency_string = 'EURUSD'
        self.currency = Currency( self.currency_string , '2001-1' , '2016-3')
        self.main()

    def main(self):
        self.account.update( self.currency.get_data() )
        self.account.trade_money("EURUSD", -100000)
        for i in range(1000):
            self.account.update(self.currency.get_data())
        self.account.trade_money("EURUSD", 100000)

        print(self.account.earn[0])

c = checker()

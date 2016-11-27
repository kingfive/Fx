from currency import Currency
import matplotlib.pyplot as plt
from graph_earn import graph_earn
from graph_hold_record import graph_hold_record

class GraphAll():
    def __init__(self,account):
        self.account = account
        self.graph_earn = graph_earn( self.account.earn )
        #self.graph_hold_record = graph_hold_record( self.account.EURUSD_hold_record )
        self.main()

    def main(self):
        plt.show()

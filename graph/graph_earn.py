from currency import Currency
import matplotlib.pyplot as plt

class graph_earn():

    def __init__(self,earn):
        self.earn = earn
        self.date_list = []
        self.money_list = []
        self.main()

    def main(self):
        for i in self.earn:
            if i.bull_or_bear == 'bull':
                self.date_list.append( i.sell.data.date_time )
                self.money_list.append( i.money )
            else:
                self.date_list.append( i.buy.data.date_time )
                self.money_list.append( i.money )

        plt.subplot(111)
        plt.plot(self.date_list , self.money_list)

import sys
sys.path.append('../')

from currency import Currency
import matplotlib.pyplot as plt

class test():

    def __init__(self):
        self.currency_string = 'EURUSD'
        self.currency = Currency(self.currency_string,'2016-1','2016-2')
        self.data_list = []
        self.date_list = []
        self.price_list = []
        self.main()

    def main(self):
        data = self.currency.get_data()
        print(data)
        while data:
            self.data_list.append(data)
            data = self.currency.get_data()

        for i in self.data_list:
            self.date_list.append(i.date_time)
            self.price_list.append(i.open)


        print(self.data_list)
        plt.plot(self.date_list , self.price_list)
        plt.show()

t = test()

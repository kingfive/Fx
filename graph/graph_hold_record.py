from currency import Currency
import matplotlib.pyplot as plt

class graph_hold_record():

    def __init__(self,hold_record):
        self.hold_record = hold_record
        self.date_list = []
        self.money_list = []
        self.main()

    def main(self):
        for i in self.hold_record:
            self.date_list.append( i.data.date_time )
            self.money_list.append( i.volume )
        else:
            self.date_list.append( i.data.date_time )
            self.money_list.append( i.volume )

        plt.subplot(212)
        plt.plot(self.date_list , self.money_list)

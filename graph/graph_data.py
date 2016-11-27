from currency import Currency
import matplotlib.pyplot as plt

class graph_data():
    def __init__(self):
        self.data_list = []

    def add_data(self,data):
        self.data_list.append( data )
        plt.subplot(212)
        for i in self.data_list:
            plt.plot( i.date_time , i.open )
        plt.show()

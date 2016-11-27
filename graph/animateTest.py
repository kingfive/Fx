import sys
sys.path.append('../')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from currency import Currency


class animateTest():
    def __init__(self):
        self.currency_string = 'EURUSD'
        self.currency = Currency( self.currency_string , '2001-1' , '2016-7' )
        self.fig = plt.figure('My Fx Project')
        self.ax1 = self.fig.add_subplot(1,1,1)
        self.date_list = []
        self.price_list = []
        self.init_data()
        self.main()

    def init_data(self):
        while len(self.date_list) < 500 :
            data = self.currency.get_data()
            self.date_list.append( data.date_time )
            self.price_list.append( data.open )

    def update(self,i):
        data = self.currency.get_data()
        if len(self.date_list) > 500 :
            self.date_list.pop(0)
            self.price_list.pop(0)

        for i in range(1):
            self.date_list.append( data.date_time )
            self.price_list.append( data.open )
        self.ax1.clear()
        self.ax1.set_title( self.currency_string )
        self.ax1.plot( self.date_list , self.price_list ,lw=2)
        self.ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H'))
        self.ax1.set_ylabel('Price',fontsize=20,family='monospace',color='green')
        for label in self.ax1.xaxis.get_ticklabels():
            label.set_rotation(15)
        plt.grid( True )

    def main(self):
        ani = animation.FuncAnimation(self.fig, self.update, interval=1)
        plt.show()

a = animateTest()

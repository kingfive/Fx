class Data():
    def __init__(self,cur,dt,op,hi,lo,cl):
        self.__currency = cur
        self.__date_time = dt
        self.__open = op
        self.__high = hi
        self.__low = lo
        self.__close = cl
        self.__price = self.__open
    def set_price(self,price):
        self.__price = price
    @property
    def currency(self):
        return self.__currency
    @property
    def date_time(self):
        return self.__date_time
    @property
    def price(self):
        return self.__price
    @property
    def open(self):
        return self.__open
    @property
    def high(self):
        return self.__high
    @property
    def low(self):
        return self.__low
    @property
    def close(self):
        return self.__close
    def __str__(self):
        str_date = str(self.__date_time)
        str_price = str(self.__price)
        return str_date + "  Price: " + str_price


class Order():
    def __init__(self , data , volume):
        self.__data = data
        self.__volume = volume
        self.__profit = 0
        self.__trade_type = 'Normal'
    def set_trade_type(self,typee):
        self.__trade_type = typee
    def __str__(self):
        str_data = str(self.__data)
        str_money = str(self.__volume)
        return str_data +  '  ' + self.__trade_type + '  Order: ' + str_money 
    @property
    def data(self):
        return self.__data
    @property
    def profit(self):
        return self.__profit
    @profit.setter
    def profit(self,profit):
        self.__profit = profit
    @property
    def volume(self):
        return self.__volume
    @volume.setter
    def volume(self,new_volume):
        self.__volume = new_volume
    @property
    def trade_type(self):
        return self.__trade_type

class Earn():
    def __init__(self,bull_or_bear,buy,sell,profit):
        self.__bull_or_bear = bull_or_bear
        self.__buy = buy
        self.__sell = sell
        self.__profit = profit
    def set_money_and_win_rate(self,win_rate,money):
        self.__win_rate = win_rate
        self.__money = money
    def __str__(self):
        str_buy_data = str(self.buy.data)
        str_sell_data = str(self.sell.data)
        str_order = str(self.buy.volume)
        str_profit = str(self.profit)
        str_win_rate = str(self.win_rate)
        str_money = str(self.money)
        return ( '"' + self.bull_or_bear + '"' + '\n' +
                'Buy  = ' + str_buy_data + '\n' +
                'Sell = ' + str_sell_data + '\n' +
                'Order = ' + str_order + '\n' +
                'Earn = ' + str_profit + '\n' +
                'Win rate = ' + str_win_rate + '\n'
                'Money = ' + str_money + '\n')
    @property
    def bull_or_bear(self):
        return self.__bull_or_bear
    @property
    def buy(self):
        return self.__buy
    @property
    def sell(self):
        return self.__sell
    @property
    def money(self):
        return self.__money
    @property
    def profit(self):
        return self.__profit
    @property
    def win_rate(self):
        return self.__win_rate

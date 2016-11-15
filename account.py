from Deal import X_USD , X_USD_profit
from form import Data , Order, Earn
from copy import copy

class Account():
    '''

    ----------------------------------------------------------------------------
    How to use it ?
    ----------------------------------------------------------------------------

    ### Start to make a trade
    ### Example

    account = Account( your money )
        # Have an account
    currency = Currency( "EURUSD" , "2001-1" , "2016-3")
        # Open a currency data file
    account.update( currency.get_data())
        # Update currency data in account
    account.trade_money( 'EURUSD' , volume )
        # Have a trade ( volume can be positive or negative )
    account.trade_multiple( 'EURUSD' , multiple )
        # Have a trade ( multiple is a multiple of money )


    ### Get your output

    account.earn  <--  It's a list

    ----------------------------------------------------------------------------
    How it did ?
    ----------------------------------------------------------------------------

    加入新貨幣對 需要改的地方 chooser  calculate_profit  update  get_now

    '''

    def __init__(self , money):
        self.__money = money
        self.__money_not_add_float_profit = money # 沒加入浮動損益的現金
        self.__lock = False # 帳戶原本正常運行 not yet used
        self.__security_deposit = 0 # 保證金 not yet used
        self.__lever = 200 # 可使用的槓桿倍數 not yet used
        self.__win_rate = 0 # 勝率
        self.__reversal_time = 0 # lens of earn
        self.__earn = [] # Earn list
        self.__hold = None # save which hold to use
        self.__hold_record = None # save which hold record to use
        self.__order_history = None # save which order_history to use
        self.__status = None #function variable
        self.__calculate_earn = None #function variable
        self.__volume = None #function variable
        self.__EURUSD_now = None # save data object (it's now price)
        self.__AUDUSD_now = None # save data object (it's now price)
        self.__EURUSD_float_profit = 0 # 浮動損益
        self.__AUDUSD_float_profit = 0 # 浮動損益
        self.__EURUSD_order_history = [] # 下單紀錄
        self.__AUDUSD_order_history = [] # 下單紀錄
        self.__EURUSD_hold = [] # 現在持有的下單
        self.__AUDUSD_hold = [] # 現在持有的下單
        self.__EURUSD_hold_record = [] # 下單紀錄
        self.__AUDUSD_hold_record = [] # 下單紀錄
        self.__stop_loss_multiple = 0
        self.__stop_win_multiple = 0
        self.__stop_loss = 0 # 停損
        self.__stop_win = 0 # 停利
        self.__stop_type = '' # 停損停利的種類
        self.__difference = { # 匯差
            'EURUSD' : 0.00006 ,
            'AUDUSD' : 0.00007
        }

    def set_stop(self,stop_loss,stop_win):
        self.__stop_loss = stop_loss # initialize
        self.__stop_win = stop_win # initialize
        self.__stop_type = 'Money type'

    def set_stop_multiple(self,stop_loss,stop_win):
        self.__stop_loss_multiple = stop_loss # remember the loss multiple
        self.__stop_win_multiple = stop_win # remember the loss multiple
        self.__stop_loss = stop_loss * self.__money # reset stop_loss
        self.__stop_win = stop_win * self.__money # reset stop_win
        self.__stop_type = 'Multiple type'

    def __add_difference_to_data(self,currency,volume):
        '''
        add fee to price , when BUY or SELL ,this function will be called
                           ( when call "trade_money" or "trade_multiple" )
        '''
        diff = self.__difference[ currency ]
        data = copy( self.get_now( currency ) )
        if volume > 0:
            data.set_price( round( data.price + diff ,5) )
        elif volume < 0:
            data.set_price( round( data.price - diff ,5) )
        return data

    def update(self,data):
        if not type(data) is Data :  # 輸入參數若不是 Data object 則不做
            return
        if data.currency =='EURUSD' :
            self.__EURUSD_now = data # updata data
        elif data.currency =='AUDUSD' :
            self.__AUDUSD_now = data # updata data
        self.__chooser( data.currency )
        self.__calculate_profit( data.currency ) # 計算浮動損益(尚未把浮動損益加入現金)
        self.__check_stop( data.currency ) # 確認是否到停損的價格
        self.__add_float_profit_to_money()

        if self.__stop_type == 'Multiple type' :
            self.set_stop_multiple(self.__stop_loss_multiple,self.__stop_win_multiple)
            # reset stop_multiple

    def __add_float_profit_to_money(self):
        self.__money  = self.__money_not_add_float_profit
        self.__money += self.__EURUSD_float_profit
        self.__money += self.__AUDUSD_float_profit

    def trade_money(self , currency , volume):
        if volume == 0:
            return
        self.__chooser( currency ) # 置換不同貨幣對需要的function
        data = self.__add_difference_to_data( currency , volume )
        order = Order(data , volume + self.__volume() )
        self.__hold_record.append( order ) # update hold record
        order = Order(data , volume)
        self.__order_history.append( order ) # update order history
        order = Order(data , volume)
        self.__reversal( order ) # 沖銷之前的下單（如果有的話）
        self.__calculate_profit( currency )
        self.__add_float_profit_to_money()


    def trade_multiple(self , currency , multiple):
        if multiple == 0:
            return
        self.__chooser( currency ) # 置換不同貨幣對需要的function
        data = self.__add_difference_to_data( currency , multiple * self.money )
        order = Order(data , multiple * self.money + self.__volume() )
        self.__hold_record.append( order ) # update hold record
        order = Order(data , multiple * self.money)
        self.__order_history.append( order ) # update order history
        order = Order(data , multiple * self.money)
        self.__reversal( order ) # 沖銷之前的下單（如果有的話）
        self.__calculate_profit( currency )
        self.__add_float_profit_to_money()


    def EURUSD_status(self):
        if (self.EURUSD_volume()) == 0:
            return "No Trade"
        elif (self.EURUSD_volume()) > 0:
            return "bull"
        else:
            return "bear"

    def EURUSD_volume(self):
        volume = 0
        for h in self.EURUSD_hold:
            volume += h.volume
        return volume

    def AUDUSD_status(self):
        if (self.AUDUSD_volume()) == 0:
            return "No Trade"
        elif (self.AUDUSD_volume()) > 0:
            return "bull"
        else:
            return "bear"

    def AUDUSD_volume(self):
        volume = 0
        for h in self.AUDUSD_hold:
            volume += h.volume
        return volume

    def get_now(self, currency):
        if  currency == 'EURUSD' :
            return self.__EURUSD_now
        if  currency == 'AUDUSD' :
            return self.__AUDUSD_now

    def __chooser(self,currency):
        if  currency == 'EURUSD' :
            self.__calculate_earn = X_USD
            self.__volume = self.EURUSD_volume
            self.__status = self.EURUSD_status
            self.__hold =  self.__EURUSD_hold
            self.__hold_record = self.__EURUSD_hold_record
            self.__order_history = self.__EURUSD_order_history
            self.__float_profit = self.__EURUSD_float_profit
        if  currency == 'AUDUSD' :
            self.__calculate_earn = X_USD
            self.__volume = self.AUDUSD_volume
            self.__status = self.AUDUSD_status
            self.__hold =  self.__AUDUSD_hold
            self.__hold_record = self.__AUDUSD_hold_record
            self.__order_history = self.__AUDUSD_order_history
            self.__float_profit = self.__AUDUSD_float_profit

    def __reversal(self , order):
        if ( (self.__status() == "bull")  and  order.volume < 0 ): # 要正向沖消
            self.__bull_reversal( order )
        elif ((self.__status() == "bear")  and  order.volume > 0): # 要反向沖消
            self.__bear_reversal( order )
        else:
            H = self.__hold
            H.append( order )

    def __bull_reversal(self , order):
        H = self.__hold # make the code more readible
        order_copy = copy( order )
        while H and abs(order.volume) > abs(H[0].volume):
            earn = self.__calculate_earn(self.__status() , H[0] , order_copy , H[0].volume )
            self.__add_earn( earn )
            order.volume += H[0].volume
            H.pop(0)
        if  H and abs(order.volume) == abs(H[0].volume):
            earn = self.__calculate_earn(self.__status() , H[0] , order_copy, H[0].volume )
            self.__add_earn( earn )
            order.volume += H[0].volume
            H.pop(0)
        elif H and abs(order.volume) < abs(H[0].volume):
            earn = self.__calculate_earn(self.__status() , H[0] , order_copy , order_copy.volume )
            self.__add_earn( earn )
            H[0].volume += order.volume
            order.volume = 0
        if  not H and order.volume != 0:
            H.append( order ) #append a order to hold

    def __bear_reversal(self , order):
        H = self.__hold # make the code more readible
        order_copy = copy( order ) # if not copy , something wrong will happen
        while (H and  abs(order.volume) > abs(H[0].volume)) :
            earn = self.__calculate_earn( self.__status() , order_copy, H[0] , H[0].volume )
            self.__add_earn( earn )
            order.volume -= abs(H[0].volume)
            H.pop(0)
        if  H and abs(order.volume) == abs(H[0].volume):
            earn = self.__calculate_earn( self.__status() , order_copy, H[0] , H[0].volume )
            self.__add_earn( earn )
            order.volume -= abs(H[0].volume)
            H.pop(0)
        elif H and abs(order.volume) < abs(H[0].volume):
            earn = self.__calculate_earn( self.__status() , order_copy, H[0] , order_copy.volume )
            self.__add_earn( earn )
            H[0].volume += order.volume
            order.volume = 0
        if  not H and order.volume != 0 :
            H.append( order ) #append a order to hold

    def __add_earn(self , earn):
        self.__money += earn.profit
        self.__money_not_add_float_profit += earn.profit
        if earn.profit > 0:
            win_or_not = 1
        else:
            win_or_not = 0
        self.__reversal_time += 1
        self.__win_rate = (self.reversal_time* self.win_rate + win_or_not) / (self.reversal_time + 1)
        earn.set_money_and_win_rate( self.win_rate , self.money )
        self.earn.append( earn )

    def __calculate_profit(self ,currency):
        if currency == 'EURUSD' :
            self.__EURUSD_float_profit = 0
            if self.__hold :
                for i in self.__hold:
                    i.profit = 0
                    i.profit += X_USD_profit(i,self.__EURUSD_now)
                    self.__EURUSD_float_profit += i.profit
        if currency == 'AUDUSD' :
            self.__AUDUSD_float_profit = 0
            if self.__hold :
                for i in self.__hold:
                    i.profit = 0
                    i.profit += X_USD_profit(i,self.__AUDUSD_now)
                    self.__AUDUSD_float_profit += i.profit

    def __check_stop(self,currency):
        if self.__stop_loss == 0 and self.__stop_win == 0:
            return
        if self.__hold:
            for index , i in enumerate(self.__hold):
                if i.profit < (-self.__stop_loss) and self.__stop_loss != 0:
                    self.__trade_hold(index , 'Stop loss' , currency)
                if i.profit > self.__stop_win and self.__stop_win != 0:
                    self.__trade_hold(index , 'Stop win' , currency)
        # check_stop -> trade_hold -> __reversal_hold ->
        # __reversal_hold_bull or __reversal_hold_bear

    def __trade_hold(self,index,typee,currency): # 停損停利用
        '''
        Trade(Reversal) a desighed hold
        '''
        self.__chooser( currency ) # 置換不同貨幣對需要的function或變數
        data = self.__add_difference_to_data( currency , - self.__hold[index].volume)
        order = Order(data , -self.__hold[index].volume + self.__volume())
        self.__hold_record.append( order ) # update hold record
        order = Order(data , -self.__hold[index].volume)
        order.set_trade_type( typee )
        self.__order_history.append( order ) # update order history
        order = Order(data , -self.__hold[index].volume)
        self.__reversal_hold( index , order ) # 沖銷某個hold

    def __reversal_hold(self,index,order):
        if self.__hold[index].volume > 0 :
            self.__reversal_hold_bull(index,order)
        else:
            self.__reversal_hold_bear(index,order)

    def __reversal_hold_bull(self,index,order):
        H = self.__hold
        earn = self.__calculate_earn(self.__status(),H[index],order,order.volume)
        H.pop(index)
        self.__calculate_profit( order.data.currency )
        self.__add_float_profit_to_money()
        self.__add_earn( earn )

    def __reversal_hold_bear(self,index,order):
        H = self.__hold
        earn = self.__calculate_earn(self.__status(),order,H[index],order.volume)
        H.pop(index)
        self.__calculate_profit( order.data.currency ) # pop hold 後 先更新profit
        self.__add_float_profit_to_money() # 再把profit 更新至money
        self.__add_earn( earn ) # 最後把更新後的資料傳進earn

    @property
    def money(self):
        return self.__money

    @property
    def money_not_add_float_profit(self):
        return self.__money_not_add_float_profit

    @property
    def EURUSD_hold(self):
        return self.__EURUSD_hold

    @property
    def AUDUSD_hold(self):
        return self.__AUDUSD_hold

    @property
    def EURUSD_hold_record(self):
        return self.__EURUSD_hold_record

    @property
    def AUDUSD_hold_record(self):
        return self.__AUDUSD_hold_record

    @property
    def EURUSD_order_history(self):
        return self.__EURUSD_order_history

    @property
    def AUDUSD_order_history(self):
        return self.__AUDUSD_order_history

    @property
    def EURUSD_float_profit(self):
        return self.__EURUSD_float_profit

    @property
    def AUDUSD_order_history(self):
        return self.__AUDUSD_order_history

    @property
    def AUDUSD_float_profit(self):
        return self.__AUDUSD_float_profit

    @property
    def win_rate(self):
        return self.__win_rate

    @property
    def earn(self):
        return self.__earn

    @property
    def reversal_time(self):
        return self.__reversal_time

from form import Earn , Data , Order
from copy import copy

def X_USD(bull_or_bear,buy,sell,volume):
    ans = round( round(sell.data.price - buy.data.price,5) * abs(volume) )
    #"round()" is to solve float error
    buy_copy = copy( buy ) # 不改動到原參數物件的值
    sell_copy = copy( sell )
    buy_copy.volume = abs(volume)
    sell_copy.volume = - abs(volume)
    return Earn( bull_or_bear , buy_copy , sell_copy , ans)

def X_USD_profit(hold,now):
    ans = round(  ( now.price - hold.data.price ) * hold.volume , 2 )
    return ans

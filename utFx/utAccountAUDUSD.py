import sys
sys.path.append('../')

from account import Account
from currency import Currency
from form import *
import unittest
import test
from datetime import datetime

money = 100000
AUDUSD_diff = 0.00006

class utAccountAUDUSD(unittest.TestCase):
    '''
    argument set :
        money : 100000
        AUDUSD difference : 0.00006
    '''
    '''
    def test_one(self):
        self.assertEqual(1,1)

    def test_hold_positive(self):
        Equal = self.assertEqual
        price = round(0.5617 + AUDUSD_diff , 5)
        profit = round(0.5617 - price , 5) * money
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',money) # 0.5617 + AUDUSD_diff
        Equal(account.AUDUSD_hold[0].volume,money)
        Equal(account.AUDUSD_hold[0].data.price,price)
        Equal(account.AUDUSD_hold[0].profit,profit)

    def test_hold_negative(self):
        Equal = self.assertEqual
        price = round(0.5617 - AUDUSD_diff , 5)
        profit = round(price - 0.5617  , 5) * money
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',-money) # 0.5617 - AUDUSD_diff
        Equal(account.AUDUSD_hold[0].volume,-money)
        Equal(account.AUDUSD_hold[0].data.price,price)
        Equal(account.AUDUSD_hold[0].profit,profit)

    def test_hold_positive_to_negative(self):
        Equal = self.assertEqual
        price = round(0.5616 - AUDUSD_diff , 5)
        profit = round(price - 0.5616  , 5) * money
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',money) # 0.5617 + AUDUSD_diff
        Equal(account.AUDUSD_hold[0].volume,money)
        account.update(AUDUSD.get_data()) # 0.5616
        account.trade_money('AUDUSD',- 2 * money) # 0.5616 - AUDUSD_diff
        Equal(account.AUDUSD_hold[0].volume,-money)
        Equal(account.AUDUSD_hold[0].data.price,price)
        Equal(account.AUDUSD_hold[0].profit,profit)


    def test_hold_negative_to_positive(self):
        Equal = self.assertEqual
        price = round(0.5616 + AUDUSD_diff , 5)
        profit = round(0.5616 - price , 5) * money
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',-money) # 0.5617 - AUDUSD_diff
        Equal(account.AUDUSD_hold[0].volume,-money)
        account.update(AUDUSD.get_data()) # 0.5616
        account.trade_money('AUDUSD',2 * money) # 0.5616 + AUDUSD_diff
        Equal(account.AUDUSD_hold[0].volume,money)
        Equal(account.AUDUSD_hold[0].data.price,price)
        Equal(account.AUDUSD_hold[0].profit,profit)

    def test_hold_multiple_positive(self):
        Equal = self.assertEqual
        price0 = round(0.5617 + AUDUSD_diff , 5)
        price1 = round(0.5616 + AUDUSD_diff , 5)
        profit0 = round(0.5616 - price0 , 5) * money
        profit1 = round( 0.5616 - price1 , 5) * money * 2
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',money) # 0.5617 + AUDUSD_diff
        account.update(AUDUSD.get_data()) # 0.5616
        Equal(account.AUDUSD_hold[0].profit,profit0)
        account.trade_money('AUDUSD', 2 * money) # 0.5616 - AUDUSD_diff
        Equal(account.AUDUSD_hold[0].volume,1 * money)
        Equal(account.AUDUSD_hold[1].volume,2 * money)
        Equal(account.AUDUSD_hold[0].data.price,price0)
        Equal(account.AUDUSD_hold[1].data.price,price1)
        Equal(account.AUDUSD_hold[0].profit,profit0)
        Equal(account.AUDUSD_hold[1].profit,profit1)

    def test_hold_multiple_negative(self):
        Equal = self.assertEqual
        price0 = round(0.5617 - AUDUSD_diff , 5)
        price1 = round(0.5616 - AUDUSD_diff , 5)
        profit0 = round(price0 - 0.5616 , 5) * money
        profit1 = round(price1 - 0.5616 , 5) * money * 2
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',-money) # 0.5617 - AUDUSD_diff
        Equal(account.AUDUSD_hold[0].volume,-money)
        account.update(AUDUSD.get_data()) # 0.5616
        account.trade_money('AUDUSD',-2 * money) # 0.5617 + AUDUSD_diff
        Equal(account.AUDUSD_hold[0].volume,-1 * money)
        Equal(account.AUDUSD_hold[1].volume,-2 * money)
        Equal(account.AUDUSD_hold[0].data.price,price0)
        Equal(account.AUDUSD_hold[1].data.price,price1)
        Equal(account.AUDUSD_hold[0].profit,profit0)
        Equal(account.AUDUSD_hold[1].profit,profit1)

    def test_hold_profit_bull(self):
        Equal = self.assertEqual
        price = round(0.5617 + AUDUSD_diff , 5)
        profit = round(0.9500 - price , 5) * money
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',money) # 0.5617 - AUDUSD_diff
        for i in range(88):
            account.update(AUDUSD.get_data()) # 0.9500
        Equal(account.AUDUSD_hold[0].volume , money)
        Equal(account.AUDUSD_hold[0].data.price , price)
        Equal(account.AUDUSD_hold[0].profit , profit)

    def test_hold_record_multiple_positive(self):
        Equal = self.assertEqual
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',money) # 0.5617 + AUDUSD_diff
        account.update(AUDUSD.get_data()) # 0.5616
        account.trade_money('AUDUSD',2*money) # 0.5616 - AUDUSD_diff
        Equal(account.AUDUSD_hold_record[0].data.date_time,datetime(2001,1,2,23,1))
        Equal(account.AUDUSD_hold_record[0].volume,money)
        Equal(account.AUDUSD_hold_record[1].volume,3*money)
        Equal(account.AUDUSD_hold_record[1].data.date_time,datetime(2001,1,2,23,2))

    def test_hold_record_multiple_negative(self):
        Equal = self.assertEqual
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',-money) # 0.5617 - AUDUSD_diff
        account.update(AUDUSD.get_data()) # 0.5616
        account.trade_money('AUDUSD',-2*money) # 0.5616 - AUDUSD_diff
        Equal(account.AUDUSD_hold_record[0].volume,-money)
        Equal(account.AUDUSD_hold_record[0].data.date_time,datetime(2001,1,2,23,1))
        Equal(account.AUDUSD_hold_record[1].volume,-3*money)
        Equal(account.AUDUSD_hold_record[1].data.date_time,datetime(2001,1,2,23,2))

    def test_hold_record_positive_to_negative(self):
        Equal = self.assertEqual
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',money) # 0.5617 + AUDUSD_diff
        account.update(AUDUSD.get_data()) # 0.5616
        account.trade_money('AUDUSD',-2*money) # 0.5616 - AUDUSD_diff
        Equal(account.AUDUSD_hold_record[0].volume,money)
        Equal(account.AUDUSD_hold_record[0].data.date_time,datetime(2001,1,2,23,1))
        Equal(account.AUDUSD_hold_record[1].volume,-money)
        Equal(account.AUDUSD_hold_record[1].data.date_time,datetime(2001,1,2,23,2))

    def test_hold_record_negative_to_positive(self):
        Equal = self.assertEqual
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',-money) # 0.5617 - AUDUSD_diff
        account.update(AUDUSD.get_data()) # 0.5616
        account.trade_money('AUDUSD',2*money) # 0.5616 + AUDUSD_diff
        Equal(account.AUDUSD_hold_record[0].volume,-money)
        Equal(account.AUDUSD_hold_record[0].data.date_time,datetime(2001,1,2,23,1))
        Equal(account.AUDUSD_hold_record[1].volume,money)
        Equal(account.AUDUSD_hold_record[1].data.date_time,datetime(2001,1,2,23,2))

    def test_all_volume_positive(self):
        Equal = self.assertEqual
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data())# 0.5617
        account.trade_money('AUDUSD',money) # 0.5617 - AUDUSD_diff
        account.update(AUDUSD.get_data())# 0.5616
        account.trade_money('AUDUSD',2*money)# 0.5617 - AUDUSD_diff
        Equal(account.AUDUSD_volume(),3*money)

    def test_AUDUSD_volume_negative(self):
        Equal = self.assertEqual
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data())
        account.trade_money('AUDUSD',-money)
        Equal(account.AUDUSD_volume(),-money)
        account.update(AUDUSD.get_data())
        account.trade_money('AUDUSD',-2*money)
        Equal(account.AUDUSD_volume(),-3*money)

    def test_AUDUSD_volume_positive_to_negative(self):
        Equal = self.assertEqual
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data())
        account.trade_money('AUDUSD',money)
        Equal(account.AUDUSD_volume(),money)
        account.update(AUDUSD.get_data())
        account.trade_money('AUDUSD',-2*money)
        Equal(account.AUDUSD_volume(),-money)

    def test_AUDUSD_volume_negative_to_positive(self):
        Equal = self.assertEqual
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data())
        account.trade_money('AUDUSD',-money)
        Equal(account.AUDUSD_volume(),-money)
        account.update(AUDUSD.get_data())
        account.trade_money('AUDUSD',2*money)
        Equal(account.AUDUSD_volume(),money)

    def test_money_bull(self):
        Equal = self.assertEqual
        profit = round( (0.5616 - AUDUSD_diff) - (0.5617 + AUDUSD_diff) ,5) * money
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',money) # 0.5617 + AUDUSD_diff
        account.update(AUDUSD.get_data()) # 0.5616
        account.trade_money('AUDUSD',-money) # 0.5616 - AUDUSD_diff
        Equal(account.money , money + profit ) #0.5617+0.00006 -> 0.5616-0.00006

    def test_money_bear(self):
        Equal = self.assertEqual
        profit = round( (0.5617 - AUDUSD_diff) - (0.5616 + AUDUSD_diff) ,5) * money
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',-money) # 0.5617 - AUDUSD_diff
        account.update(AUDUSD.get_data()) # 0.5616
        account.trade_money('AUDUSD',money) # 0.5617 + AUDUSD_diff
        Equal(account.money,money + profit) #0.5617-0.00006 -> 0.5616+0.00006

    def test_money_bull_to_bear(self):
        Equal = self.assertEqual
        buy_price = round(0.5617 + AUDUSD_diff , 5)
        sell_price = round(0.5616 - AUDUSD_diff , 5)
        profit = round(sell_price -buy_price,5) * money
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',money) # 0.5617 + AUDUSD_diff
        account.update(AUDUSD.get_data()) # 0.5616
        account.trade_money('AUDUSD',- 2 * money) # 0.5616 - AUDUSD_diff
        Equal(money+profit,account.money) #0.5617 -> 0.5616

    def test_money_bear_to_bull(self):
        Equal = self.assertEqual
        buy_price = round(0.5616 + AUDUSD_diff , 5)
        sell_price = round(0.5617 - AUDUSD_diff , 5)
        profit = round(sell_price -buy_price,5) * money
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',- money) # 0.5617 - AUDUSD_diff
        account.update(AUDUSD.get_data()) # 0.5616
        account.trade_money('AUDUSD',2 * money) # 0.5617 + AUDUSD_diff
        Equal(money+profit,account.money) # 0.5617-0.00006->0.5616+0.00006

    def test_earn_bull(self):
        Equal = self.assertEqual
        buy_price = round(0.5617 + AUDUSD_diff , 5)
        sell_price = round(0.5616 - AUDUSD_diff , 5)
        profit = round(sell_price -buy_price,5) * money
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',money) # 0.5617 + AUDUSD_diff
        account.update(AUDUSD.get_data()) # 0.5616
        account.trade_money('AUDUSD',-money) # 0.5616 - AUDUSD_diff
        Equal(account.earn[0].profit,profit)
        Equal(account.earn[0].buy.data.price , buy_price)
        Equal(account.earn[0].sell.data.price , sell_price)
        Equal(account.earn[0].buy.volume , money)

    def test_earn_bear(self):
        Equal = self.assertEqual
        buy_price = round(0.5616 + AUDUSD_diff , 5)
        sell_price = round(0.5617 - AUDUSD_diff , 5)
        profit = round(sell_price -buy_price,5) * money
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',-money) # 0.5617 - AUDUSD_diff
        account.update(AUDUSD.get_data()) # 0.5616
        account.trade_money('AUDUSD',money) # 0.5616 + AUDUSD_diff
        Equal(account.earn[0].profit,profit)
        Equal(account.earn[0].buy.data.price , buy_price)
        Equal(account.earn[0].sell.data.price , sell_price)
        Equal(account.earn[0].buy.volume , money)

    def test_earn_bull_to_bear(self):
        Equal = self.assertEqual
        buy_price = round(0.5617 + AUDUSD_diff , 5)
        sell_price = round(0.5616 - AUDUSD_diff , 5)
        profit = round(sell_price -buy_price,5) * money
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data())
        account.trade_money('AUDUSD',money)
        account.update(AUDUSD.get_data())
        account.trade_money('AUDUSD',- 2 * money)
        Equal(account.earn[0].profit,profit)
        Equal(account.earn[0].buy.data.price , buy_price)
        Equal(account.earn[0].sell.data.price , sell_price)
        Equal(account.earn[0].buy.volume , money)

    def test_earn_bear_to_bull(self):
        Equal = self.assertEqual
        buy_price = round(0.5616 + AUDUSD_diff , 5)
        sell_price = round(0.5617 - AUDUSD_diff , 5)
        profit = round(sell_price -buy_price,5) * money
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data())
        account.trade_money('AUDUSD',-money)
        account.update(AUDUSD.get_data())
        account.trade_money('AUDUSD',2 * money)
        Equal(account.earn[0].profit,profit)
        Equal(account.earn[0].buy.data.price , buy_price)
        Equal(account.earn[0].sell.data.price , sell_price)
        Equal(account.earn[0].buy.volume , money)

    def test_AUDUSD_float_profit_bull(self):
        Equal = self.assertEqual
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data())
        account.trade_money('AUDUSD',money)
        account.update(AUDUSD.get_data())
        account.trade_money('AUDUSD',-money)
        Equal(account.AUDUSD_float_profit , 0)

    def test_AUDUSD_float_profit_bear(self):
        Equal = self.assertEqual
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data())
        account.trade_money('AUDUSD',money)
        account.update(AUDUSD.get_data())
        account.trade_money('AUDUSD',-money)
        Equal(account.AUDUSD_float_profit , 0)

    def test_AUDUSD_float_profit_bear(self):
        Equal = self.assertEqual
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data())
        account.trade_money('AUDUSD',-money)
        account.update(AUDUSD.get_data())
        account.trade_money('AUDUSD',money)
        Equal(account.AUDUSD_float_profit , 0)

    def test_AUDUSD_float_profit_multiple_bull(self):
        Equal = self.assertEqual
        price1 = round(0.5617 + AUDUSD_diff , 5)
        price2 = round(0.5616 + AUDUSD_diff , 5)
        profit1 = round((0.5616 - price1) * money , 5)
        profit2 = round((2 * 0.5616 - price1 - price2) * money , 5)
        profit3 = round((2 * 0.9505 - price1 - price2) * money , 5)
        profit4 = round((0.9505 - price2) * money , 5)
        profit5 = round((0.5616 - price2) * money , 5)
        # 0.5617 -> 0.5616 -> 0.9505 -> 0.5616
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',money) # 0.5617 + AUDUSD_diff
        account.update(AUDUSD.get_data()) # 0.5616
        Equal(account.AUDUSD_float_profit , profit1)
        account.trade_money('AUDUSD',money) # 0.5616 + AUDUSD_diff
        Equal(account.AUDUSD_float_profit , profit2)
        account.update(AUDUSD.get_data()) # 0.9505
        Equal(account.AUDUSD_float_profit , profit3)
        account.trade_money('AUDUSD',-money) # 0.9505 - AUDUSD_diff
        Equal(account.AUDUSD_float_profit , profit4)
        account.update(AUDUSD.get_data()) # 0.5616
        Equal(account.AUDUSD_float_profit , profit5)
        account.trade_money('AUDUSD',-money) # 0.5616 AUDUSD_diff
        Equal(account.AUDUSD_float_profit , 0)

    def test_AUDUSD_float_profit_multiple_bull(self):
        Equal = self.assertEqual
        price1 = round(0.5617 - AUDUSD_diff , 5)
        price2 = round(0.5616 - AUDUSD_diff , 5)
        profit1 = round((price1 - 0.5616) * money , 5)
        profit2 = round((price1 + price2 - 2 * 0.5616) * money , 5)
        profit3 = round((price1 + price2 - 2 * 0.9505) * money , 5)
        profit4 = round((price2 - 0.9505) * money , 5)
        profit5 = round((price2 - 0.5616) * money , 5)
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',-money)
        account.update(AUDUSD.get_data()) # 0.5616
        Equal(account.AUDUSD_float_profit , profit1)
        account.trade_money('AUDUSD',-money)
        Equal(account.AUDUSD_float_profit , profit2)
        account.update(AUDUSD.get_data()) # 0.9505
        Equal(account.AUDUSD_float_profit , profit3)
        account.trade_money('AUDUSD',money)
        Equal(account.AUDUSD_float_profit , profit4)
        account.update(AUDUSD.get_data()) # 0.5616
        Equal(account.AUDUSD_float_profit , profit5)
        account.trade_money('AUDUSD',money)
        Equal(account.AUDUSD_float_profit , 0)

    def test_AUDUSD_hold_profit_bear(self):
        Equal = self.assertEqual
        price1 = round( 0.5617 - AUDUSD_diff , 5)
        profit = round( price1 - 0.5616 , 5) * money
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',-money)
        account.update(AUDUSD.get_data()) # 0.5616
        Equal(account.AUDUSD_hold[0].profit , profit)
        account.trade_money('AUDUSD',money)
        Equal(len(account.AUDUSD_hold) , 0)
        account.update(AUDUSD.get_data()) # 0.9505
        Equal(len(account.AUDUSD_hold) , 0)

    def test_AUDUSD_hold_profit_bull(self):
        Equal = self.assertEqual
        price = round(0.5617 + AUDUSD_diff , 5)
        profit = round(0.5616 - price , 5) * money
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',money)
        account.update(AUDUSD.get_data()) # 0.5616
        Equal(account.AUDUSD_hold[0].profit , profit)
        account.trade_money('AUDUSD',-money)
        Equal(len(account.AUDUSD_hold) , 0)
        account.update(AUDUSD.get_data()) # 0.9505
        Equal(len(account.AUDUSD_hold) , 0)

    def test_stop_loss_bull(self):
        Equal = self.assertEqual
        price_buy = round(0.5617 + AUDUSD_diff , 5)
        price_sell = round(0.9495 - AUDUSD_diff , 5)
        profit = round(price_sell - price_buy , 5) * money
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.set_stop(100,0)
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',money)
        for i in range(91): # 0.9495 第93行 第92個價格
            account.update(AUDUSD.get_data())
        Equal(len(account.AUDUSD_hold),0)
        Equal(len(account.earn),1)
        Equal(account.earn[0].bull_or_bear,'bull')
        Equal(account.earn[0].sell.data.date_time,datetime(2001,1,3,0,49) )
        Equal(account.earn[0].buy.data.date_time,datetime(2001,1,2,23,1) )
        Equal(account.earn[0].sell.data.price,price_sell)
        Equal(account.earn[0].buy.data.price,price_buy)
        Equal(account.earn[0].money,money + profit)
        Equal(account.earn[0].profit,profit)

    def test_stop_loss_hold_record_bull(self):
        Equal = self.assertEqual
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.set_stop(100,0)
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',money)
        for i in range(91): # 0.9495 第93行 第92個價格
            account.update(AUDUSD.get_data())
        Equal(len(account.AUDUSD_hold_record),2)
        Equal(account.AUDUSD_hold_record[0].data.date_time,datetime(2001,1,2,23,1))
        Equal(account.AUDUSD_hold_record[1].data.date_time,datetime(2001,1,3,0,49))
        Equal(account.AUDUSD_hold_record[0].volume,money)
        Equal(account.AUDUSD_hold_record[1].volume,0)

    def test_stop_loss_bear(self):
        Equal = self.assertEqual
        sell_price = round(0.5617 - AUDUSD_diff , 5)
        buy_price = round(0.9529 + AUDUSD_diff , 5)
        profit = round(sell_price - buy_price , 5) * money
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.set_stop(100,0)
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',-money)
        for i in range(516): # 0.9529 第518行 第517個價格
            account.update(AUDUSD.get_data())
        Equal(len(account.AUDUSD_hold),0)
        Equal(len(account.earn),1)
        Equal(account.earn[0].bull_or_bear,'bear')
        Equal(account.earn[0].buy.data.date_time,datetime(2001,1,3,8,11) )
        Equal(account.earn[0].sell.data.date_time,datetime(2001,1,2,23,1) )
        Equal(account.earn[0].money,money + profit)
        Equal(account.earn[0].profit , profit)

    def test_stop_loss_hold_record_bear(self):
        Equal = self.assertEqual
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.set_stop(100,0)
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',-money)
        for i in range(516): # 0.9529 第518行 第517個價格
            account.update(AUDUSD.get_data())
        Equal(len(account.AUDUSD_hold_record),2)
        Equal(account.AUDUSD_hold_record[0].data.date_time,datetime(2001,1,2,23,1))
        Equal(account.AUDUSD_hold_record[1].data.date_time,datetime(2001,1,3,8,11))
        Equal(account.AUDUSD_hold_record[0].volume,-money)
        Equal(account.AUDUSD_hold_record[1].volume,0)

    def test_stop_win_earn_bull(self):
        Equal = self.assertEqual
        buy_price = round(0.5617 + AUDUSD_diff , 5)
        sell_price = round(0.9529 - AUDUSD_diff , 5)
        profit = round((sell_price - buy_price) * money, 5)
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.set_stop(0,100)
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',money)
        for i in range(516): # 0.9529 第518行 第517個價格
            account.update(AUDUSD.get_data())
        Equal(len(account.AUDUSD_hold),0)
        Equal(len(account.earn),1)
        Equal(account.earn[0].bull_or_bear,'bull')
        Equal(account.earn[0].buy.data.date_time,datetime(2001,1,2,23,1) )
        Equal(account.earn[0].sell.data.date_time,datetime(2001,1,3,8,11) )
        Equal(account.earn[0].money,money + profit)
        Equal(account.earn[0].profit,profit)

    def test_stop_win_hold_record_bull(self):
        Equal = self.assertEqual
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.set_stop(0,100)
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',money)
        for i in range(516): # 0.9529 第518行 第517個價格
            account.update(AUDUSD.get_data())
        Equal(len(account.AUDUSD_hold_record),2)
        Equal(account.AUDUSD_hold_record[0].data.date_time,datetime(2001,1,2,23,1))
        Equal(account.AUDUSD_hold_record[1].data.date_time,datetime(2001,1,3,8,11))
        Equal(account.AUDUSD_hold_record[0].volume,money)
        Equal(account.AUDUSD_hold_record[1].volume,0)

    def test_stop_win_earn_bear(self):
        Equal = self.assertEqual
        sell_price = round(0.5617 - AUDUSD_diff , 5)
        buy_price = round(0.9495+AUDUSD_diff , 5)
        profit = round((sell_price - buy_price) * money , 5)
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.set_stop(0,100)
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',-money)
        for i in range(91): # 0.9495 第93行 第92個價格
            account.update(AUDUSD.get_data())
        Equal(len(account.AUDUSD_hold),0)
        Equal(len(account.earn),1)
        Equal(account.earn[0].bull_or_bear,'bear')
        Equal(account.earn[0].buy.data.date_time,datetime(2001,1,3,0,49) )
        Equal(account.earn[0].sell.data.date_time,datetime(2001,1,2,23,1) )
        Equal(account.earn[0].money,money + profit)
        Equal(account.earn[0].profit,profit)

    def test_stop_win_hold_record_bear(self):
        Equal = self.assertEqual
        account = Account(money)
        AUDUSD = Currency('AUDUSD','2001-1','2001-1')
        account.set_stop(0,100)
        account.update(AUDUSD.get_data()) # 0.5617
        account.trade_money('AUDUSD',-money)
        for i in range(91): # 0.9495 第93行 第92個價格
            account.update(AUDUSD.get_data())
        Equal(len(account.AUDUSD_hold_record),2)
        Equal(account.AUDUSD_hold_record[0].data.date_time,datetime(2001,1,2,23,1))
        Equal(account.AUDUSD_hold_record[1].data.date_time,datetime(2001,1,3,0,49))
        Equal(account.AUDUSD_hold_record[0].volume,-money)
        Equal(account.AUDUSD_hold_record[1].volume,0)
    '''
if __name__ == '__main__':
    AUDUSD_diff = 0.00007
    money = 100000
    unittest.main()

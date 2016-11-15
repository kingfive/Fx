import sys
sys.path.append('../')

from account import Account
from currency import Currency
from form import *
import unittest
import test
from datetime import datetime


EURUSD_diff = 0.00006
money = 100000

'''
earn 的 money 尚未測 但結果正確
profit需要測試 結果應正確
停損停利先不用測
'''

class utAccount(unittest.TestCase):
    '''
    argument set :
        money : 100000
        EURUSD difference : 0.00006
    '''

    def test_one(self):
        self.assertEqual(1,1)

    def test_hold_bull_1(self):
        Equal = self.assertEqual
        price1 = round(0.9507 + EURUSD_diff , 5)
        price2 = round(0.9506 + EURUSD_diff , 5)
        profit1 = round(0.9507 - price1 , 5) * money
        profit2 = round(0.9506 - price1 , 5) * money
        profit3 = round(0.9506 - price2 , 5) * money * 2
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',money) # 0.9507 + EURUSD_diff
        Equal(len(account.EURUSD_hold),1)
        Equal(account.EURUSD_hold[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold[0].volume , money)
        Equal(account.EURUSD_hold[0].data.price , price1)
        Equal(account.EURUSD_hold[0].profit , profit1)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(len(account.EURUSD_hold),1)
        Equal(account.EURUSD_hold[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold[0].volume , money)
        Equal(account.EURUSD_hold[0].data.price , price1)
        Equal(account.EURUSD_hold[0].profit , profit2)
        account.trade_money('EURUSD',2*money) # 0.9506 + EURUSD_diff
        Equal(len(account.EURUSD_hold),2)
        Equal(account.EURUSD_hold[1].data.date_time , datetime(2001,1,2,23,2))
        Equal(account.EURUSD_hold[1].volume , 2*money)
        Equal(account.EURUSD_hold[1].data.price , price2)
        Equal(account.EURUSD_hold[1].profit , profit3)

    def test_hold_bear_2(self):
        Equal = self.assertEqual
        price1 = round(0.9507 - EURUSD_diff , 5)
        price2 = round(0.9506 - EURUSD_diff , 5)
        profit1 = round(price1 - 0.9507  , 5) * money
        profit2 = round(price1 - 0.9506  , 5) * money
        profit3 = round(price2 - 0.9506  , 5) * money * 2
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-money) # 0.9507 - EURUSD_diff
        Equal(len(account.EURUSD_hold),1)
        Equal(account.EURUSD_hold[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold[0].volume , -money)
        Equal(account.EURUSD_hold[0].data.price , price1)
        Equal(account.EURUSD_hold[0].profit , profit1)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(len(account.EURUSD_hold),1)
        Equal(account.EURUSD_hold[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold[0].volume , -money)
        Equal(account.EURUSD_hold[0].data.price , price1)
        Equal(account.EURUSD_hold[0].profit , profit2)
        account.trade_money('EURUSD',-2*money) # 0.9506 - EURUSD_diff
        Equal(len(account.EURUSD_hold),2)
        Equal(account.EURUSD_hold[1].data.date_time , datetime(2001,1,2,23,2))
        Equal(account.EURUSD_hold[1].volume,-2*money)
        Equal(account.EURUSD_hold[1].data.price,price2)
        Equal(account.EURUSD_hold[1].profit,profit3)

    def test_hold_bull_to_bear_3(self):
        Equal = self.assertEqual
        price = round(0.9507 + EURUSD_diff , 5)
        profit1 = round(0.9507 - price , 5) * money
        profit2 = round(0.9506 - price , 5) * money
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',money) # 0.9507 + EURUSD_diff
        Equal(len(account.EURUSD_hold),1)
        Equal(account.EURUSD_hold[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold[0].volume , money)
        Equal(account.EURUSD_hold[0].data.price , price)
        Equal(account.EURUSD_hold[0].profit , profit1)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(len(account.EURUSD_hold),1)
        Equal(account.EURUSD_hold[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold[0].volume , money)
        Equal(account.EURUSD_hold[0].data.price , price)
        Equal(account.EURUSD_hold[0].profit , profit2)
        account.trade_money('EURUSD',-money) # 0.9506 - EURUSD_diff
        Equal(len(account.EURUSD_hold),0)

    def test_hold_bear_to_bull_4(self):
        Equal = self.assertEqual
        price = round(0.9507 - EURUSD_diff , 5)
        profit1 = round(price - 0.9507  , 5) * money
        profit2 = round(price - 0.9506 , 5) * money
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-money) # 0.9507 + EURUSD_diff
        Equal(len(account.EURUSD_hold),1)
        Equal(account.EURUSD_hold[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold[0].volume , -money)
        Equal(account.EURUSD_hold[0].data.price , price)
        Equal(account.EURUSD_hold[0].profit , profit1)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(len(account.EURUSD_hold),1)
        Equal(account.EURUSD_hold[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold[0].volume , -money)
        Equal(account.EURUSD_hold[0].data.price , price)
        Equal(account.EURUSD_hold[0].profit , profit2)
        account.trade_money('EURUSD',money) # 0.9506 - EURUSD_diff
        Equal(len(account.EURUSD_hold),0)

    def test_hold_two_bull_to_bear_5(self):
        Equal = self.assertEqual
        price1 = round(0.9507 + EURUSD_diff , 5)
        profit1 = round(0.9507 - price1 , 5) * money * 2
        profit2 = round(0.9506 - price1 , 5) * money * 2
        profit3 = round(0.9506 - price1 , 5) * money
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',2*money) # 0.9507 - EURUSD_diff
        Equal(len(account.EURUSD_hold),1)
        Equal(account.EURUSD_hold[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold[0].volume , 2*money)
        Equal(account.EURUSD_hold[0].data.price , price1)
        Equal(account.EURUSD_hold[0].profit , profit1)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(len(account.EURUSD_hold),1)
        Equal(account.EURUSD_hold[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold[0].volume , 2*money)
        Equal(account.EURUSD_hold[0].data.price , price1)
        Equal(account.EURUSD_hold[0].profit , profit2)
        account.trade_money('EURUSD',-money) # 0.9506 + EURUSD_diff
        Equal(len(account.EURUSD_hold),1)
        Equal(account.EURUSD_hold[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold[0].volume , money)
        Equal(account.EURUSD_hold[0].data.price , price1)
        Equal(account.EURUSD_hold[0].profit , profit3)

    def test_hold_two_bear_to_bull_6(self):
        Equal = self.assertEqual
        price1 = round(0.9507 - EURUSD_diff , 5)
        profit1 = round(price1 - 0.9507 , 5) * money * 2
        profit2 = round(price1 - 0.9506 , 5) * money * 2
        profit3 = round(price1 - 0.9506 , 5) * money
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-2*money) # 0.9507 + EURUSD_diff
        Equal(len(account.EURUSD_hold),1)
        Equal(account.EURUSD_hold[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold[0].volume , -2*money)
        Equal(account.EURUSD_hold[0].data.price , price1)
        Equal(account.EURUSD_hold[0].profit , profit1)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(len(account.EURUSD_hold),1)
        Equal(account.EURUSD_hold[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold[0].volume , -2*money)
        Equal(account.EURUSD_hold[0].data.price , price1)
        Equal(account.EURUSD_hold[0].profit , profit2)
        account.trade_money('EURUSD',money) # 0.9506 - EURUSD_diff
        Equal(len(account.EURUSD_hold),1)
        Equal(account.EURUSD_hold[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold[0].volume , -money)
        Equal(account.EURUSD_hold[0].data.price , price1)
        Equal(account.EURUSD_hold[0].profit , profit3)

    def test_hold_bull_to_two_bear_7(self):
        Equal = self.assertEqual
        price1 = round(0.9507 + EURUSD_diff , 5)
        price2 = round(0.9506 - EURUSD_diff , 5)
        profit1 = round(0.9507 - price1 , 5) * money
        profit2 = round(0.9506 - price1 , 5) * money
        profit3 = round(price2 - 0.9506 , 5) * money
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',money) # 0.9507 - EURUSD_diff
        Equal(len(account.EURUSD_hold),1)
        Equal(account.EURUSD_hold[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold[0].volume , money)
        Equal(account.EURUSD_hold[0].data.price , price1)
        Equal(account.EURUSD_hold[0].profit , profit1)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(len(account.EURUSD_hold),1)
        Equal(account.EURUSD_hold[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold[0].volume , money)
        Equal(account.EURUSD_hold[0].data.price , price1)
        Equal(account.EURUSD_hold[0].profit , profit2)
        account.trade_money('EURUSD',-2 * money) # 0.9507 + EURUSD_diff
        Equal(len(account.EURUSD_hold),1)
        Equal(account.EURUSD_hold[0].data.date_time , datetime(2001,1,2,23,2))
        Equal(account.EURUSD_hold[0].volume , -money)
        Equal(account.EURUSD_hold[0].data.price , price2)
        Equal(account.EURUSD_hold[0].profit , profit3)

    def test_hold_bear_to_two_bull_8(self):
        Equal = self.assertEqual
        price1 = round(0.9507 - EURUSD_diff , 5)
        price2 = round(0.9506 + EURUSD_diff , 5)
        profit1 = round(price1 - 0.9507 , 5) * money
        profit2 = round(price1 - 0.9506 , 5) * money
        profit3 = round(0.9506 - price2 , 5) * money
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-money) # 0.9507 - EURUSD_diff
        Equal(len(account.EURUSD_hold),1)
        Equal(account.EURUSD_hold[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold[0].volume , -money)
        Equal(account.EURUSD_hold[0].data.price , price1)
        Equal(account.EURUSD_hold[0].profit , profit1)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(len(account.EURUSD_hold),1)
        Equal(account.EURUSD_hold[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold[0].volume , -money)
        Equal(account.EURUSD_hold[0].data.price , price1)
        Equal(account.EURUSD_hold[0].profit , profit2)
        account.trade_money('EURUSD',2 * money) # 0.9507 + EURUSD_diff
        Equal(len(account.EURUSD_hold),1)
        Equal(account.EURUSD_hold[0].data.date_time , datetime(2001,1,2,23,2))
        Equal(account.EURUSD_hold[0].volume , money)
        Equal(account.EURUSD_hold[0].data.price , price2)
        Equal(account.EURUSD_hold[0].profit , profit3)

    def test_hold_record_bull_1(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',money) # 0.9507 + EURUSD_diff
        Equal(len(account.EURUSD_hold_record),1)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , money)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(len(account.EURUSD_hold_record),1)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , money)
        account.trade_money('EURUSD',2*money) # 0.9506 - EURUSD_diff
        Equal(len(account.EURUSD_hold_record),2)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , money)
        Equal(account.EURUSD_hold_record[1].volume , 3*money)
        Equal(account.EURUSD_hold_record[1].data.date_time , datetime(2001,1,2,23,2))

    def test_hold_record_bear_2(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-money) # 0.9507 - EURUSD_diff
        Equal(len(account.EURUSD_hold_record),1)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , -money)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(len(account.EURUSD_hold_record),1)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , -money)
        account.trade_money('EURUSD',-2*money) # 0.9506 - EURUSD_diff
        Equal(len(account.EURUSD_hold_record),2)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , -money)
        Equal(account.EURUSD_hold_record[1].data.date_time , datetime(2001,1,2,23,2))
        Equal(account.EURUSD_hold_record[1].volume , -3*money)

    def test_hold_record_bull_to_bear_3(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',money) # 0.9507 + EURUSD_diff
        Equal(len(account.EURUSD_hold_record),1)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , money)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(len(account.EURUSD_hold_record),1)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , money)
        account.trade_money('EURUSD',-money) # 0.9506 - EURUSD_diff
        Equal(len(account.EURUSD_hold_record),2)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , money)
        Equal(account.EURUSD_hold_record[1].data.date_time , datetime(2001,1,2,23,2))
        Equal(account.EURUSD_hold_record[1].volume ,0)

    def test_hold_record_bear_to_bull_4(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-money) # 0.9507 - EURUSD_diff
        Equal(len(account.EURUSD_hold_record),1)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , -money)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(len(account.EURUSD_hold_record),1)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , -money)
        account.trade_money('EURUSD',money) # 0.9506 + EURUSD_diff
        Equal(len(account.EURUSD_hold_record),2)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , -money)
        Equal(account.EURUSD_hold_record[1].data.date_time , datetime(2001,1,2,23,2))
        Equal(account.EURUSD_hold_record[1].volume ,0)

    def test_hold_record_two_bull_to_bear_5(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-2*money) # 0.9507 - EURUSD_diff
        Equal(len(account.EURUSD_hold_record),1)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , -2*money)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(len(account.EURUSD_hold_record),1)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , -2*money)
        account.trade_money('EURUSD',money) # 0.9506 + EURUSD_diff
        Equal(len(account.EURUSD_hold_record),2)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , -2*money)
        Equal(account.EURUSD_hold_record[1].data.date_time , datetime(2001,1,2,23,2))
        Equal(account.EURUSD_hold_record[1].volume ,-money)

    def test_hold_record_two_bull_to_bear_5(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',2*money) # 0.9507 - EURUSD_diff
        Equal(len(account.EURUSD_hold_record),1)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , 2*money)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(len(account.EURUSD_hold_record),1)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , 2*money)
        account.trade_money('EURUSD',-money) # 0.9506 + EURUSD_diff
        Equal(len(account.EURUSD_hold_record),2)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , 2*money)
        Equal(account.EURUSD_hold_record[1].data.date_time , datetime(2001,1,2,23,2))
        Equal(account.EURUSD_hold_record[1].volume ,money)

    def test_hold_record_two_bear_to_bull_6(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-2*money) # 0.9507 - EURUSD_diff
        Equal(len(account.EURUSD_hold_record),1)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , -2*money)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(len(account.EURUSD_hold_record),1)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , -2*money)
        account.trade_money('EURUSD',money) # 0.9506 + EURUSD_diff
        Equal(len(account.EURUSD_hold_record),2)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , -2*money)
        Equal(account.EURUSD_hold_record[1].data.date_time , datetime(2001,1,2,23,2))
        Equal(account.EURUSD_hold_record[1].volume ,-money)

    def test_hold_record_bull_to_two_bear_7(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',money) # 0.9507 - EURUSD_diff
        Equal(len(account.EURUSD_hold_record),1)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , money)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(len(account.EURUSD_hold_record),1)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , money)
        account.trade_money('EURUSD',-2*money) # 0.9506 + EURUSD_diff
        Equal(len(account.EURUSD_hold_record),2)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , money)
        Equal(account.EURUSD_hold_record[1].data.date_time , datetime(2001,1,2,23,2))
        Equal(account.EURUSD_hold_record[1].volume ,-money)

    def test_hold_record_bear_to_two_bull_8(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-money) # 0.9507 - EURUSD_diff
        Equal(len(account.EURUSD_hold_record),1)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , -money)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(len(account.EURUSD_hold_record),1)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , -money)
        account.trade_money('EURUSD',2*money) # 0.9506 + EURUSD_diff
        Equal(len(account.EURUSD_hold_record),2)
        Equal(account.EURUSD_hold_record[0].data.date_time , datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[0].volume , -money)
        Equal(account.EURUSD_hold_record[1].data.date_time , datetime(2001,1,2,23,2))
        Equal(account.EURUSD_hold_record[1].volume , money)

    def test_EURUSD_order_history_bull_1(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',money) # 0.9507 - EURUSD_diff
        Equal(account.EURUSD_order_history[0].data.date_time,datetime(2001,1,2,23,1))
        Equal(account.EURUSD_order_history[0].volume,money)
        Equal(len(account.EURUSD_order_history),1)
        account.update(EURUSD.get_data()) # 0.9506
        account.trade_money('EURUSD',2*money) # 0.9506 + EURUSD_diff
        Equal(account.EURUSD_order_history[1].data.date_time,datetime(2001,1,2,23,2))
        Equal(account.EURUSD_order_history[1].volume,2*money)
        Equal(len(account.EURUSD_order_history),2)

    def test_EURUSD_order_history_bear_2(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-money) # 0.9507 - EURUSD_diff
        Equal(account.EURUSD_order_history[0].data.date_time,datetime(2001,1,2,23,1))
        Equal(account.EURUSD_order_history[0].volume,-money)
        Equal(len(account.EURUSD_order_history),1)
        account.update(EURUSD.get_data()) # 0.9506
        account.trade_money('EURUSD',-2*money) # 0.9506 + EURUSD_diff
        Equal(account.EURUSD_order_history[1].data.date_time,datetime(2001,1,2,23,2))
        Equal(account.EURUSD_order_history[1].volume,-2*money)
        Equal(len(account.EURUSD_order_history),2)

    def test_EURUSD_order_history_bull_to_bear_3(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',money) # 0.9507 - EURUSD_diff
        Equal(account.EURUSD_order_history[0].data.date_time,datetime(2001,1,2,23,1))
        Equal(account.EURUSD_order_history[0].volume,money)
        Equal(len(account.EURUSD_order_history),1)
        account.update(EURUSD.get_data()) # 0.9506
        account.trade_money('EURUSD',-money) # 0.9506 + EURUSD_diff
        Equal(account.EURUSD_order_history[1].data.date_time,datetime(2001,1,2,23,2))
        Equal(account.EURUSD_order_history[1].volume,-money)
        Equal(len(account.EURUSD_order_history),2)

    def test_EURUSD_order_history_bear_to_bull_4(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-money) # 0.9507 - EURUSD_diff
        Equal(account.EURUSD_order_history[0].data.date_time,datetime(2001,1,2,23,1))
        Equal(account.EURUSD_order_history[0].volume,-money)
        Equal(len(account.EURUSD_order_history),1)
        account.update(EURUSD.get_data()) # 0.9506
        account.trade_money('EURUSD',money) # 0.9506 + EURUSD_diff
        Equal(account.EURUSD_order_history[1].data.date_time,datetime(2001,1,2,23,2))
        Equal(account.EURUSD_order_history[1].volume,money)
        Equal(len(account.EURUSD_order_history),2)

    def test_EURUSD_order_history_two_bull_to_bear_5(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',2*money) # 0.9507 - EURUSD_diff
        Equal(account.EURUSD_order_history[0].data.date_time,datetime(2001,1,2,23,1))
        Equal(account.EURUSD_order_history[0].volume,2*money)
        Equal(len(account.EURUSD_order_history),1)
        account.update(EURUSD.get_data()) # 0.9506
        account.trade_money('EURUSD',-money) # 0.9506 + EURUSD_diff
        Equal(account.EURUSD_order_history[1].data.date_time,datetime(2001,1,2,23,2))
        Equal(account.EURUSD_order_history[1].volume,-money)
        Equal(len(account.EURUSD_order_history),2)

    def test_EURUSD_order_history_two_bear_to_bull_6(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-2*money) # 0.9507 - EURUSD_diff
        Equal(account.EURUSD_order_history[0].data.date_time,datetime(2001,1,2,23,1))
        Equal(account.EURUSD_order_history[0].volume,-2*money)
        Equal(len(account.EURUSD_order_history),1)
        account.update(EURUSD.get_data()) # 0.9506
        account.trade_money('EURUSD',money) # 0.9506 + EURUSD_diff
        Equal(account.EURUSD_order_history[1].data.date_time,datetime(2001,1,2,23,2))
        Equal(account.EURUSD_order_history[1].volume,money)
        Equal(len(account.EURUSD_order_history),2)

    def test_EURUSD_order_history_bull_to_two_bear_7(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',money) # 0.9507 - EURUSD_diff
        Equal(account.EURUSD_order_history[0].data.date_time,datetime(2001,1,2,23,1))
        Equal(account.EURUSD_order_history[0].volume,money)
        Equal(len(account.EURUSD_order_history),1)
        account.update(EURUSD.get_data()) # 0.9506
        account.trade_money('EURUSD',-2*money) # 0.9506 + EURUSD_diff
        Equal(account.EURUSD_order_history[1].data.date_time,datetime(2001,1,2,23,2))
        Equal(account.EURUSD_order_history[1].volume,-2*money)
        Equal(len(account.EURUSD_order_history),2)

    def test_EURUSD_order_history_bear_to_two_bull_8(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-money) # 0.9507 - EURUSD_diff
        Equal(account.EURUSD_order_history[0].data.date_time,datetime(2001,1,2,23,1))
        Equal(account.EURUSD_order_history[0].volume,-money)
        Equal(len(account.EURUSD_order_history),1)
        account.update(EURUSD.get_data()) # 0.9506
        account.trade_money('EURUSD',2*money) # 0.9506 + EURUSD_diff
        Equal(account.EURUSD_order_history[1].data.date_time,datetime(2001,1,2,23,2))
        Equal(account.EURUSD_order_history[1].volume,2*money)
        Equal(len(account.EURUSD_order_history),2)

    def test_EURUSD_volume_bull_1(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data())# 0.9507
        account.trade_money('EURUSD',money) # 0.9507 - EURUSD_diff
        account.update(EURUSD.get_data())# 0.9506
        account.trade_money('EURUSD',2*money)# 0.9507 - EURUSD_diff
        Equal(account.EURUSD_volume(),3*money)

    def test_EURUSD_volume_bear_2(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data())
        account.trade_money('EURUSD',-money)
        Equal(account.EURUSD_volume(),-money)
        account.update(EURUSD.get_data())
        account.trade_money('EURUSD',-2*money)
        Equal(account.EURUSD_volume(),-3*money)

    def test_EURUSD_volume_bull_to_bear_3(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data())
        account.trade_money('EURUSD',money)
        Equal(account.EURUSD_volume(),money)
        account.update(EURUSD.get_data())
        account.trade_money('EURUSD',-money)
        Equal(account.EURUSD_volume(),0)

    def test_EURUSD_volume_bear_to_bull_4(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data())
        account.trade_money('EURUSD',-money)
        Equal(account.EURUSD_volume(),-money)
        account.update(EURUSD.get_data())
        account.trade_money('EURUSD',money)
        Equal(account.EURUSD_volume(),0)

    def test_EURUSD_volume_two_bull_to_bear_5(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data())
        account.trade_money('EURUSD',2*money)
        Equal(account.EURUSD_volume(),2*money)
        account.update(EURUSD.get_data())
        account.trade_money('EURUSD',-money)
        Equal(account.EURUSD_volume(),money)

    def test_EURUSD_volume_two_bear_to_bull_6(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data())
        account.trade_money('EURUSD',-2*money)
        Equal(account.EURUSD_volume(),-2*money)
        account.update(EURUSD.get_data())
        account.trade_money('EURUSD',money)
        Equal(account.EURUSD_volume(),-money)

    def test_EURUSD_volume_bull_to_two_bear_7(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data())
        account.trade_money('EURUSD',money)
        Equal(account.EURUSD_volume(),money)
        account.update(EURUSD.get_data())
        account.trade_money('EURUSD',-2*money)
        Equal(account.EURUSD_volume(),-money)

    def test_EURUSD_volume_bear_to_two_bull_8(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data())
        account.trade_money('EURUSD',-money)
        Equal(account.EURUSD_volume(),-money)
        account.update(EURUSD.get_data())
        account.trade_money('EURUSD',2*money)
        Equal(account.EURUSD_volume(),money)

    def test_EURUSD_float_profit_bull_1(self):
        Equal = self.assertEqual
        account = Account(money)
        price1 = round(0.9507 + EURUSD_diff , 5)
        price2 = round(0.9506 + EURUSD_diff , 5)
        profit1 = round(0.9507 - price1 , 5) * money
        profit2 = round(0.9506 - price1 , 5) * money
        profit3 = round(0.9506 - price1 , 5) * money + \
                  round(0.9506 - price2 , 5) * money * 2
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',money) # 0.9507 + EURUSD_diff
        Equal(account.EURUSD_float_profit , profit1)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(account.EURUSD_float_profit , profit2)
        account.trade_money('EURUSD',2*money)
        Equal(account.EURUSD_float_profit , profit3)

    def test_EURUSD_float_profit_bear_2(self):
        Equal = self.assertEqual
        account = Account(money)
        price1 = round(0.9507 - EURUSD_diff , 5)
        price2 = round(0.9506 - EURUSD_diff , 5)
        profit1 = round(price1 - 0.9507 , 5) * money
        profit2 = round(price1 - 0.9506 , 5) * money
        profit3 = round(price1 - 0.9506 , 5) * money + \
                  round(price2 - 0.9506 , 5) * money * 2
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-money) # 0.9507 + EURUSD_diff
        Equal(account.EURUSD_float_profit , profit1)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(account.EURUSD_float_profit , profit2)
        account.trade_money('EURUSD',-2*money)
        Equal(account.EURUSD_float_profit , profit3)

    def test_EURUSD_float_profit_bull_to_bear_3(self):
        Equal = self.assertEqual
        account = Account(money)
        price1 = round(0.9507 + EURUSD_diff , 5)
        profit1 = round(0.9507 - price1 , 5) * money
        profit2 = round(0.9506 - price1 , 5) * money
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',money) # 0.9507 + EURUSD_diff
        Equal(account.EURUSD_float_profit , profit1)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(account.EURUSD_float_profit , profit2)
        account.trade_money('EURUSD',-money) # 0.9506 - EURUSD_diff
        Equal(account.EURUSD_float_profit , 0)

    def test_EURUSD_float_profit_bear_to_bull_4(self):
        Equal = self.assertEqual
        account = Account(money)
        price1 = round(0.9507 - EURUSD_diff , 5)
        profit1 = round(price1 - 0.9507 , 5) * money
        profit2 = round(price1 - 0.9506 , 5) * money
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-money) # 0.9507 + EURUSD_diff
        Equal(account.EURUSD_float_profit , profit1)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(account.EURUSD_float_profit , profit2)
        account.trade_money('EURUSD',money) # 0.9506 - EURUSD_diff
        Equal(account.EURUSD_float_profit , 0)

    def test_EURUSD_float_profit_two_bull_to_bear_5(self):
        Equal = self.assertEqual
        account = Account(money)
        price1 = round(0.9507 + EURUSD_diff , 5)
        profit1 = round(0.9507 - price1 , 5) * money * 2
        profit2 = round(0.9506 - price1 , 5) * money * 2
        profit3 = round(0.9506 - price1 , 5) * money
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',2*money) # 0.9507 + EURUSD_diff
        Equal(account.EURUSD_float_profit , profit1)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(account.EURUSD_float_profit , profit2)
        account.trade_money('EURUSD',-money) # 0.9506 - EURUSD_diff
        Equal(account.EURUSD_float_profit , profit3)

    def test_EURUSD_float_profit_two_bear_to_bull_6(self):
        Equal = self.assertEqual
        account = Account(money)
        price1 = round(0.9507 - EURUSD_diff , 5)
        profit1 = round(price1 - 0.9507 , 5) * money * 2
        profit2 = round(price1 - 0.9506 , 5) * money * 2
        profit3 = round(price1 - 0.9506 , 5) * money
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-2*money) # 0.9507 + EURUSD_diff
        Equal(account.EURUSD_float_profit , profit1)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(account.EURUSD_float_profit , profit2)
        account.trade_money('EURUSD',money) # 0.9506 - EURUSD_diff
        Equal(account.EURUSD_float_profit , profit3)

    def test_EURUSD_float_profit_bull_to_two_bear_7(self):
        Equal = self.assertEqual
        account = Account(money)
        price1 = round(0.9507 + EURUSD_diff , 5)
        price2 = round(0.9506 - EURUSD_diff , 5)
        profit1 = round(0.9507 - price1 , 5) * money
        profit2 = round(0.9506 - price1 , 5) * money
        profit3 = round(price2 - 0.9506 , 5) * money
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',money) # 0.9507 + EURUSD_diff
        Equal(account.EURUSD_float_profit , profit1)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(account.EURUSD_float_profit , profit2)
        account.trade_money('EURUSD',-2*money) # 0.9506 - EURUSD_diff
        Equal(account.EURUSD_float_profit , profit3)

    def test_EURUSD_float_profit_bear_to_two_bull_8(self):
        Equal = self.assertEqual
        account = Account(money)
        price1 = round(0.9507 - EURUSD_diff , 5)
        price2 = round(0.9506 + EURUSD_diff , 5)
        profit1 = round(price1 - 0.9507 , 5) * money
        profit2 = round(price1 - 0.9506 , 5) * money
        profit3 = round(0.9506 - price2 , 5) * money
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-money) # 0.9507 + EURUSD_diff
        Equal(account.EURUSD_float_profit , profit1)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(account.EURUSD_float_profit , profit2)
        account.trade_money('EURUSD',2*money) # 0.9506 - EURUSD_diff
        Equal(account.EURUSD_float_profit , profit3)

    def test_money_bull_1(self):
        Equal = self.assertEqual
        price1 = round(0.9507 + EURUSD_diff , 5)
        price2 = round(0.9506 + EURUSD_diff , 5)
        profit1 = round(0.9507 - price1 , 5) * money
        profit2 = round(0.9506 - price1 , 5) * money
        profit3 = round(0.9506 - price2 , 5) * money * 2
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',money) # 0.9507 + EURUSD_diff
        Equal(account.money , money + profit1 )
        account.update(EURUSD.get_data()) # 0.9506
        Equal(account.money , money + profit2 )
        account.trade_money('EURUSD',2*money) # 0.9506 - EURUSD_diff
        Equal(account.money , money + profit2 + profit3 )

    def test_money_bear_2(self):
        Equal = self.assertEqual
        price1 = round(0.9507 - EURUSD_diff , 5)
        price2 = round(0.9506 - EURUSD_diff , 5)
        profit1 = round(price1 - 0.9507 , 5) * money
        profit2 = round(price1 - 0.9506 , 5) * money
        profit3 = round(price2 - 0.9506 , 5) * money * 2
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-money) # 0.9507 + EURUSD_diff
        Equal(account.money , money + profit1 )
        account.update(EURUSD.get_data()) # 0.9506
        Equal(account.money , money + profit2 )
        account.trade_money('EURUSD',-2*money) # 0.9506 - EURUSD_diff
        Equal(account.money , money + profit2 + profit3 )

    def test_money_bull_to_bear_3(self):
        Equal = self.assertEqual
        price1 = round(0.9507 + EURUSD_diff , 5)
        price2 = round(0.9506 - EURUSD_diff , 5)
        profit1 = round(0.9507 - price1 , 5) * money
        profit2 = round(0.9506 - price1 , 5) * money
        profit3 = round(price2 - price1 , 5) * money
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',money) # 0.9507 + EURUSD_diff
        Equal(account.money , money + profit1 )
        account.update(EURUSD.get_data()) # 0.9506
        Equal(account.money , money + profit2 )
        account.trade_money('EURUSD',-money) # 0.9506 - EURUSD_diff
        Equal(account.money , money + profit3 )

    def test_money_bear_to_bull_4(self):
        Equal = self.assertEqual
        price1 = round(0.9507 + EURUSD_diff , 5)
        price2 = round(0.9506 - EURUSD_diff , 5)
        profit1 = round(0.9507 - price1 , 5) * money
        profit2 = round(0.9506 - price1 , 5) * money
        profit3 = round(price2 - price1 , 5) * money
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',money) # 0.9507 + EURUSD_diff
        Equal(account.money , money + profit1 )
        account.update(EURUSD.get_data()) # 0.9506
        Equal(account.money , money + profit2 )
        account.trade_money('EURUSD',-money) # 0.9506 - EURUSD_diff
        Equal(account.money , money + profit3 )

    def test_money_two_bull_to_bear_5(self):
        Equal = self.assertEqual
        price1 = round(0.9507 + EURUSD_diff , 5) # buy
        price2 = round(0.9506 - EURUSD_diff , 5) # sell
        profit1 = round(0.9507 - price1 , 5) * money * 2
        profit2 = round(0.9506 - price1 , 5) * money * 2
        profit3 = round(price2 - price1 , 5) * money + \
                  round(0.9506 - price1 , 5) * money # 一個money沖銷 一個仍留著
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',2*money) # 0.9507 + EURUSD_diff
        Equal(account.money , money + profit1 )
        account.update(EURUSD.get_data()) # 0.9506
        Equal(account.money , money + profit2 )
        account.trade_money('EURUSD',-money) # 0.9506 - EURUSD_diff
        Equal(account.money , money + profit3 )

    def test_money_two_bear_to_bull_6(self):
        Equal = self.assertEqual
        price1 = round(0.9507 - EURUSD_diff , 5)
        price2 = round(0.9506 + EURUSD_diff , 5)
        profit1 = round(price1 - 0.9507 , 5) * money * 2
        profit2 = round(price1 - 0.9506 , 5) * money * 2
        profit3 = round(price1 - price2 , 5) * money + \
                  round(price1 - 0.9506 , 5) * money
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-2*money) # 0.9507 + EURUSD_diff
        Equal(account.money , money + profit1 )
        account.update(EURUSD.get_data()) # 0.9506
        Equal(account.money , money + profit2 )
        account.trade_money('EURUSD',money) # 0.9506 - EURUSD_diff
        Equal(account.money , money + profit3 )

    def test_money_bull_to_two_bear_7(self):
        Equal = self.assertEqual
        price1 = round(0.9507 + EURUSD_diff , 5) # buy
        price2 = round(0.9506 - EURUSD_diff , 5) # sell
        profit1 = round(0.9507 - price1 , 5) * money
        profit2 = round(0.9506 - price1 , 5) * money
        profit3 = round(price2 - price1 , 5) * money + \
                  round(price2 - 0.9506 , 5) * money
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',money) # 0.9507 + EURUSD_diff
        Equal(account.money , money + profit1 )
        account.update(EURUSD.get_data()) # 0.9506
        Equal(account.money , money + profit2 )
        account.trade_money('EURUSD',-2*money) # 0.9506 - EURUSD_diff
        Equal(account.money , money + profit3 )

    def test_money_bear_to_two_bull_8(self):
        Equal = self.assertEqual
        price1 = round(0.9507 - EURUSD_diff , 5) # sell
        price2 = round(0.9506 + EURUSD_diff , 5) # buy
        profit1 = round(price1 - 0.9507 , 5) * money
        profit2 = round(price1 - 0.9506 , 5) * money
        profit3 = round(price1 - price2 , 5) * money + \
                  round(0.9506 - price2 , 5) * money
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-money) # 0.9507 + EURUSD_diff
        Equal(account.money , money + profit1 )
        account.update(EURUSD.get_data()) # 0.9506
        Equal(account.money , money + profit2 )
        account.trade_money('EURUSD',2*money) # 0.9506 - EURUSD_diff
        Equal(account.money , money + profit3 )

    def test_earn_bull_1(self):
        Equal = self.assertEqual
        buy_price = round(0.9507 + EURUSD_diff , 5)
        sell_price = round(0.9506 - EURUSD_diff , 5)
        profit = round(sell_price - buy_price , 5) * money
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',money) # 0.9507 + EURUSD_diff
        Equal(len(account.earn),0)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(len(account.earn),0)
        account.trade_money('EURUSD',-money) # 0.9506 - EURUSD_diff
        Equal(len(account.earn),1)
        Equal(account.earn[0].bull_or_bear , 'bull')
        Equal(account.earn[0].profit , profit)
        Equal(account.earn[0].buy.data.price , buy_price)
        Equal(account.earn[0].sell.data.price , sell_price)
        Equal(account.earn[0].buy.data.date_time , datetime(2001,1,2,23,1))
        Equal(account.earn[0].sell.data.date_time , datetime(2001,1,2,23,2))
        Equal(account.earn[0].buy.volume , money)
        Equal(account.earn[0].sell.volume , -money)

    def test_earn_bear_2(self):
        Equal = self.assertEqual
        buy_price = round(0.9506 + EURUSD_diff , 5)
        sell_price = round(0.9507 - EURUSD_diff , 5)
        profit = round(sell_price - buy_price , 5) * money
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-money) # 0.9507 - EURUSD_diff
        Equal(len(account.earn),0)
        account.update(EURUSD.get_data()) # 0.9506
        Equal(len(account.earn),0)
        account.trade_money('EURUSD',money) # 0.9506 + EURUSD_diff
        Equal(len(account.earn),1)
        Equal(account.earn[0].bull_or_bear , 'bear')
        Equal(account.earn[0].profit , profit)
        Equal(account.earn[0].buy.data.price , buy_price)
        Equal(account.earn[0].sell.data.price , sell_price)
        Equal(account.earn[0].buy.data.date_time , datetime(2001,1,2,23,2))
        Equal(account.earn[0].sell.data.date_time , datetime(2001,1,2,23,1))
        Equal(account.earn[0].buy.volume , money)
        Equal(account.earn[0].sell.volume , -money)

    def test_earn_bull_to_bear_3(self):
        Equal = self.assertEqual
        buy_price = round(0.9507 + EURUSD_diff , 5)
        sell_price = round(0.9506 - EURUSD_diff , 5)
        profit = round(sell_price - buy_price , 5) * money
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data())
        account.trade_money('EURUSD',money)
        Equal(len(account.earn),0)
        account.update(EURUSD.get_data())
        Equal(len(account.earn),0)
        account.trade_money('EURUSD',-money)
        Equal(len(account.earn),1)
        Equal(account.earn[0].bull_or_bear , 'bull')
        Equal(account.earn[0].profit , profit)
        Equal(account.earn[0].buy.data.price , buy_price)
        Equal(account.earn[0].sell.data.price , sell_price)
        Equal(account.earn[0].buy.data.date_time , datetime(2001,1,2,23,1))
        Equal(account.earn[0].sell.data.date_time , datetime(2001,1,2,23,2))
        Equal(account.earn[0].buy.volume , money)
        Equal(account.earn[0].sell.volume , -money)

    def test_earn_bear_to_bull_4(self):
        Equal = self.assertEqual
        buy_price = round(0.9506 + EURUSD_diff , 5)
        sell_price = round(0.9507 - EURUSD_diff , 5)
        profit = round(sell_price - buy_price,5) * money
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data())
        account.trade_money('EURUSD',-money)
        Equal(len(account.earn),0)
        account.update(EURUSD.get_data())
        Equal(len(account.earn),0)
        account.trade_money('EURUSD',2 * money)
        Equal(len(account.earn),1)
        Equal(account.earn[0].bull_or_bear , 'bear')
        Equal(account.earn[0].profit , profit)
        Equal(account.earn[0].buy.data.price , buy_price)
        Equal(account.earn[0].sell.data.price , sell_price)
        Equal(account.earn[0].buy.data.date_time , datetime(2001,1,2,23,2))
        Equal(account.earn[0].sell.data.date_time , datetime(2001,1,2,23,1))
        Equal(account.earn[0].buy.volume , money)
        Equal(account.earn[0].sell.volume , -money)

    def test_earn_two_bull_to_bear_5(self):
        Equal = self.assertEqual
        buy_price = round(0.9507 + EURUSD_diff , 5)
        sell_price = round(0.9506 - EURUSD_diff , 5)
        profit = round(sell_price - buy_price , 5) * money
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data())
        account.trade_money('EURUSD',2*money)
        Equal(len(account.earn),0)
        account.update(EURUSD.get_data())
        Equal(len(account.earn),0)
        account.trade_money('EURUSD',-money)
        Equal(len(account.earn),1)
        Equal(account.earn[0].bull_or_bear , 'bull')
        Equal(account.earn[0].profit , profit)
        Equal(account.earn[0].buy.data.price , buy_price)
        Equal(account.earn[0].sell.data.price , sell_price)
        Equal(account.earn[0].buy.data.date_time , datetime(2001,1,2,23,1))
        Equal(account.earn[0].sell.data.date_time , datetime(2001,1,2,23,2))
        Equal(account.earn[0].buy.volume , money)
        Equal(account.earn[0].sell.volume , -money)

    def test_earn_two_bear_to_bull_6(self):
        Equal = self.assertEqual
        buy_price = round(0.9506 + EURUSD_diff , 5)
        sell_price = round(0.9507 - EURUSD_diff , 5)
        profit = round(sell_price - buy_price , 5) * money
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data())
        account.trade_money('EURUSD',-2*money)
        Equal(len(account.earn),0)
        account.update(EURUSD.get_data())
        Equal(len(account.earn),0)
        account.trade_money('EURUSD',money)
        Equal(len(account.earn),1)
        Equal(account.earn[0].bull_or_bear , 'bear')
        Equal(account.earn[0].profit , profit)
        Equal(account.earn[0].buy.data.price , buy_price)
        Equal(account.earn[0].sell.data.price , sell_price)
        Equal(account.earn[0].buy.data.date_time , datetime(2001,1,2,23,2))
        Equal(account.earn[0].sell.data.date_time , datetime(2001,1,2,23,1))
        Equal(account.earn[0].buy.volume , money)
        Equal(account.earn[0].sell.volume , -money)

    def test_earn_bull_to_two_bear_7(self):
        Equal = self.assertEqual
        buy_price = round(0.9507 + EURUSD_diff , 5)
        sell_price = round(0.9506 - EURUSD_diff , 5)
        profit = round(sell_price - buy_price , 5) * money
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data())
        account.trade_money('EURUSD',money)
        Equal(len(account.earn),0)
        account.update(EURUSD.get_data())
        Equal(len(account.earn),0)
        account.trade_money('EURUSD',-2*money)
        Equal(len(account.earn),1)
        Equal(account.earn[0].bull_or_bear , 'bull')
        Equal(account.earn[0].profit , profit)
        Equal(account.earn[0].buy.data.price , buy_price)
        Equal(account.earn[0].sell.data.price , sell_price)
        Equal(account.earn[0].buy.data.date_time , datetime(2001,1,2,23,1))
        Equal(account.earn[0].sell.data.date_time , datetime(2001,1,2,23,2))
        Equal(account.earn[0].buy.volume , money)
        Equal(account.earn[0].sell.volume , -money)

    def test_earn_bear_to_two_bull_8(self):
        Equal = self.assertEqual
        buy_price = round(0.9506 + EURUSD_diff , 5)
        sell_price = round(0.9507 - EURUSD_diff , 5)
        profit = round(sell_price - buy_price , 5) * money
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.update(EURUSD.get_data())
        account.trade_money('EURUSD',-money)
        Equal(len(account.earn),0)
        account.update(EURUSD.get_data())
        Equal(len(account.earn),0)
        account.trade_money('EURUSD',2*money)
        Equal(len(account.earn),1)
        Equal(account.earn[0].bull_or_bear , 'bear')
        Equal(account.earn[0].profit , profit)
        Equal(account.earn[0].buy.data.price , buy_price)
        Equal(account.earn[0].sell.data.price , sell_price)
        Equal(account.earn[0].buy.data.date_time , datetime(2001,1,2,23,2))
        Equal(account.earn[0].sell.data.date_time , datetime(2001,1,2,23,1))
        Equal(account.earn[0].buy.volume , money)
        Equal(account.earn[0].sell.volume , -money)

    def test_stop_loss_hold_bull_1(self):
        Equal = self.assertEqual
        buy_price = round(0.9507 + EURUSD_diff , 5)
        sell_price = round(0.9495 - EURUSD_diff , 5)
        profit = round(sell_price - buy_price , 5) * money
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.set_stop(100,0)
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',money)
        Equal(len(account.EURUSD_hold),1)
        for i in range(91): # 0.9495 第93行 第92個價格
            account.update(EURUSD.get_data())
        Equal(len(account.EURUSD_hold),0)

    def test_stop_loss_hold_bear_2(self):
        Equal = self.assertEqual
        buy_price = round(0.9507 - EURUSD_diff , 5)
        sell_price = round(0.9495 + EURUSD_diff , 5)
        profit = round(sell_price - buy_price , 5) * money
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.set_stop(100,0)
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-money)
        for i in range(516): # 0.9529 第518行 第517個價格
            account.update(EURUSD.get_data())
        Equal(len(account.EURUSD_hold),0)


    def test_stop_loss_hold_record_bull_1(self):
        Equal = self.assertEqual
        buy_price = round(0.9507 + EURUSD_diff , 5)
        sell_price = round(0.9495 - EURUSD_diff , 5)
        profit = round(sell_price - buy_price , 5) * money
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.set_stop(100,0)
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',money)
        for i in range(91): # 0.9495 第93行 第92個價格
            account.update(EURUSD.get_data())
        Equal(len(account.EURUSD_hold),0)
        Equal(len(account.EURUSD_hold_record),2)
        Equal(len(account.earn),1)
        Equal(account.earn[0].bull_or_bear,'bull')
        Equal(account.earn[0].sell.data.date_time , datetime(2001,1,3,0,49) )
        Equal(account.earn[0].buy.data.date_time , datetime(2001,1,2,23,1) )
        Equal(account.earn[0].sell.data.price , sell_price)
        Equal(account.earn[0].buy.data.price , buy_price)
        Equal(account.earn[0].buy.volume , money)
        Equal(account.earn[0].sell.volume , -money)
        Equal(account.earn[0].money , money + profit)
        Equal(account.earn[0].profit , profit)

'''
    def test_stop_loss_hold_record_bull(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.set_stop(100,0)
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',money)
        for i in range(91): # 0.9495 第93行 第92個價格
            account.update(EURUSD.get_data())
        Equal(len(account.EURUSD_hold_record),2)
        Equal(account.EURUSD_hold_record[0].data.date_time,datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[1].data.date_time,datetime(2001,1,3,0,49))
        Equal(account.EURUSD_hold_record[0].volume,money)
        Equal(account.EURUSD_hold_record[1].volume,0)

    def test_stop_loss_bear(self):
        Equal = self.assertEqual
        sell_price = round(0.9507 - EURUSD_diff , 5)
        buy_price = round(0.9529 + EURUSD_diff , 5)
        profit = round(sell_price - buy_price , 5) * money
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.set_stop(100,0)
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-money)
        for i in range(516): # 0.9529 第518行 第517個價格
            account.update(EURUSD.get_data())
        Equal(len(account.EURUSD_hold),0)
        Equal(len(account.earn),1)
        Equal(account.earn[0].bull_or_bear,'bear')
        Equal(account.earn[0].buy.data.date_time,datetime(2001,1,3,8,11) )
        Equal(account.earn[0].sell.data.date_time,datetime(2001,1,2,23,1) )
        Equal(account.earn[0].money,money + profit)
        Equal(account.earn[0].profit , profit)

    def test_stop_loss_hold_record_bear(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.set_stop(100,0)
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-money)
        for i in range(516): # 0.9529 第518行 第517個價格
            account.update(EURUSD.get_data())
        Equal(len(account.EURUSD_hold_record),2)
        Equal(account.EURUSD_hold_record[0].data.date_time,datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[1].data.date_time,datetime(2001,1,3,8,11))
        Equal(account.EURUSD_hold_record[0].volume,-money)
        Equal(account.EURUSD_hold_record[1].volume,0)

    def test_stop_win_earn_bull(self):
        Equal = self.assertEqual
        buy_price = round(0.9507 + EURUSD_diff , 5)
        sell_price = round(0.9529 - EURUSD_diff , 5)
        profit = round((sell_price - buy_price) * money, 5)
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.set_stop(0,100)
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',money)
        for i in range(516): # 0.9529 第518行 第517個價格
            account.update(EURUSD.get_data())
        Equal(len(account.EURUSD_hold),0)
        Equal(len(account.earn),1)
        Equal(account.earn[0].bull_or_bear,'bull')
        Equal(account.earn[0].buy.data.date_time,datetime(2001,1,2,23,1) )
        Equal(account.earn[0].sell.data.date_time,datetime(2001,1,3,8,11) )
        Equal(account.earn[0].money,money + profit)
        Equal(account.earn[0].profit,profit)

    def test_stop_win_hold_record_bull(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.set_stop(0,100)
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',money)
        for i in range(516): # 0.9529 第518行 第517個價格
            account.update(EURUSD.get_data())
        Equal(len(account.EURUSD_hold_record),2)
        Equal(account.EURUSD_hold_record[0].data.date_time,datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[1].data.date_time,datetime(2001,1,3,8,11))
        Equal(account.EURUSD_hold_record[0].volume,money)
        Equal(account.EURUSD_hold_record[1].volume,0)

    def test_stop_win_earn_bear(self):
        Equal = self.assertEqual
        sell_price = round(0.9507 - EURUSD_diff , 5)
        buy_price = round(0.9495+EURUSD_diff , 5)
        profit = round((sell_price - buy_price) * money , 5)
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.set_stop(0,100)
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-money)
        for i in range(91): # 0.9495 第93行 第92個價格
            account.update(EURUSD.get_data())
        Equal(len(account.EURUSD_hold),0)
        Equal(len(account.earn),1)
        Equal(account.earn[0].bull_or_bear,'bear')
        Equal(account.earn[0].buy.data.date_time,datetime(2001,1,3,0,49) )
        Equal(account.earn[0].sell.data.date_time,datetime(2001,1,2,23,1) )
        Equal(account.earn[0].money,money + profit)
        Equal(account.earn[0].profit,profit)

    def test_stop_win_hold_record_bear(self):
        Equal = self.assertEqual
        account = Account(money)
        EURUSD = Currency('EURUSD','2001-1','2001-1')
        account.set_stop(0,100)
        account.update(EURUSD.get_data()) # 0.9507
        account.trade_money('EURUSD',-money)
        for i in range(91): # 0.9495 第93行 第92個價格
            account.update(EURUSD.get_data())
        Equal(len(account.EURUSD_hold_record),2)
        Equal(account.EURUSD_hold_record[0].data.date_time,datetime(2001,1,2,23,1))
        Equal(account.EURUSD_hold_record[1].data.date_time,datetime(2001,1,3,0,49))
        Equal(account.EURUSD_hold_record[0].volume,-money)
        Equal(account.EURUSD_hold_record[1].volume,0)
'''

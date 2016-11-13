import sys
sys.path.append('../')

from account import Account
from currency import Currency
from form import *
import unittest
import test
from datetime import datetime

class utCurrency(unittest.TestCase):

    def test_one(self):
        self.assertEqual(1,1)
    def test_new_currency(self):
        currency = Currency('EURUSD','2003-5','2006-5')
        while True:
            data = currency.get_data()
            if data == False:
                break
            print(data)

if __name__ == '__main__':
    unittest.main()

from form import Data
from datetime import datetime
import os
class Currency():

    def __init__(self,currency,first_range=None,last_range=None):
        self.__currency = currency
        self.first_range = first_range #string
        self.last_range = last_range #string
        if self.first_range != None :
            self.__now_year = int(self.first_range[0:4])
            self.__now_month = int(self.first_range[5:])
            self.__last_year = int(self.last_range[0:4])
            self.__last_month = int(self.last_range[5:])
            self.__change_path()
            self.__file_input = open('currency' + '/' +
                                currency + '/' +
                                self.first_range[0:4] + '-' +
                                self.first_range[5:] , 'rt')
        else:
            self.__now_year = 0 # 故意讓他們不相等
            self.__now_month = 1 # get_next_file 才能正常運作
            self.__last_year = 2
            self.__last_month = 3
            self.__file_input = open(currency,'rt')

    def get_data(self):
        '''
        This function can get a new data object from file
        If EOF ,
        return False
        '''

        line = self.__file_input.readline() # 讀第1行
        if  line.startswith('<TICKER>'): # 防止出現第1行垃圾資料
            line = self.__file_input.readline() #出現垃圾 再讀一行

        if not line: # 防止EOF
            if self.__get_next_file() == 'No File': # 換 file
                return False # No file , False
            line = self.__file_input.readline() # 換file 讀第1行

        line_split = line.split(",")
        currency = line_split[0]
        year = int(line_split[1][0:4])
        month = int(line_split[1][4:6])
        day = int(line_split[1][6:8])
        hour = int(line_split[2][0:2])
        minute = int(line_split[2][2:4])
        second = int(line_split[2][4:6])
        openn = float(line_split[3])
        high = float(line_split[4])
        low = float(line_split[5])
        close = float(line_split[6])
        timer = datetime(year,month,day,hour,minute,second)
        one_data = Data(currency,timer,openn,high,low,close)
        return one_data

    def __get_next_file(self):
        if self.__now_year == self.__last_year and self.__now_month == self.__last_month:
            return 'No File'
        if (self.__now_year < self.__last_year or
           (self.__now_year == self.__last_year and self.__now_month < self.__last_month) ):
            if self.__now_month != 12 :
                self.__now_month += 1
            else:
                self.__now_year += 1
                self.__now_month = 1
        file_path = 'currency' + '/' + \
                    self.__currency + '/' + \
                    str(self.__now_year) + '-' + \
                    str(self.__now_month)
        self.__file_input = open(file_path,'rt')
        return file_path

    def __change_path(self):
        while not ('currency.py' in os.listdir('.')):
            os.chdir('../')

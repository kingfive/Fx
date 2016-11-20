import random

def get(currency):
    data = currency.get_data()
    return data

def one_or_minus():
    l = [-1,1]
    ans = random.choice(l)
    return ans

def random_update(account,currency,time):
    ran = random.randint(int(time*0.5) , time)
    for i in range(ran):
        data = currency.get_data()
        account.update( data )
    return data


def print_earn(account):
    for i in account.earn:
        print(i)

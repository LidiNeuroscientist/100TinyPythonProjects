
def Increase(price=0, dis=0, format=False):
    '''
    Calculates the increase in a given price by returning the result with or without formatting
    :param price: The price that you want to format
    :param dis: value of the discount wanted
    :param format: Do you want the output with currency format or only the value
    :return: the price formatted with or without thw currency
    '''
    res = price + ((price * dis) / 100)
    return res if format is False else Currency(res)


def Decrease(price=0, dis=0, format=False):
    res = price - ((price * dis) / 100)
    return res if format is False else Currency(res)


def Double(price=0, format=False):
    res = price * 2
    return res if format is False else Currency(res)


def Half(price=0, format=False):
    res = price / 2
    return res if format is False else Currency(res)


def Currency(price=0, currency='EUR'):
    return f'{currency} {price:.2f}'.replace('.', ',')


def Summary(price=0, inc=10, dis=5): # price given, inc= % that will increase, dis = % of discount
    '''Calculates the increase in a given price by returning the result with or without formatting
    :param price: The price that you want to format
    :param inc: value of increase, if you dont type give 10%
    :param dis: value of discount, if you dont type give 5%
    :return: the price formatted with or without thw currency
    '''
    print('-' * 30)
    print('SUMMARY OF PRICES'.center(30))
    print('-' * 30)
    print(f'The Price is: \t\t{Currency(price)}')  # \t means tabulation
    print(f'The DOUBLE is: \t\t{Double(price, True)}')
    print(f'The HALF is: \t\t{Half(price, True)}')
    print(f'With {inc}% increase: \t{Increase(price, inc, True)}')
    print(f'With {dis}% discount: \t{Decrease(price, dis, True)}')
    print('-' * 30)

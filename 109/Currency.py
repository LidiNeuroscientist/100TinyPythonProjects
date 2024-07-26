
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

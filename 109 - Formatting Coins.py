'''COINS PART 2

Modify the functions that were created in challenge 107 so that they accept one
more parameter. Informing whether or not the value returned by them will be
formatted by the currency() function, from challenge 108 '''



def Increase(price=0, dis=0, format=False):
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


# PRINCIPAL PROGRAM
price = float(input('Type a PRICE: EUR '))
print(f'The price of {Currency(price)} with 10% INCREASE is:'
      f' {Increase(price, 10, True)}')
print(f'The price of {Currency(price)} with 20% DISCOUNT is:'
      f' {Decrease(price, 20, True)}')
print(f'The DOUBLE of {Currency(price)} is: '
      f' {Double(price, True)}')
print(f'The HALF of {Currency(price)} is:'
      f' {Half(price, False)}')

# If you insert the parameter True shows the currency if put False shows only
# the value
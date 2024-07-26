''' FORMATTING COINS

Adapt the code from challenge 107, creating an additional currency() function
that can display the as a formatted monetary value. '''



def Increase(n=0, dis=0):
    res = n + ((n * dis) / 100)
    return res


def Decrease(n=0, dis=0):
    res = n - ((n * dis) / 100)
    return res


def Double(n=0):
    res = n * 2
    return res


def Half(n=0):
    res = n / 2
    return res


def Currency(n=0, currency='EUR'):
    return f'{currency} {n:.2f}'.replace('.', ',')


# PRINCIPAL PROGRAM
price = float(input('Type a PRICE: EUR '))
print(f'The price of {Currency(price)} with 10% INCREASE is: '
      f'{Currency(Increase(price, 10))}')
print(f'The price of {Currency(price)} with 20% DISCOUNT is:'
      f' {Currency(Decrease(price, 20))}')
print(f'The DOUBLE of {Currency(price)} is: '
      f' {Currency(Double(price))}')
print(f'The HALF of {Currency(price)} is:'
      f' {Currency(Half(price))}')

'''MODULE EXERCISE

Create a module called currency.py that has the built-in functions increase(
), decrease(), double(), half().

Also make a program that imports this module and uses some of these functions '''

''' OBS: WITHOUT MODULES OR LIBRARY HERE '''

def Increase(n, dis):
    res = n + ((n * dis) / 100)
    return res


def Decrease(n, dis):
    res = n - ((n * dis) / 100)
    return res


def Double(n):
    res = n * 2
    return res


def Half(n):
    res = n / 2
    return res


# PRINCIPAL PROGRAM
price = float(input('Type a PRICE: EUR '))
print(f'The prince with 10% INCREASE: EUR {Increase(price, 10)}')
print(f'The price with 20% DISCOUNT: EUR {Decrease(price, 20)}')
print(f'The DOUBLE of the price: EUR {Double(price)}')
print(f'The HALF of the price: EUR {Half(price)}')

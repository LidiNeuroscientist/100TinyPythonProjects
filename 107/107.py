import Currency


# PRINCIPAL PROGRAM
price = float(input('Type a PRICE: EUR '))
print(f'The prince with 10% INCREASE: EUR {Currency.Increase(price, 10)}')
print(f'The price with 20% DISCOUNT: EUR {Currency.Decrease(price, 20)}')
print(f'The DOUBLE of the price: EUR {Currency.Double(price)}')
print(f'The HALF of the price: EUR {Currency.Half(price)}')

from Currency import Currency, Increase, Decrease, Double, Half

# PRINCIPAL PROGRAM
price = float(input('Type a PRICE: EUR '))
print(f'The price of {Currency(price)} with 10% INCREASE is:'
      f' {Increase(price, 10, True)}')
print(f'The price of {Currency(price)} with 20% DISCOUNT is:'
      f' {Decrease(price, 20, True)}')
print(f'The DOUBLE of {Currency(price)} is: '
      f' {Double(price, True)}')
print(f'The HALF of {Currency(price)} is:'
      f' {Half(price, True)}')

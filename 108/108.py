import Currency

# PRINCIPAL PROGRAM
price = float(input('Type a PRICE: EUR '))
print(f'The price of {Currency.Currency(price)} with 10% INCREASE is:'
      f' {Currency.Currency(Currency.Increase(price, 10))}')
print(f'The price of {Currency.Currency(price)} with 20% DISCOUNT is:'
      f' {Currency.Currency(Currency.Decrease(price, 20))}')
print(f'The DOUBLE of {Currency.Currency(price)} is: '
      f' {Currency.Currency(Currency.Double(price))}')
print(f'The HALF of {Currency.Currency(price)} is:'
      f' {Currency.Currency(Currency.Half(price))}')
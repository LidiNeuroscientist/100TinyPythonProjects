''' PAYMENT MANAGER

create a program that calculates the amount to be paid for a product,
considering its normal price and payment terms:

- cash or check: 10% discount
- card payment: 5% discount
- up to 2x by card: normal price
- 3x or more: 20% interest added  '''


print('{:-^75}'.format('BOL.COM'))
p = float(input('\033[1;97mType the product PRICE: EUR \033[m'))
print('\033[1;31m[1] Cash\033[m \n\033[1;32m[2] Debit card\033[m \n\033[1;33m['
      '3] 2x Credit card\033[m \n\033[1;34m[4] Above 3x Credit '
      'card\033[m')
m = int(input('\033[1;97mType the NUMBER of payment METHOD: \033[m'))
print('--' * 39)
if m == 1:
    np = p - (p * 10 / 100)
    print('\033[1;31mPaying with CASH you get 10% discount: NEW PRICE IS EUR {}\033[m'.format(np))
elif m == 2:
    np = p - (p * 5 / 100)
    print('\033[1;32mPaying with DEBIT CARD you get 5% discount: NEW PRICE IS EUR {}\033[m'.format(np))
elif m == 3:
    mp = p / 2
    print('\033[1;33mPaying in 2x by Credit card: PRICE IS EUR {} \nThe '
          'monthly payment will be: EUR {} \033['
          'm'.format(p, mp))
else:
    m = int(input('\033[1;97mHow many installments? \033[m'))
    np = p + (p * 20 / 100)
    mp = np / m
    print('\033[1;34mPaying in {}x by Credit card, the price raises '
          '20%: NEW PRICE IS EUR {} \nThe monthly payment will be: EUR {'
          '}\033[m'.format(m, np, mp))

''' TABULAR AND PRICES

create a program that has a single tuple with product names and their
respective prices in the sequence at the end show a price list organizing
data in tabular form (PRICE TABLE) '''


print('-=-' * 14)
print('\033[1;97mPRODUCTS AND PRICES\033[m'.center(50))
print('-=-' * 14)
list = ('Potato', '1.00', 'Banana', '1.55', 'Tomato', '1.29',
         'Cabbage', '1.79', 'Garlic', '0.99', 'Onion', '1.89')
for item in range(0, len(list)):
    if item % 2 == 0:
        print(f'{list[item]:.<30}', end=' ')
    else:
        print(f'EUR {list[item]:>5}')
print('\033[1;97m-=-' * 14)
print('THANKS FOR YOUR VISIT'.center(40))
